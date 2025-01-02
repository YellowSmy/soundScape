from django.shortcuts import render, get_object_or_404, redirect

from.models import Diary
from .forms import DiaryForm


## Basic Page

def Index(request):
    posts = Diary.objects.all()
    return render(request, 'index.html', {'posts':posts})
 

def Detail(request, diary_id):
    post = get_object_or_404(Diary, pk=diary_id)
    print(post)
    return render(request, 'detail.html', {'post':post})


## CRUD

#Create
def New(request): 
    return render(request, 'edit.html', {'submitType': "발행"})

def Create(request): 
    #POST Request
    if request.method == "POST":
        form = DiaryForm(request.POST)
        
        if form.is_valid():
            diary = form.save(commit=False)
            diary.save()
            return redirect('diary:index')
        
        else:
           return redirect('diary:index')
    
    #GET Request
    else:
        form = DiaryForm()
        return render(request, 'edit.html', {'form' : form, 'submitType': "발행"})


#Update
def Edit(request):
    return render(request, 'edit.html', {'submitType': "수정"})

def Update(request, diary_id):
    diary = get_object_or_404(Diary, pk=diary_id) #content upload

    #POST Request
    if request.method == "POST":
        form = DiaryForm(request.POST, instance=diary)
        
        if form.is_valid():
            diary = form.save(commit=False)
            diary.save()
            return redirect('diary:detail', diary_id=diary.pk)
        
        else:
           return redirect('diary:index')
    
    #GET Request
    else:
        form = DiaryForm(instance=diary)
        return render(request, 'edit.html', {'form' : form, 'submitType': "수정"}) 


#Delete
def Delete(request, diary_id):
    diary = get_object_or_404(Diary, pk=diary_id)
    diary.delete()

    return redirect('diary:index')