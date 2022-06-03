from rest_framework.exceptions import APIException


class ShiftNotFoundError(APIException):
    default_detail = "Shift not found in the database."
    status_code = 400
