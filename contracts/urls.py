from django.urls import path
from contracts.views import ContractView, UpdateAndDeleteContractView

urlpatterns = [ #(4)
    path('contracts/', ContractView.as_view()),
    path('contracts/<str:id>', UpdateAndDeleteContractView.as_view()),

]