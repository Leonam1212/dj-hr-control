from django.urls import path
from work_days.views import MakeCheckInView, WorkDayView, WorkDayByIdView

urlpatterns = [
    path('work_days/', WorkDayView.as_view()),
    path('work_days/<str:id>/', WorkDayByIdView.as_view()),
    path('checkin/<str:personal_code>', MakeCheckInView.as_view())
]