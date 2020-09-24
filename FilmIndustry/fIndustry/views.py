from django.shortcuts import render, redirect
from fIndustry.regForm import personForm, talentForm, bankForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from fIndustry.models import person, talent, bankDetails

# Create your views here.
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
        if form.is_valid():
            form.save()
        thisUser = request.user
        thisPerson = person.objects.get(user__exact = thisUser)
        return redirect('talentBank',thisPerson.id)
    else:
        personID = person_id
        return render(request,'talentInfo.html',{'personID':personID}) 

def talentBank(request,person_id):
    if request.method == "POST":
        form = bankForm(request.POST)
        print(form)
        if form.is_valid():
            print("It is valid")
            form.save()
        userID = request.user.id
        return redirect('profile')
    else:
        personID = person_id
        return render(request,'talentBank.html',{'personID':personID})

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