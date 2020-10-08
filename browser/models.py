from django.db import models


class Room(models.Model):
    id = models.TextField(primary_key=True)
    shortdesc = models.TextField()
    longdesc = models.TextField()
    area = models.TextField()
    indoors = models.BooleanField()
    exits = models.TextField()

    class Meta:
        db_table = "room"


class Exit(models.Model):
    direction = models.TextField(primary_key=True)
    source = models.ForeignKey(
        Room, on_delete=models.CASCADE, primary_key=True, db_column="source"
    )
    destination = models.ForeignKey(
        Room, on_delete=models.CASCADE, primary_key=True, db_column="destination"
    )

    class Meta:
        db_table = "exit"
