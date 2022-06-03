from rest_framework import generics

from accounts.permissions import IsRH
from shifts.models import Shift
from shifts.serializers import ShiftSerializer


class ListShiftView(generics.ListCreateAPIView):
    permission_classes = [IsRH]

    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
    lookup_field = "id"


class UpdateAndDeleteShiftView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsRH]

    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
    lookup_field = "id"
