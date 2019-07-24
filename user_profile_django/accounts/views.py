from django.db import transaction
from django.contrib import messages
from django.contrib.auth import (authenticate, login, logout,
                                 update_session_auth_hash)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

from . import models
from . import forms


def sign_in(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            if form.user_cache is not None:
                user = form.user_cache
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(
                        reverse('accounts:profile'))
                else:
                    messages.error(
                        request, "That user account has been disabled.")
            else:
                messages.error(
                    request, "Username or password is incorrect.")
    return render(request, 'accounts/sign_in.html', {'form': form})


def sign_up(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            login(request, user)
            messages.success(
                request,
                "You're now a user! You've been signed in, too."
            )
            return HttpResponseRedirect(
                reverse('accounts:profile'))
    return render(request, 'accounts/sign_up.html', {'form': form})


def sign_out(request):
    logout(request)
    messages.success(request, "You've been signed out. Come back soon!")
    return HttpResponseRedirect(reverse('home'))


@login_required
@transaction.atomic
def profile_edit(request):
    if request.method == 'POST':
        profile_form = forms.ProfileForm(
            request.POST, request.FILES,instance=request.user.profile
        )
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request,'Profile was successfully updated!')
            return redirect('accounts:profile')
    else:
        profile_form = forms.ProfileForm(instance=request.user.profile)
    return render(request, 'accounts/profile_edit.html', {
        'profile_form': profile_form})


@login_required
def profile(request):
    if request.method == 'GET':
        user = request.user
        profile = request.user.profile
        return render(request, 'accounts/profile.html', {'user': user,
                                                        'profile': profile
                                                        })


@login_required
def change_pass(request):
    if request.method == 'POST':
        form = forms.ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            # Line above is important to keep session logged
            messages.success(request, 'Password successfully modified!!!')
            return redirect('accounts:profile')
    else:
        form = forms.ChangePasswordForm(request.user)
    return render(
                 request, 'accounts/change_password.html', {'form': form})
