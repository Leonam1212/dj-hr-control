from rest_framework import generics

from work_days.models import WorkDay
from work_days.serializers import WorkDaySerializer

class WorkDayView(generics.ListCreateAPIView):
  queryset = WorkDay.objects.all()
  serializer_class = WorkDaySerializer

class WorkDayByIdView(generics.UpdateAPIView):
  queryset = WorkDay.objects.all()
  serializer_class = WorkDaySerializer
  lookup_field = "id"