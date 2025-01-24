from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from ..models import Diary
from ..forms import DiaryForm

## CRUD

#Create
@login_required()
def Create(request): 
    #POST Request
    if request.method == "POST":
        form = DiaryForm(request.POST)
        
        if form.is_valid():
            diary = form.save(commit=False)
            diary.writer = request.user.profile
            
            diary.save()
            return redirect('diary:index')
        
    #GET Request
    else:
        form = DiaryForm()
        context = {'form' : form,'submitType': "발행"}
        return render(request, 'diary/edit.html', context)


#Update
def Update(request, diary_id):
    diary = get_object_or_404(Diary, pk=diary_id) #content upload

    if request.user == diary.writer.user:
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
            return render(request, 'diary/edit.html', {'form' : form, 'submitType': "수정"}) 
        
    else:
        return redirect('diary:index')


#Delete
def Delete(request, diary_id):
    diary = get_object_or_404(Diary, pk=diary_id)

    # 사용자 본인 확인
    if request.user.profile == diary.writer: 
        diary.delete()
        return redirect('diary:index')
    
    else:
        return redirect('diary:index')