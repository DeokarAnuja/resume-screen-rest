from django.shortcuts import render
from rest_framework import generics
from .models import Recruiter,Candidate,CandidateProfile,Vacancy
from .serializers import RecruiterSerializer,CandidateSerializer,CandidateProfileSerializer,VacancySerializer

# recruiter list
class RecruiterList(generics.ListCreateAPIView):
    queryset=Recruiter.objects.all().order_by('id')
    serializer_class=RecruiterSerializer

# recruiter detail
class RecruiterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Recruiter.objects.all()
    serializer_class=RecruiterSerializer


# candidate list
class CandidateList(generics.ListCreateAPIView):
    queryset=Candidate.objects.all().order_by('id')
    serializer_class=CandidateSerializer

# candidate detail
class CandidateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Candidate.objects.all()
    serializer_class=CandidateSerializer

# candidate profile list
class CandidateProfileList(generics.ListCreateAPIView):
    queryset=CandidateProfile.objects.all().order_by('id')
    serializer_class=CandidateProfileSerializer

# candidate profile detail
class CandidateProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=CandidateProfile.objects.all()
    serializer_class=CandidateProfileSerializer

class VacancyList(generics.ListCreateAPIView):
    queryset=Vacancy.objects.all()
    serializer_class=VacancySerializer
