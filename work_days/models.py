from uuid import uuid4

from django.db import models

class WorkDay(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    checkin = models.DateTimeField(auto_now_add=True)
    checkout = models.DateTimeField(null=True)
    time_worked = models.TimeField(null=True)
    is_holiday = models.BooleanField(default=False)
    is_weekend = models.BooleanField(default=False)

    """ employee_code = models.ForeignKey("employees.Employee",
                                        on_delete=models.DO_NOTHING,
                                        to_field="personal_code",
                                        db_column="employee_code") """
                                    