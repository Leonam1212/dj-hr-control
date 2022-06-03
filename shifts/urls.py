from django.urls import path

from shifts.views import ListShiftView, UpdateAndDeleteShiftView

urlpatterns = [
    path("shifts/", ListShiftView.as_view()),
    path("shifts/<str:id>/", UpdateAndDeleteShiftView.as_view()),
]

