from django.shortcuts import render,redirect
from .forms import ExtendedUserCreationForm, LoginForm
from django.template import loader
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from .models import UserProfile
#from django.contrib.auth.decorators import login_required


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
            return redirect('products:list_products')
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
                    return redirect('products:list_products')
                
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