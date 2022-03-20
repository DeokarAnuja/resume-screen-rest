from django.contrib import admin
from .models import Recruiter

#Customer details to show in admin panel
class RecruiterAdmin(admin.ModelAdmin):
    fields=['id','name','email','phone','company_name','company_address']


admin.site.register(Recruiter,RecruiterAdmin)
