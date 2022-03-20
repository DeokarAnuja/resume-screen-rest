from django.urls import path

from . import views

urlpatterns = [

    #recruiter
    path('recruiter/', views.RecruiterList.as_view()),

    # path('customer/', CustomerList.as_view()),
    # path('customer/<int:pk>/', CustomerDetail.as_view()),
    # path('customer-login/', user_login),


    # candidate
    # path('instructor/', InstructorList.as_view()),
    # path('instructor/<int:instructor_id>/', InstructorDetail.as_view()),
    # path('instructor-login/', instructor_login),
    # path('plan-category/', PlanCategoryList.as_view()),
    # path('instructor-plan/<int:instructor_id>',InstructorPlanList.as_view()),

    # Job vacancy
    # path('plan/', PlanList.as_view())


]