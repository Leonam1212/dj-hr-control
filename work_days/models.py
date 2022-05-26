from uuid import uuid4
import datetime

from django.db import models

class Work_day(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    checkin = models.DateTimeField(auto_now_add=True)
    checkout = models.DateTimeField()
    time_worked = models.TimeField(default=datetime.time(0,0,0))
    is_holiday = models.BooleanField(default=False)
    is_weekend = models.BooleanField(default=False)

    employee_code = models.ForeignKey("employees.Employee",
                                        on_delete=models.DO_NOTHING,
                                        to_field="personal_code",
                                        db_column="employee_code")
                                    