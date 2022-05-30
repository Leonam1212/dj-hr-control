from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics, status
from rest_framework.response import Response
from employees.models import Employee
from work_days.models import WorkDay
from datetime import date, datetime

from work_days.models import WorkDay
from work_days.serializers import WorkDaySerializer
from accounts.permissions import IsRH

class MakeCheckInView(generics.GenericAPIView):
  qyeryset = WorkDay.objects.all()
  serializer_class = WorkDaySerializer

  def post(self, response: Response, personal_code=""):
    try:
      today = datetime.now()
      employee = Employee.objects.all().filter(personal_code=personal_code).first()
      dayFilter = WorkDay.objects.all().filter(employee_code=personal_code).filter(date=today.date())
      
      if not employee: 
        raise ObjectDoesNotExist

      if dayFilter:
        time_checkin = dayFilter.first().checkin
        duration = datetime.combine(date.min, today.time()) - datetime.combine(date.min, time_checkin)
        dayFilter.update(checkout=today, time_worked=str(duration))

        serialized = WorkDaySerializer(dayFilter.first())

        return Response(serialized.data, status.HTTP_201_CREATED)

      new_work_day = WorkDay.objects.create(employee_code=employee)

      serialized = WorkDaySerializer(new_work_day)
      
      return Response(serialized.data, status.HTTP_201_CREATED)

    except(ObjectDoesNotExist):
      return Response({"detail": "Employee not found"}, status.HTTP_404_NOT_FOUND)

class WorkDayView(generics.ListCreateAPIView):
  permission_classes = [IsRH]
  queryset = WorkDay.objects.all()
  serializer_class = WorkDaySerializer

class WorkDayByIdView(generics.UpdateAPIView, generics.DestroyAPIView):
  permission_classes = [IsRH]
  queryset = WorkDay.objects.all()
  serializer_class = WorkDaySerializer
  lookup_field = "id"