from django.shortcuts import render, redirect
from fIndustry.regForm import personForm, talentForm, bankForm, jobForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from fIndustry.models import person, talent, bankDetails, CHITNumber
from django.db.models import Q
#Tinashe Mukundi Chitamba
#This script has the methods for the different views in the application.
#It defines what the server does when each view is called, and which html page is
#rendered. If there are any calculations needed, the method also defines that. 
#Methods also process forms
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password = password)
            login(request, user)
            return redirect('personalInfo')
    form = UserCreationForm()
    context = {'form': form}
    return render(request,'registration/register.html',context)

def personalInfo(request):
    if request.method == "POST":
        form = personForm(request.POST)
        if form.is_valid():
            form.save()
        thisUser = request.user
        thisPerson = person.objects.get(user__exact = thisUser)
        return redirect('talentInfo',thisPerson.id)
    else:
        currentUser = request.user
        currentUserID = currentUser.id
        return render(request,'personalInfo.html',{'currentUserID': currentUserID})

def talentInfo(request,person_id):
    if request.method == "POST":
        form = talentForm(request.POST)
        print('checking validity')
        if form.is_valid():
            print('it is valid')
            form.save()
        else:
            print(form.errors)
        thisUser = request.user
        thisPerson = person.objects.get(user__exact = thisUser)
        return redirect('talentBank',thisPerson.id)
    else:
        personID = person_id
        chitnumber = CHITNumber.objects.get(pk = 1)
        setattr(chitnumber, 'CHITNo',(chitnumber.CHITNo+1))
        chitnumber.save()
        cn = str(chitnumber.CHITNo)
        return render(request,'talentInfo.html',{'personID':personID,'CHIT':cn}) 

def talentBank(request,person_id):
    if request.method == "POST":
        form = bankForm(request.POST)
        print(form)
        if form.is_valid():
            print("It is valid")
            form.save()
        return redirect('profile')
    else:
        personID = person_id
        thisUser = request.user
        thisPerson = person.objects.get(user__exact = thisUser)
        thisTalent = talent.objects.get(person__exact = thisPerson)
        return render(request,'talentBank.html',{'personID':personID, 'CHIT':thisTalent.CHITNumber})

def profile(request):
    thisUser = request.user
    thisPerson = person.objects.get(user__exact = thisUser)
    thisTalent = talent.objects.get(person__exact = thisPerson)
    thisBank = bankDetails.objects.get(person__exact = thisPerson)
    context = {'name':thisPerson.firstName,'surname':thisPerson.surname,
                'email':thisPerson.email,'number':thisPerson.phoneNumber,
                'address':thisTalent.address,'CHIT':thisTalent.CHITNumber,
                'race':thisTalent.race,'gender':thisTalent.gender,
                'bankName':thisBank.bankName,'accountNumber':thisBank.accountNumber,
                'branch':thisBank.branchCode}
    return render(request,'profile.html',context)

def landingPage(request):
    return render (request, 'landingPage.html')

def createJob(request):
    if request.method == "POST":
        form = jobForm(request.POST)
        if form.is_valid():
            print('Job created')
            form.save()
        return redirect('createJob')
    else:
        currentUser = request.user
        currentUserID = currentUser.id
        return render(request,'createJob.html')

def adminDashboard(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        print(query)
        personList = person.objects.filter(
            Q(firstName__icontains=query) | Q(surname__icontains=query)
        )
        return render(request,'adminDashboard.html',{'personList':personList})
        
    personList = person.objects.all()
    return render(request, 'adminDashboard.html',{'personList':personList})