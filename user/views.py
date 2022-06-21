from django.shortcuts import redirect, render
from user.forms import NewUserForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import DetailView

# Create your views here.

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request,"Registration successful")
            return redirect('home:home')
        messages.error(request,"Unsucessful registration")
        

    form = NewUserForm()


    context = {
        'form':form
    }
    return render(request,'user/register-form.html',context)

def UserProfile(request):
    return render(request,'user/user_profile.html')
