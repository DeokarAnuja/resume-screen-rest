from django.urls import  path
from . import views
urlpatterns = [
    path('candidate-login/',views.candidate_login,name="candidate-login"),
]