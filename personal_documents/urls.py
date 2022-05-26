from django.urls import path
from personal_documents.views import PersonalDocumentsView, PersonalDocumentByIdView

urlpatterns = [
    path('personal_documents/', PersonalDocumentsView.as_view()),
    path('personal_documents/<str:id>/', PersonalDocumentByIdView.as_view()),
]