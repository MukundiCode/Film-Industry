from fIndustry import views
from django.urls import path

urlpatterns = [
    path('',views.personalInfo,name ='personalInfo'),
    path('/personalInfo',views.talentInfo,name = 'talentInfo'),
    path('/talentInfo',views.talentBank,name = 'talentBank'),
    path('register',views.register, name = 'register')
]
