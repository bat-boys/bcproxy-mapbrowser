from rest_framework import serializers  # type: ignore
from .models import Room, Exit


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ["area"]


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ["shortdesc", "longdesc", "area", "indoors", "exits"]


class ExitSerializer(serializers.ModelSerializer):
    source = serializers.PrimaryKeyRelatedField(queryset=Room.objects.all())
    destination = serializers.PrimaryKeyRelatedField(queryset=Room.objects.all())

    class Meta:
        model = Exit
        fields = ["source", "destination", "direction"]


"""
class NoteSerializer(serializers.ModelSerializer):
    rooms = serializers.PrimaryKeyRelatedField(
        queryset=Room.objects.all())

    class Meta:
        model = Note
        fields = ['desc', 'rooms']

    def create(self, validated_data):
        room = validated_data.pop('rooms')
        note = Note.objects.create(rooms=room, **validated_data)
        return note
"""
