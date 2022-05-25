from django.urls import path
from .views import LoginView, AccountView, AccountUpdateAndDeleteView

urlpatterns = [
    path("accounts/", AccountView.as_view()),
    path("accounts/<pk>",AccountUpdateAndDeleteView.as_view()),
    path("login/",LoginView.as_view())
]