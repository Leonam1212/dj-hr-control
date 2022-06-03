from uuid import uuid4

from django.db import models


class Candidate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=150)
    pdf_file = models.FileField(upload_to='')
