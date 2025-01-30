from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from django.utils import timezone
from django.contrib import messages

from ..models import Diary
from ..forms import DiaryForm

## CRUD

#Create
@login_required()
def Create(request): 
    if request.user.is_guest == True:
        guest_diary_count = Diary.objects.filter(writer=request.user.profile, is_temp_save=False).count()
        print(guest_diary_count)

        if guest_diary_count > 3:
            messages.info(request, "게스트의 글쓰기는 3개까지 가능해요.", extra_tags='guest_message')
            return redirect("diary:index")
   
        #POST Request
    if request.method == "POST":
        form = DiaryForm(request.POST)

        if form.is_valid():
            diary = form.save(commit=False)
            diary.writer = request.user.profile
            diary.create_at = timezone.now()
            #temp-save
            if 'temp-save' in request.POST:
                diary.is_temp_save = True

            diary.save()
            return redirect('diary:index')
          
    #GET Request
    else:
        form = DiaryForm()
        context = {'form' : form }
        return render(request, 'diary/edit.html', context)


#Update
@login_required()
def Update(request, diary_id):
    diary = get_object_or_404(Diary, pk=diary_id) #content upload

    if request.user == diary.writer.user:
        #POST Request
        if request.method == "POST":
            form = DiaryForm(request.POST, instance=diary)
            
            if form.is_valid():
                diary = form.save(commit=False)
                #temp-save
                if 'temp-save' in request.POST:
                    diary.is_temp_save = True
                    diary.save()
                    return redirect('diary:index')
                
                if diary.is_temp_save == True:
                    diary.is_temp_save = False
                    diary.create_at = timezone.now()

                diary.save()
                return redirect('diary:detail', diary_id=diary.pk)
            
            else:
                return redirect('diary:index')
        
        #GET Request
        else:
            form = DiaryForm(instance=diary)
            return render(request, 'diary/edit.html', {'form' : form}) 
        
    else:
        return redirect('diary:index')


#Delete
@login_required()
def Delete(request, diary_id):
    diary = get_object_or_404(Diary, pk=diary_id)

    # 사용자 본인 확인
    if request.user == diary.writer.user: 
        diary.delete()
        return redirect('diary:index')
    
    else:
        return redirect('diary:index')