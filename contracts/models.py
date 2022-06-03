from uuid import uuid4

from django.db import models


class Contract(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    contract_type = models.CharField(max_length=20)
    contract_duration = models.DateField()
    salary = models.DecimalField(max_digits=6, decimal_places=2)
    position = models.CharField(max_length=150)
    work_shift = models.ForeignKey(
        "shifts.Shift", related_name="contracts", on_delete=models.DO_NOTHING, null=True
    )
