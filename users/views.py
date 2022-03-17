
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Tour account has been created! {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form': form})

@login_required
def profile(reguest):
    if reguest.method == 'POST':
        u_form = UserUpdateForm(reguest.POST,instance=reguest.user)
        p_form = ProfileUpdateForm(reguest.POST,reguest.FILES,instance=reguest.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(reguest, f'Your account has been Updated! !')
            return redirect('profile')
            
    else:
        u_form = UserUpdateForm(instance=reguest.user)
        p_form = ProfileUpdateForm(instance=reguest.user.profile)
        
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(reguest,'users/profile.html',context)