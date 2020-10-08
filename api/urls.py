from django.conf.urls import url
from . import views


urlpatterns = [
    url('^exit/', views.ExitView.as_view({'get': 'list', 'post': 'create'})),
    url('^room/', views.RoomView.as_view({'get': 'list', 'post': 'create'})),
    url('^note/', views.NoteView.as_view({'get': 'list', 'post': 'create'})),
]
