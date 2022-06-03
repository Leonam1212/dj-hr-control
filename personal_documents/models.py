from uuid import uuid4

from django.core.validators import RegexValidator
from django.db import models


class Personal_document(models.Model):
  id = models.UUIDField(primary_key = True, default = uuid4, editable = True)
  cpf = models.CharField(max_length = 15, unique = True,
    validators=[
      RegexValidator(
        regex = r"[0-9]{3}[\.][0-9]{3}[\.][0-9]{3}[-][0-9]{2}$",
        message = "The cpf must follow the format: xxx.xxx.xxx-xx",
        code = 400,
      )
    ]
  )
  nit = models.CharField(max_length = 15, unique = True,
    validators=[
      RegexValidator(
        regex = r"[0-9]{3}[\.][0-9]{5}[\.][0-9]{2}[-][0-9]{1}$",
        message = "The nit must follow the format: xxx.xxxxx.xx-x",
        code = 400,
      )
    ]
  )
  rg = models.CharField(max_length = 15, unique = True,
    validators=[
      RegexValidator(
        regex = r"[0-9]{2}[\.][0-9]{3}[\.][0-9]{3}[-][0-9]{1}$",
        message = "The rg must follow the format: xx.xxx.xxx-x",
        code = 400,
      )
    ]
  )
  ctps = models.CharField(max_length = 15, unique = True,
    validators=[
      RegexValidator(
        regex = r"[0-9]{7}[-][0-9]{4}$",
        message = "The cpts must follow the format: xxxxxxx-xxxx",
        code = 400,
      )
    ]
  )
  cnpj = models.CharField(max_length = 20, null = True, unique = True,
    validators=[
      RegexValidator(
        regex = r"[0-9]{2}[\.][0-9]{3}[\.][0-9]{3}[\/][0-9]{4}[-][0-9]{2}$",
        message = "The cnpj must follow the format: xx.xxx.xxx/xxxx-xx",
        code = 400,
      )
    ]
  )