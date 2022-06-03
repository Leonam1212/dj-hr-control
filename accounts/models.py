from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models


class Account(AbstractUser):
    id = models.UUIDField(primary_key=True ,editable=False, default=uuid4)
    email = models.EmailField(unique=True, max_length=255, null=False)
    password = models.CharField(max_length=255)
    username = None

    USERNAME_FIELD: str = 'email'
    REQUIRED_FIELDS = []