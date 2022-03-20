from django.shortcuts import render
import requests 
baseApiUrl='http://127.0.0.1:8000/api/'
# Create your views here.
def candidate_login(request):
    response =requests.get(baseApiUrl+'candidate/')
    return render(request, 'frontend/candidate/test.html',{'response':response.json()})