import django_filters
from rest_framework import viewsets

from .serializers import RoomSerializer, ExitSerializer
from .models import Room, Exit


class RoomView(viewsets.ModelViewSet):
    serializer_class = RoomSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = '__all__'
    queryset = Room.objects.all()


class ExitView(viewsets.ModelViewSet):
    serializer_class = ExitSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = '__all__'
    queryset = Exit.objects.all()

"""
class NoteView(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = '__all__'
    queryset = Note.objects.all()
"""