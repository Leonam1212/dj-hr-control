from rest_framework import generics

from work_days.models import WorkDay
from work_days.serializers import WorkDaySerializer
from accounts.permissions import IsRH

class WorkDayView(generics.ListCreateAPIView):
  permission_classes = [IsRH]
  queryset = WorkDay.objects.all()
  serializer_class = WorkDaySerializer

class WorkDayByIdView(generics.UpdateAPIView):
  permission_classes = [IsRH]
  queryset = WorkDay.objects.all()
  serializer_class = WorkDaySerializer
  lookup_field = "id"