from apps.authentication.views import (
    GebruikerAanmakenView,
    GebruikerAanpassenView,
    GebruikerLijstView,
    LoginView,
    LogoutView,
    gebruiker_bulk_import,
)
from apps.authorisatie.views import (
    RechtengroepAanmakenView,
    RechtengroepAanpassenView,
    RechtengroepLijstView,
    RechtengroepVerwijderenView,
)
from apps.beheer.views import (
    OnderwerpAanmakenView,
    OnderwerpAanpassenView,
    OnderwerpLijstView,
    beheer,
    http_404,
    http_500,
    root,
)
from apps.categories.viewsets import CategoryViewSet
from apps.groups.viewsets import GroupViewSet
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from django_db_schema_renderer.urls import schema_urls
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"group", GroupViewSet, basename="group")
router.register(r"category", CategoryViewSet, basename="category")

urlpatterns = [
    path("", root, name="root"),
    path("api/v1/", include((router.urls, "app"), namespace="v1")),
    path("api-token-auth/", views.obtain_auth_token),
    path("health/", include("health_check.urls")),
    path("db-schema/", include((schema_urls, "db-schema"))),
    path("plate/", include("django_spaghetti.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path(
        "login/",
        LoginView.as_view(),
        name="login",
    ),
    path(
        "logout/",
        LogoutView.as_view(),
        name="logout",
    ),
    path("beheer/", beheer, name="beheer"),
    path("beheer/gebruiker/", GebruikerLijstView.as_view(), name="gebruiker_lijst"),
    path(
        "beheer/gebruiker/aanmaken/",
        GebruikerAanmakenView.as_view(),
        name="gebruiker_aanmaken",
    ),
    path(
        "beheer/gebruiker/<int:pk>/aanpassen/",
        GebruikerAanpassenView.as_view(),
        name="gebruiker_aanpassen",
    ),
    path(
        "beheer/gebruiker/bulk-import/",
        gebruiker_bulk_import,
        name="gebruiker_bulk_import",
    ),
    path("beheer/onderwerp/", OnderwerpLijstView.as_view(), name="onderwerp_lijst"),
    path(
        "beheer/onderwerp/aanmaken/",
        OnderwerpAanmakenView.as_view(),
        name="onderwerp_aanmaken",
    ),
    path(
        "beheer/onderwerp/<uuid:pk>/aanpassen/",
        OnderwerpAanpassenView.as_view(),
        name="onderwerp_aanpassen",
    ),
    path(
        "beheer/rechtengroep/",
        RechtengroepLijstView.as_view(),
        name="rechtengroep_lijst",
    ),
    path(
        "beheer/rechtengroep/aanmaken/",
        RechtengroepAanmakenView.as_view(),
        name="rechtengroep_aanmaken",
    ),
    path(
        "beheer/rechtengroep/<int:pk>/aanpassen/",
        RechtengroepAanpassenView.as_view(),
        name="rechtengroep_aanpassen",
    ),
    path(
        "beheer/rechtengroep/<int:pk>/verwijderen/",
        RechtengroepVerwijderenView.as_view(),
        name="rechtengroep_verwijderen",
    ),
]

if not settings.ENABLE_DJANGO_ADMIN_LOGIN:
    urlpatterns += [
        path(
            "admin/login/",
            RedirectView.as_view(url="/login/?next=/admin/"),
            name="admin_login",
        ),
        path(
            "admin/logout/",
            RedirectView.as_view(url="/logout/?next=/"),
            name="admin_logout",
        ),
    ]

if settings.OIDC_ENABLED:
    urlpatterns += [
        path("oidc/", include("mozilla_django_oidc.urls")),
    ]

urlpatterns += [
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
        path("404/", http_404, name="404"),
        path("500/", http_500, name="500"),
    ]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
