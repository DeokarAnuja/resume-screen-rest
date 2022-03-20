from django.shortcuts import render
from rest_framework import generics
from .models import Recruiter
from .serializers import RecruiterSerializer
# recruiter list
class RecruiterList(generics.ListCreateAPIView):
    queryset=Recruiter.objects.all().order_by('id')
    serializer_class=RecruiterSerializer
