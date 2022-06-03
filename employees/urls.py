from django.urls import path

from .views import (CreateWorkScheduleView, EmployeeView,
                    UpdateDestroyEmployeeView)

urlpatterns = [
    path('employees/', EmployeeView.as_view()),
    path('employees/<str:id>/', UpdateDestroyEmployeeView.as_view()),
    path("work_schedule/", CreateWorkScheduleView.as_view())
]
