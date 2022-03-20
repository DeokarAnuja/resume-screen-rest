from django.urls import path

from . import views

urlpatterns = [

    #recruiter
    path('recruiter/', views.RecruiterList.as_view()),
    path('recruiter/<int:pk>/', views.RecruiterDetail.as_view()),

    # candidate
    path('candidate/', views.CandidateList.as_view()),
    path('candidate/<int:pk>/', views.CandidateDetail.as_view()),
    path('candidate-profile/', views.CandidateProfileList.as_view()),
    path('candidate-profile/<int:pk>/', views.CandidateProfileDetail.as_view()),

    # Job vacancy
    path('vacancy/', views.VacancyList.as_view())


]