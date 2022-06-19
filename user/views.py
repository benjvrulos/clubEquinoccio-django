from django.shortcuts import redirect, render
from user.forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == "POST":
        messages.success(request,"METHOD_POST")
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
