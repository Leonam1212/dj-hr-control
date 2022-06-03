from datetime import datetime
from uuid import uuid4

from django.db import models


def isweekend():
    if(datetime.now().weekday() == 0):
        return True
    if(datetime.now().weekday() == 6):
        return True
    return False

class WorkDay(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    date = models.DateField(auto_now_add=True, null=True)
    checkin = models.TimeField(auto_now_add=True, null=True)
    checkout = models.TimeField(null=True)
    time_worked = models.TimeField(null=True)
    is_weekend = models.BooleanField(default=isweekend())

    employee_code = models.ForeignKey("employees.Employee",
                                        on_delete=models.DO_NOTHING,
                                        to_field="personal_code",
                                        db_column="employee_code",
                                        null=True) 
                                    
