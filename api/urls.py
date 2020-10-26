from django.conf.urls import url  # type: ignore
from rest_framework import permissions  # type: ignore
from drf_yasg.views import get_schema_view  # type: ignore
from drf_yasg import openapi  # type: ignore

from . import views

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    url("^area/", views.AreaView.as_view({"get": "list"})),
    url("^exit/", views.ExitView.as_view({"get": "list", "post": "create"})),
    url("^room/", views.RoomView.as_view({"get": "list", "post": "create"})),
    # url('^note/', views.NoteView.as_view({'get': 'list', 'post': 'create'})),
    url(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    url(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    url(
        r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
]
