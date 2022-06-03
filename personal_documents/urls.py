from django.urls import path

from personal_documents.views import (CreatePersonalDocumentsView,
                                      ListPersonalDocumentsView,
                                      PersonalDocumentByIdView)

urlpatterns = [
    path(
        "personal_documents/create/<str:employee_id>/", CreatePersonalDocumentsView.as_view()
    ),
    path("personal_documents/", ListPersonalDocumentsView.as_view()),
    path("personal_documents/<str:id>/", PersonalDocumentByIdView.as_view()),
]
