from django.conf.urls import url  # type: ignore
from . import views


urlpatterns = [
    url("^area/", views.AreaView.as_view({"get": "list"})),
    url("^exit/", views.ExitView.as_view({"get": "list", "post": "create"})),
    url("^room/", views.RoomView.as_view({"get": "list", "post": "create"})),
    # url('^note/', views.NoteView.as_view({'get': 'list', 'post': 'create'})),
]
