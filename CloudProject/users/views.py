from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, userUpdateForm, ProfileUpdateForm
import logging
import boto3
from botocore.exceptions import ClientError
from django.core.files.storage import default_storage


def register(request):
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}!')
            messages.success(request, f'Please log in using your new username and password.')

            return redirect('App-Login')
    else:
        #form = UserCreationForm()
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form, 'title': 'Register'})


def create_bucket(username):
    pass


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = userUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance = \
        request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Update successful!')
            return redirect('User-Profile')
    else:
        u_form = userUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context, {'title': 'Profile'})


def create_bucket(bucket_name):
    pass
