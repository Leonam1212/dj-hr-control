from django.urls import path

from work_days.views import (GetWorkDaysByPersonalCode, MakeCheckInView,
                             WorkDayByIdView, WorkDayView)

urlpatterns = [
    path('work_days/', WorkDayView.as_view()),
    path('work_days/<str:id>/', WorkDayByIdView.as_view()),
    path('checkin/<str:personal_code>/', MakeCheckInView.as_view()),
    path('checkin/<str:personal_code>/list/', GetWorkDaysByPersonalCode.as_view())
]