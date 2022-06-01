from rest_framework.exceptions import APIException
from shifts.models import Shift


class ShiftNotFoundError(APIException):
    avaliable_shifts = Shift.objects.all()
    shifts_name = [shift.name for shift in avaliable_shifts]

    default_detail = {
        "detail": "Shift not found in the database.",
        "avaliable_shifts": shifts_name,
    }
    status_code = 400
