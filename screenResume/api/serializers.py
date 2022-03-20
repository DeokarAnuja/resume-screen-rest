from rest_framework import serializers
from .models import Recruiter

#Serializer for Recruiter
class RecruiterSerializer(serializers.ModelSerializer):
     class Meta:
        model=Recruiter
        fields=['id','name','email','password','phone','company_name','company_address']