from uuid import uuid4
from django.db import models

# Create your models here.
class Contract(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    contract_type = models.CharField(max_length=20)
    contract_duration = models.DateField()
    salary = models.FloatField()
    position = models.CharField(max_length=150)
    work_shift = models.CharField(max_length=20)

    