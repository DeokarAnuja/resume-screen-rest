from django.contrib import admin
from .models import Recruiter,Candidate,CandidateProfile

#Customer details to show in admin panel
@admin.register(Recruiter)
class RecruiterAdmin(admin.ModelAdmin):
    fields=['id','name','email','phone','company_name','company_address']

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    fields=['id','name','email','phone']

@admin.register(CandidateProfile)
class CandidateProfileAdmin(admin.ModelAdmin):
    fields=['id','candidate_id','resume_pdf','github_profile','other_skills']


