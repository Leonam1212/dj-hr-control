from uuid import uuid4

from django.db import models


class Shift(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=20, unique=True)
    base_checkin = models.TimeField()
    base_checkout = models.TimeField()
