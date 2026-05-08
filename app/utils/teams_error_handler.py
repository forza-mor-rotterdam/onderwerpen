import datetime as _dt
import logging
import os
import socket
import threading

import requests
from django.conf import settings
from django.utils.log import AdminEmailHandler
from django.views.debug import ExceptionReporter


_TRACEBACK_BUDGET_BYTES = 20_000
_USER_AGENT_LIMIT = 256

_logger = logging.getLogger(__name__)


class TeamsWebhookHandler(AdminEmailHandler):
    """Logging handler that POSTs error reports to a Power Automate webhook.

    Mirrors AdminEmailHandler's contract (only fires on logged errors,
    extracts the request from the LogRecord, reuses Django's ExceptionReporter)
    but delivers an Adaptive Card to a Microsoft Teams chat instead of email.
    """

    _local = threading.local()

    def emit(self, record):
        try:
            if getattr(self._local, "in_emit", False):
                return
            self._local.in_emit = True

            url = getattr(settings, "TEAMS_WEBHOOK_URL", "") or ""
            if not url:
                return

            request = getattr(record, "request", None)
            subject = self.format_subject(
                "%s: %s" % (record.levelname, record.getMessage())
            )

            traceback_text = ""
            if record.exc_info:
                exc_type, exc_value, tb = record.exc_info
                reporter = ExceptionReporter(
                    request, exc_type, exc_value, tb, is_email=True
                )
                traceback_text = reporter.get_traceback_text()

            payload = build_adaptive_card(
                subject=subject,
                level=record.levelname,
                request=request,
                record=record,
                traceback_text=traceback_text,
            )

            try:
                response = requests.post(url, json=payload, timeout=(3, 5))
                if response.status_code >= 400:
                    _logger.warning(
                        "TeamsWebhookHandler POST to %s returned %d: %s",
                        url,
                        response.status_code,
                        response.text[:500],
                    )
            except Exception:
                _logger.warning(
                    "TeamsWebhookHandler POST to %s failed", url, exc_info=True
                )
        except Exception:
            _logger.exception("TeamsWebhookHandler crashed in emit()")
        finally:
            self._local.in_emit = False


def build_adaptive_card(*, subject, level, request, record, traceback_text):
    body = [_header_block(subject=subject, level=level)]

    if request is not None:
        body.append({"type": "FactSet", "facts": _request_facts(record, request)})
    body.append({"type": "FactSet", "facts": _env_facts(record)})

    if record.exc_info:
        exc_type, exc_value, _ = record.exc_info
        body.append(
            {
                "type": "TextBlock",
                "text": f"{exc_type.__name__}: {exc_value}",
                "weight": "Bolder",
                "wrap": True,
                "fontType": "Monospace",
            }
        )

    actions = []
    if traceback_text:
        body.append(
            {
                "type": "Container",
                "id": "traceback",
                "isVisible": False,
                "items": [
                    {
                        "type": "TextBlock",
                        "text": _fenced_code(_truncate(traceback_text)),
                        "wrap": True,
                        "fontType": "Monospace",
                    }
                ],
            }
        )
        actions.append(
            {
                "type": "Action.ToggleVisibility",
                "title": "Show traceback",
                "targetElements": ["traceback"],
            }
        )

    content = {
        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
        "type": "AdaptiveCard",
        "version": "1.4",
        "body": body,
    }
    if actions:
        content["actions"] = actions

    return {
        "type": "message",
        "attachments": [
            {
                "contentType": "application/vnd.microsoft.card.adaptive",
                "content": content,
            }
        ],
    }


def _header_block(*, subject, level):
    color = {"ERROR": "Attention", "CRITICAL": "Attention", "WARNING": "Warning"}.get(
        level, "Default"
    )
    return {
        "type": "TextBlock",
        "text": f"[onderwerpen] {level}: {subject}",
        "weight": "Bolder",
        "color": color,
        "wrap": True,
    }


def _request_facts(record, request):
    user = getattr(request, "user", None)
    if user is not None and getattr(user, "is_authenticated", False):
        user_label = str(user)
    else:
        user_label = "anonymous"

    ip = request.META.get("REMOTE_ADDR", "—")
    forwarded = request.META.get("HTTP_X_FORWARDED_FOR")
    if forwarded:
        ip = f"{ip} (X-Forwarded-For: {forwarded})"

    user_agent = request.META.get("HTTP_USER_AGENT", "—")
    if len(user_agent) > _USER_AGENT_LIMIT:
        user_agent = user_agent[: _USER_AGENT_LIMIT - 1] + "…"

    status_code = getattr(record, "status_code", None)
    return [
        {"title": "Method", "value": request.method or "—"},
        {"title": "Path", "value": request.get_full_path()},
        {"title": "Status", "value": str(status_code) if status_code else "—"},
        {"title": "User", "value": user_label},
        {"title": "IP", "value": ip},
        {"title": "User-Agent", "value": user_agent},
        {"title": "Referer", "value": request.META.get("HTTP_REFERER", "—")},
    ]


def _env_facts(record):
    timestamp = _dt.datetime.utcfromtimestamp(record.created).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )
    return [
        {"title": "Service", "value": "onderwerpen"},
        {"title": "Hostname", "value": socket.gethostname()},
        {"title": "Git SHA", "value": os.environ.get("GIT_SHA") or "—"},
        {"title": "Timestamp", "value": timestamp},
        {"title": "Logger", "value": record.name},
    ]


def _truncate(text):
    encoded = text.encode("utf-8")
    if len(encoded) <= _TRACEBACK_BUDGET_BYTES:
        return text
    head = encoded[:_TRACEBACK_BUDGET_BYTES].decode("utf-8", errors="ignore")
    return f"{head}\n… [truncated, {len(encoded) - _TRACEBACK_BUDGET_BYTES} more bytes]"


def _fenced_code(text):
    return f"```\n{text}\n```"
