import django_filters  # type: ignore
from rest_framework import viewsets  # type: ignore

from .serializers import AreaSerializer, RoomSerializer, ExitSerializer
from .models import Room, Exit


class AreaView(viewsets.ModelViewSet):
    serializer_class = AreaSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = "__all__"
    queryset = (
        Room.objects.exclude(area__endswith="(ship)")
        .exclude(area__endswith="(player city)")
        .distinct("area")
    )


class RoomView(viewsets.ModelViewSet):
    serializer_class = RoomSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = "__all__"
    queryset = Room.objects.all()


class ExitView(viewsets.ModelViewSet):
    serializer_class = ExitSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = "__all__"
    queryset = Exit.objects.all()


"""
class NoteView(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = '__all__'
    queryset = Note.objects.all()
"""
