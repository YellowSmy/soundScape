from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from accounts.forms import SignUpForm

# Create your views here.
def Signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('diary:index')
        
    else:
        form = SignUpForm()
        
    return render(request, 'signup.html', {'form' : form})