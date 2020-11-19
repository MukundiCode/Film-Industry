from fIndustry import views
from django.urls import path

#The urls script has all the urls for the different views for the filming app
#It shows the name of the url path, along with the name of the view associated
#with the url. Some url patterns take in a variable, and this is represented by
#url/<variable>. Every new view should be added here.
urlpatterns = [
    path('profile',views.profile,name ='profile'),
    path('/personalInfo',views.personalInfo,name = 'personalInfo'),
    path('/talentInfo/<person_id>',views.talentInfo,name = 'talentInfo'),
    path('/talentBank/<person_id>',views.talentBank,name = 'talentBank'),
    path('register',views.register, name = 'register'),
    path('landingPage',views.landingPage, name = 'landingPage'),
    path('createJob', views.createJob, name ='createJob'),
    path('adminDashboard', views.adminDashboard,name = 'adminDashboard')
]
