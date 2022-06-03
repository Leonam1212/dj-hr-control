from django.urls import path

from .views import CreateAddressView, ListAddressView, UpdateDestroyAddressView

urlpatterns = [
    path("addresses/create/<str:employee_id>/", CreateAddressView.as_view()),
    path("addresses/", ListAddressView.as_view()),
    path("addresses/<str:id>/", UpdateDestroyAddressView.as_view()),
]
