from pyexpat import model
from django.db import models
from django.utils import timezone
import os
from uuid import uuid4
    
# recruiter model
class Recruiter(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    phone = models.IntegerField()
    company_name=models.CharField(max_length=100)
    company_address=models.TextField()

# candidate model
class Candidate(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    phone = models.IntegerField()
    is_first=models.BooleanField(default=False)

# model to maintain resume data as profile
class CandidateProfile(models.Model):
    candidate_id=models.ForeignKey(Candidate,on_delete=models.CASCADE)
    resume_pdf = models.FileField(upload_to='uploaded_resume/')
    github_profile = models.URLField(null=True, blank=True)
    other_skills=models.TextField(null=True,blank=True)

class Vacancy(models.Model):
    recruiter=models.ForeignKey(Recruiter,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    skills= models.TextField()
    candidates_apply=models.TextField(blank=True)


