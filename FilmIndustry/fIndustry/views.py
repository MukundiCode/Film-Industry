from django.shortcuts import render, redirect
from fIndustry.regForm import personForm, talentForm, bankForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from fIndustry.models import person

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print("It is post")
        if form.is_valid():
            print("Form is valid")
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
        print(request.POST)
        form = personForm(request.POST)
        print('checking validity...')
        if form.is_valid():
            print("It is valid")
            form.save()
        person_id = 2
        return redirect('talentInfo',person_id)
    else:
        return render(request,'personalInfo.html',{})

def talentInfo(request,person_id):
    if request.method == "POST":
        #person_obj = person.objects.get(pk = person_id)
        form = talentForm(request.POST)
        print(form)
        print('checking validity...')
        if form.is_valid():
            print("It is valid")
            form.save()
        return redirect('talentBank')
    else:
        return render(request,'talentInfo.html',{}) 

def talentBank(request):
    if request.method == "POST":
        print(request.POST)
        form = bankForm(request.POST)
        print('checking validity...')
        if form.is_valid():
            print("It is valid")
            form.save()
        return redirect('personalInfo')
    else:
        return render(request,'talentBank.html',{})
