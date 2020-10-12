from django.db import models

class Exit(models.Model):
    direction = models.TextField(primary_key=True)
    source = models.ForeignKey('Room', on_delete=models.DO_NOTHING, db_column='source', related_name='source')
    destination = models.ForeignKey('Room', on_delete=models.DO_NOTHING, db_column='destination', related_name='destination')

    class Meta:
        db_table = 'exit'
        unique_together = (('direction', 'source', 'destination'),)


class Room(models.Model):
    id = models.TextField(primary_key=True)
    shortdesc = models.TextField()
    longdesc = models.TextField()
    area = models.TextField(blank=True, null=True)
    indoors = models.BooleanField(blank=True, null=True)
    exits = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'room'


"""
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
"""