from django.shortcuts import render, redirect
from fIndustry.regForm import personForm

# Create your views here.
def login(request):
    if request.method == "POST":
        print(request.POST)
        form = personForm(request.POST)
        print('checking validity...')
        if form.is_valid():
            print("It is valid")
            form.save()
        return redirect('login')
    else:
        return render(request,'login.html',{})
