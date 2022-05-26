from django.urls import path
from .views import AddressView, UpdateDestroyAddressView
urlpatterns = [ #(4)
    path('addresses/', AddressView.as_view()),
    path('addresses/<str:id>', UpdateDestroyAddressView.as_view()),
]