from rest_framework import generics
from accounts.permissions import IsRH
from shifts.models import Shift
from shifts.serializers import ShiftSerializer
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.request import Request
from rest_framework.response import Response
from datetime import datetime
import calendar


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
    def post(self, request: Request, type=""):
       

            employee_list = Employee.objects.all()
            employees = EmployeeSerializer(employee_list, many=True)
            shift_list = Shift.objects.all()
            shifts = ShiftSerializer(shift_list, many=True)
            newSchedule = createSchedule(employees.data, shifts.data)

            return Response(newSchedule)
        
def createSchedule(employees ,shifts):
    date = datetime.now()
    month = date.month
    month_range = calendar.monthrange(date.year, date.month)
    month_name = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    week_name = {
        6: "Sunday",
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday"
    }


    def schedule():
        table = {}
        


        for day in range(month_range[1]):
            days = {}
            days["week_day"] = week_name[calendar.weekday(date.year, date.month, day+1)]
            
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