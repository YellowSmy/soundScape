from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from ..models import Comment, Diary
from ..forms import ComentForm

## COMMENT

# Create
@login_required()
@require_POST
def Create_comment(request, diary_id):
    post = get_object_or_404(Diary, pk=diary_id)
    comment_form = ComentForm(request.POST)

    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.post = post
        comment.writer = request.user

        comment.save()
        return redirect('diary:detail', diary_id=post.pk)
    
  
# Delete
@login_required()
@require_POST
def Delete_comment(request, diary_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    # 사용자 본인 확인
    if request.user == comment.writer: 
        comment.delete()
        return redirect('diary:detail', pk=diary_id)
    
    else:
        return redirect('diary:detail', pk=diary_id)
    