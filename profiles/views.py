from django.shortcuts import render,redirect
from .forms import ExtendedUserCreationForm, LoginForm
from django.template import loader
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import UserProfile
def user_register(request):
    template = loader.get_template('profiles/user_register.html')
    if request.method == 'POST':
        form =ExtendedUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1') 
            user = authenticate(username=username,password=password)
            login(request,user)
            
             # Create a UserProfile for the newly registered user
            UserProfile.objects.create(
                user=user,
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                phone_number=form.cleaned_data['phone_number']
            )
            #return redirect('home')
            return HttpResponse('Registered and Logged in')
    else:
        form = ExtendedUserCreationForm()
    
    context = {'form':form,}
    return HttpResponse(template.render(context,request))

def log_in(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    #return redirect ('home')
                    return HttpResponse('Logged In')
                
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
        else:
            form = LoginForm()
    form = LoginForm()
    template = loader.get_template('profiles/login.html')
    context = {'form':form}
    return HttpResponse(template.render(context,request))