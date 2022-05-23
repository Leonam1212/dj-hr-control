from uuid import uuid4

from django.core.validators import RegexValidator
from django.db import models


class Employee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=150)
    phone_number = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r"^\([1-9]{2}\) (?:[2-8]|9[1-9])[0-9]{3}-[0-9]{4}$",
                message="The phone number must  follow the format: (xx) xxxxx-xxxx",
                code=400,
            )
        ],
    )

    # contract = models.OneToOneField("contracts.Contract", on_delete=models.CASCADE)

    # personal_documents = models.OneToOneField("personal_documents.PersonalDocuments", on_delete=models.CASCADE)

    # address = models.ForeignKey("addresses.Address", on_delete=models.DO_NOTHING)
