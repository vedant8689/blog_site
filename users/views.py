from django.shortcuts import render, redirect
#message 
from django.contrib import messages
#import Register form created for email add
from .forms import UserRegistrationForm
#login required decorators
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib.auth import logout
#import forms
from .forms import UserUpdateForm, ProfileUpdateForm

#create register view
def register(request):
    if request.method == 'POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {user} !')
            return redirect ('login')

    else:
        form=UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form, 'title': 'Register User'})
# @login_required

@login_required
def profile(request):
    if request.method == 'POST':
        u_form=UserUpdateForm(request.POST, instance=request.user)
        p_form=ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Profile Updated Successfully!!')
            return redirect('profile')
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'title': 'Profile Page'
    }
    return render(request, 'users/profile.html', context)

@login_required
def custom_logout(request):
    logout(request)
    return render(request, 'users/logout.html')
