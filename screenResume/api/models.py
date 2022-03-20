from django.db import models

# Create your models here.
class Recruiter(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    phone = models.IntegerField()
    company_name=models.CharField(max_length=100)
    company_address=models.TextField()
    