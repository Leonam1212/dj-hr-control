from django.urls import path

from .views import AccountUpdateAndDeleteView, AccountView, LoginView

urlpatterns = [
    path("accounts/", AccountView.as_view()),
    path("accounts/<id>/",AccountUpdateAndDeleteView.as_view()),
    path("login/",LoginView.as_view())
]