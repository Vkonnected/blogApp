from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    if(request.method=='POST'):
        #form=UserCreationForm(request.POST)
        form=UserRegisterForm(request.POST)
        if(form.is_valid()):
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account created successfully for {username}')
            #return redirect('blog-home')
            return redirect('login')
    else:
        #form=UserCreationForm()
        form=UserRegisterForm()
    return render(request,"users/register.html",{'form':form})

@login_required
def profile(request):
    if (request.method == 'POST'):
        uform = UserUpdateForm(request.POST, instance=request.user)
        pform = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if (uform.is_valid() and pform.is_valid()):
            uform.save()
            pform.save()
            messages.success(request, f'Profile Updated')
            return redirect('profile')
    else:
        uform=UserUpdateForm(instance=request.user)
        pform=ProfileUpdateForm(instance=request.user.userprofile)
    context={
        'pform':pform,
        'uform':uform
    }
    return render(request,"users/profile.html",context)

