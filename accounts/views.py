from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from accounts.forms import SignUpForm

## 회원가입
def Signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            
            return redirect('diary:index')
        
    else:
        form = SignUpForm()
        
    return render(request, 'signup.html', {'form' : form})
