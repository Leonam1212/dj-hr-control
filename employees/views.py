from rest_framework.request import Request
from rest_framework.response import Response
from datetime import datetime
from createPdf.jinja import createPDF
from django.core.exceptions import ObjectDoesNotExist
from django.http import FileResponse
from rest_framework import generics
import calendar

from accounts.permissions import IsRH
from shifts.models import Shift
from shifts.serializers import ShiftSerializer
from .models import Employee
from .serializers import EmployeeDetailedSerializer, EmployeeSerializer, EmployeeScheduleSerializer



class EmployeeView(generics.ListCreateAPIView):
    permission_classes = [IsRH]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    def get_serializer_class(self):
        if self.request.method == "GET":
            return EmployeeDetailedSerializer
        return super().get_serializer_class()

class UpdateDestroyEmployeeView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsRH]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = "id"

class CreateWorkScheduleView(generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeScheduleSerializer

    def get(self, request: Request, type=""):
        try:
            employee_list = Employee.objects.all()
            employees = EmployeeScheduleSerializer(employee_list, many=True)
            shift_list = Shift.objects.all()
            shifts = ShiftSerializer(shift_list, many=True)
            newSchedule = createSchedule(employees.data, shifts.data)
            if not employee_list:
                raise ObjectDoesNotExist

            if type == "json":
                return Response(newSchedule)
            if type == "pdf":
                createPDF(newSchedule)
                return FileResponse(open('createPdf/output/file.pdf', 'rb'))
            return Response({"error": "type not found."})
        except(ObjectDoesNotExist):
            return Response({"detail": "Employee not found"}, status.HTTP_404_NOT_FOUND)

            
        
def createSchedule(employees ,shifts):
    date = datetime.now()
    month = date.month
    month_range = calendar.monthrange(date.year, date.month)
    month_name = {
        1: "Janeiro",
        2: "Fevereiro",
        3: "Março",
        4: "Abril",
        5: "Maio",
        6: "Juinho",
        7: "Julho",
        8: "Agosto",
        9: "Setembro",
        10: "Outubro",
        11: "Novembro",
        12: "Dezembro"
    }
    week_name = {
        6: "Segunda-feira",
        0: "Terça-feira",
        1: "Quarta-feira",
        2: "Quinta-feira",
        3: "Sexta-feira",
        4: "Sabado",
        5: "Saturday"
    }


    def schedule():
        table = {}
        
        for day in range(month_range[1]):
            days = {}
            days["week_day"] = [week_name[calendar.weekday(date.year, date.month, day+1)]]
            
            for shift in shifts:
                days[shift["name"]] = []

                for employee in employees:
                    shift_name = employee['contract']['work_shift']['name']
                    if(shift_name == shift["name"]):
                        days[shift["name"]].append(employee['name'])
                
            table[day+1] = days
            
        return table
    
    table = {}
    table["month"] = month_name[month]
    table["month_range"] = month_range[1]
    table["first_day_week"] = month_range[0]
    table["schedule"] = schedule()

    return table