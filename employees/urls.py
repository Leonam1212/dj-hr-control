from django.urls import path
from .views import EmployeeView
urlpatterns = [ #(4)
    path('employees/', EmployeeView.as_view()),
]