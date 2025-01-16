from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from ..models import Diary
from ..forms import CommentForm

## Base Function

def Index(request):
    posts = Diary.objects.all()
    return render(request, 'diary/index.html', {'posts':posts})
 

def Detail(request, diary_id):
    #post
    post = get_object_or_404(Diary, pk=diary_id)
    
    #comment
    comment_form = CommentForm() # 댓글작성 Form 추가
    comments = post.comment_set.all()

    context = {
        'post' : post,
        'comments' : comments,
        'comment_form': comment_form
    }

    return render(request, 'diary/detail.html', context)
