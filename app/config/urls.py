from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions

from config import settings

admin_url = settings.ADMIN_URL

urlpatterns = [
    path(f"{admin_url}/", admin.site.urls, name="admin-url"),
]


if settings.DEBUG:
    try:
        import debug_toolbar  # noqa

        urlpatterns += [
            path("__debug__/", include(debug_toolbar.urls)),
        ]
    except ImportError:
        pass

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.ENV == "dev":
    from drf_yasg import openapi  # noqa
    from drf_yasg.views import get_schema_view  # noqa

    schema_view = get_schema_view(
        openapi.Info(
            title="GENESIS API",
            default_version="v1",
            description="",
            contact=openapi.Contact(email="hello@elefanto.kz"),
            license=openapi.License(name="MIT License"),
        ),
        public=True,
        permission_classes=[permissions.AllowAny],
    )

    urlpatterns += [
        path(
            "api/swagger/",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="schema-swagger",
        ),
        path(
            "api/redoc/",
            schema_view.with_ui("redoc", cache_timeout=0),
            name="schema-redoc",
        ),
    ]
