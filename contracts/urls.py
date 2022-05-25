from django.urls import path

from contracts.views import ContractView


urlpatterns = [ #(4)
    path('contracts/', ContractView.as_view()),
    path('contracts/<str:contract_id>', ContractView.as_view()),

]