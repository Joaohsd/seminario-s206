from __future__ import annotations

import uuid

from django.db import models


class ParkingLot(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Car(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    year = models.DateTimeField()
    is_parked = models.BooleanField(default=False)
    parked_in = models.ForeignKey(ParkingLot, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
