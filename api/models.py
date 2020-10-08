from django.db import models


class Room(models.Model):
    shortdesc = models.TextField()
    longdesc = models.TextField()
    area = models.TextField(null=True, blank=True)
    indoors = models.BooleanField()
    exits = models.TextField(null=True, blank=True)

    class Meta:
        db_table = "room"

    def __str__(self):
        return self.shortdesc


class Exit(models.Model):
    direction = models.TextField(null=True, blank=True)
    source = models.ForeignKey('Room', null=True, blank=True, on_delete=models.CASCADE, related_name='source')
    destination = models.ForeignKey('Room', null=True, blank=True, on_delete=models.CASCADE, related_name='destination')

    class Meta:
        db_table = "exit"

    def __str__(self):
        return self.direction, self.source, self.destination


class Note(models.Model):
    rooms = models.ForeignKey('Room', on_delete=models.CASCADE, related_name='rooms', null=True, blank=True)
    desc = models.TextField()

    class Meta:
        db_table = "note"

    def __str__(self):
        return self.id, self.desc, self.rooms
