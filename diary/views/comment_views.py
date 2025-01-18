from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from django.utils import timezone

from ..models import Comment, Diary
from ..forms import CommentForm

## COMMENT

# Create
@login_required()
@require_POST
def Create_comment(request, diary_id, parent_id=None):
    post = get_object_or_404(Diary, pk=diary_id)
    comment_form = CommentForm(request.POST)

    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.post = post
        comment.writer = request.user

        # 대댓글 기능
        if parent_id: #대댓글
            parent_comment= get_object_or_404(Comment, id=parent_id)
            comment.parent = parent_comment
        
        else: #일반 댓글 처리
            comment.parent = None

        comment.save()
        return redirect('diary:detail', diary_id)
    
  
# Update
## 차후 AJAX 처리할 것.
@login_required()
def Update_comment(request, diary_id, comment_id, parent_id=None):
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.user == comment.writer:
        if request.method == 'POST':
            comment_form = CommentForm(request.POST, instance=comment)

            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.modify_date = timezone.now()

                comment.save()
                return redirect('diary:detail', diary_id)
        else: 
            comment_form = CommentForm(instance=comment)
            return render(request, 'diary/editComment.html', {'comment':comment, 'form': comment_form}) 


# Delete
@login_required()
@require_POST
def Delete_comment(request, diary_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    # 사용자 본인 확인
    if request.user == comment.writer: 
        comment.delete()
        return redirect('diary:detail', diary_id)