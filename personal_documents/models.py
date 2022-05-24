from uuid import uuid4
from django.db import models

class Personal_document(models.Model):
  id = models.UUIDField(primary_key = True, default = uuid4, editable = True)
  cpf = models.CharField(max_length = 15)
  nit = models.CharField(max_length = 15)
  rg = models.CharField(max_length = 15)
  ctps = models.CharField(max_length = 15)
  cnpj = models.CharField(max_length = 15, null = True)