from django.urls import path

from contracts.views import (CreateContractView, ListContractView,
                             UpdateAndDeleteContractView)

urlpatterns = [
    path("contracts/create/<str:employee_id>/", CreateContractView.as_view()),
    path("contracts/", ListContractView.as_view()),
    path("contracts/<str:id>/", UpdateAndDeleteContractView.as_view()),
]
