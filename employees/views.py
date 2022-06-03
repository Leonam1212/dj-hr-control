import calendar
from datetime import datetime

from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response

from accounts.permissions import IsRH
from shifts.models import Shift

from .models import Employee
from .serializers import EmployeeSerializer


class EmployeeView(generics.ListCreateAPIView):
    permission_classes = [IsRH]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    def get_serializer_class(self):
        if self.request.method == "GET":
            return EmployeeSerializer
        return super().get_serializer_class()

class UpdateDestroyEmployeeView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsRH]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = "id"

class CreateWorkScheduleView(generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request: Request):

        newSchedule = createSchedule()
        return Response(newSchedule)
            
            
def createSchedule():
    date = datetime.now()
    month = date.month
    month_range = calendar.monthrange(date.year, date.month)
    month_name = {
        1: "Janeiro",
        2: "Fevereiro",
        3: "Março",
        4: "Abril",
        5: "Maio",
        6: "Junho",
        7: "Julho",
        8: "Agosto",
        9: "Setembro",
        10: "Outubro",
        11: "Novembro",
        12: "Dezembro"
    }
    week_name = {
        0: "Segunda-feira",
        1: "Terça-feira",
        2: "Quarta-feira",
        3: "Quinta-feira",
        4: "Sexta-feira",
        5: "Sabado",
        6: "Domingo"
    }


    def schedule():
        table = {}

        avaliable_shifts = Shift.objects.all()
        # shifts_name = [shift.name for shift in avaliable_shifts]

        avaliable_employees = Employee.objects.all()
        employee_shift = [(employee.name, employee.contract.work_shift.name) for employee in avaliable_employees]
        
        for day in range(month_range[1]):
            days = {}
            days["dia da semana"] = [week_name[calendar.weekday(date.year, date.month, day+1)]]
            
            for shift in avaliable_shifts:
                days[shift.name]= []

                for person in employee_shift:
        
                    if(person[1] == shift.name):
                        days[shift.name].append(person[0])
                
            table[day+1] = days
            
        return table
    
    table = {}
    table["month"] = month_name[month]
    table["month_range"] = month_range[1]
    table["first_day_week"] = month_range[0]
    table["schedule"] = schedule()

    return table