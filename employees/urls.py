from django.urls import path
from .views import EmployeeView, UpdateEmployeeView
urlpatterns = [ #(4)
    path('employees/', EmployeeView.as_view()),
    path('employees/<str:id>', UpdateEmployeeView.as_view()),
]