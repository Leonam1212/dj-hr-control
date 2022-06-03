from rest_framework.exceptions import APIException


class ShiftNotSentError(APIException):
    default_detail = {"shift": ["This field is required."]}
    status_code = 400
