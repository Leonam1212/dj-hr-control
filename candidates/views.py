from rest_framework import generics
from .models import Candidate
from .serializers import CandidateSerializer


class CandidateView(generics.ListCreateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer


class UpdateDestroyCandidateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    lookup_field = "id"
