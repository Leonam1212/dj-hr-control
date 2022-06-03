from datetime import date, datetime

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response

from accounts.permissions import IsRH
from employees.models import Employee
from work_days.models import WorkDay
from work_days.serializers import WorkDaySerializer


class MakeCheckInView(generics.GenericAPIView):
  qyeryset = WorkDay.objects.all()
  serializer_class = WorkDaySerializer

  def post(self, request: Request, personal_code=""):
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
        dayFilter.first().save()

        serialized = WorkDaySerializer(dayFilter.first())

        return Response(serialized.data, status.HTTP_201_CREATED)

      new_work_day = WorkDay.objects.create(employee_code=employee)

      serialized = WorkDaySerializer(new_work_day)
      
      return Response(serialized.data, status.HTTP_201_CREATED)

    except(ObjectDoesNotExist):
      return Response({"detail": "Employee not found"}, status.HTTP_404_NOT_FOUND)

class GetWorkDaysByPersonalCode(generics.GenericAPIView):
  permission_classes = [IsRH]
  qyeryset = WorkDay.objects.all()
  serializer_class = WorkDaySerializer

  def get(self, request: Request, personal_code=""):
    try:
      dayFilter = WorkDay.objects.all().filter(employee_code=personal_code)

      if not dayFilter:
        raise ObjectDoesNotExist
      
      serialized = WorkDaySerializer(dayFilter, many=True)
      
      return Response(serialized.data, status.HTTP_200_OK)

    except(ObjectDoesNotExist):
      return Response({"detail": "Personal code not found, or nothing registered"}, status.HTTP_404_NOT_FOUND)

class WorkDayView(generics.ListCreateAPIView):
  permission_classes = [IsRH]
  queryset = WorkDay.objects.all()
  serializer_class = WorkDaySerializer

class WorkDayByIdView(generics.UpdateAPIView, generics.DestroyAPIView):
  permission_classes = [IsRH]
  queryset = WorkDay.objects.all()
  serializer_class = WorkDaySerializer
  lookup_field = "id"