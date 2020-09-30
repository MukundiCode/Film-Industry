from fIndustry import views
from django.urls import path

urlpatterns = [
    path('profile',views.profile,name ='profile'),
    path('/personalInfo',views.personalInfo,name = 'personalInfo'),
    path('/talentInfo/<person_id>',views.talentInfo,name = 'talentInfo'),
    path('/talentBank/<person_id>',views.talentBank,name = 'talentBank'),
    path('register',views.register, name = 'register'),
    path('landingPage',views.landingPage, name = 'landingPage'),
    path('createJob', views.createJob, name ='createJob')
]
