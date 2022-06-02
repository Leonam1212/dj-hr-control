from django.urls import path

from .views import CandidateView, UpdateDestroyCandidateView

urlpatterns = [  # (4)
    path("candidates/", CandidateView.as_view()),
    path("candidates/<str:id>/", UpdateDestroyCandidateView.as_view()),
]
