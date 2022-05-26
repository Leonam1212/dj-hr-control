from django.urls import path
from .views import EmployeeView, UpdateDestroyEmployeeView

urlpatterns = [
    path('employees/', EmployeeView.as_view()),
    path('employees/<str:id>/', UpdateDestroyEmployeeView.as_view()),
]
