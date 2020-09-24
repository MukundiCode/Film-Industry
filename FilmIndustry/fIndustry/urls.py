from fIndustry import views
from django.urls import path

urlpatterns = [
    path('',views.personalInfo,name ='personalInfo'),
    path('/personalInfo',views.talentInfo,name = 'talentInfo'),
    path('/talentInfo/<person_id>',views.talentInfo,name = 'talentInfo'),
    path('/talentBank/<person_id>',views.talentBank,name = 'talentBank'),
    path('register',views.register, name = 'register')
]
