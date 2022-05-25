from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from accounts.models import Account

class IsRH(BasePermission):
    def has_permission(self, request: Request, _):
        user: Account = request.user

        if not user.is_authenticated:
            return False

        return True