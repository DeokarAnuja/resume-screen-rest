from rest_framework import serializers
from .models import Recruiter,Candidate,CandidateProfile,Vacancy

#Serializer for Recruiter
class RecruiterSerializer(serializers.ModelSerializer):
     class Meta:
        model=Recruiter
        fields=['id','name','email','password','phone','company_name','company_address']

class CandidateSerializer(serializers.ModelSerializer):
     class Meta:
        model=Candidate
        fields=['id','name','email','password','phone']

class CandidateProfileSerializer(serializers.ModelSerializer):
     class Meta:
        model=CandidateProfile
        fields=['id','candidate_id','resume_pdf','github_profile','other_skills']

class VacancySerializer(serializers.ModelSerializer):
     class Meta:
        model=Vacancy
        fields=['id','recruiter','title','description','skills','candidates_apply']