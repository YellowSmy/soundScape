from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required



from ..models import Diary, Comment
from ..forms import CommentForm

from accounts.models import Profile
from utils.context_processors import user_profile

## Base Function

def Index(request):
    posts = Diary.objects.all()
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

   