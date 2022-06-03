from uuid import uuid4

from django.core.validators import RegexValidator
from django.db import models


class Address(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    street = models.CharField(max_length=150)
    number = models.IntegerField()
    complement = models.CharField(max_length=150)
    postal_code = models.CharField(max_length=9,
        validators=[
            RegexValidator(
                regex=r"^[0-9]{5}(?:-[0-9]{3})?$",
                message="The postal_code number must follow the format: xxxxx-xxx",
                code=400,
            )
        ],)
