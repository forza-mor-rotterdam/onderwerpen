from django.contrib.admin.views.decorators import staff_member_required


@staff_member_required
def test_teams_error_view(request):
    raise RuntimeError(
        "Testfout vanuit /beheer/test-teams-foutmelding/ — "
        "om de Power Automate-webhook end-to-end te verifiëren."
    )
