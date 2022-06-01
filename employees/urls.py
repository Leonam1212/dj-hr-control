from django.urls import path
from .views import EmployeeView, UpdateDestroyEmployeeView, CreateWorkScheduleView

urlpatterns = [
    path('employees/', EmployeeView.as_view()),
    path('employees/<str:id>/', UpdateDestroyEmployeeView.as_view()),
    path("work_schedule/<str:type>", CreateWorkScheduleView.as_view())
]
