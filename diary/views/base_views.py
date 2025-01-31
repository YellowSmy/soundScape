from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseBadRequest

from ..models import Diary, Comment
from ..forms import CommentForm

## Base Function

def Index(request):
    posts = Diary.objects.filter(is_temp_save=False)
    return render(request, 'diary/index.html', {'posts':posts})

def Detail(request, diary_id):
    post = get_object_or_404(Diary, pk=diary_id) #post
    #comment
    comment_form = CommentForm() # 댓글작성 Form 추가
    comments = Comment.objects.filter(post=post, parent=None).order_by("-created_at")
    context = {
        'post' : post,
        'comments' : comments,
        'comment_form': comment_form
    }

    return render(request, 'diary/detail.html', context)

   
## Like
@login_required()
def Like(request, diary_id):
    diary = get_object_or_404(Diary, pk=diary_id)
    if diary.like_users.filter(user_id=request.user.profile.user_id).exists():
        diary.like_users.remove(request.user.profile)
                                
    else:
        diary.like_users.add(request.user.profile)
    
    return redirect('diary:detail', diary_id)


## Temp-save list
@login_required()
def Temp_save(request):
    diarys = Diary.objects.filter(is_temp_save=True, writer=request.user.profile)
    if diarys.exists():
        html_content = render(request, 'diary/temp_save.html', {'diarys': diarys})
        return JsonResponse({"html": html_content.content.decode('utf-8')})

    else:
        html_content = render(request, 'diary/temp_save.html', {'none': "임시 저장 글이 없습니다"})
        return JsonResponse({"html": html_content.content.decode('utf-8')})
    

## Theme change
def Change_theme(request):
    theme = request.GET.get('theme', '')
    valid_themes = ['basic', 'rock', 'ballad', 'jazz', 'pop']
    
    if theme not in valid_themes:
        return HttpResponseBadRequest("Invalid theme selected")
    
    css_path = f'/static/css/theme/{theme}.css'
    print(css_path, theme)

    return JsonResponse({'css_path': css_path})