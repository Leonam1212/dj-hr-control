from uuid import uuid4

from django.core.validators import RegexValidator
from django.db import models


class Employee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=150)
    phone_number = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r"^\([1-9]{2}\) 9[1-9][0-9]{3}-[0-9]{4}$",
                message="The phone number must follow the format: (xx) 9xxxx-xxxx",
                code=400,
            )
        ],
    )
    personal_code = models.CharField(unique=True,
        max_length=6,
        validators=[
            RegexValidator(
                regex=r"^[0-9]{6}",
                message="the personal code is a string with six numbers, format: xxxxxx",
                code=400,
            )
        ],)

    contract = models.OneToOneField(
        "contracts.Contract",
        on_delete=models.SET_NULL,
        null=True,
    )

    personal_documents = models.OneToOneField(
        "personal_documents.Personal_document", on_delete=models.SET_NULL, null=True
    )

    address = models.ForeignKey(
        "addresses.Address",
        related_name="employees",
        on_delete=models.SET_NULL,
        null=True,
    )
