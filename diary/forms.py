from django import forms
from .models import Diary, Comment

## Main Content Form
class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ['title', 'content','video_id', 'thumbnail_url']
        exclude = ['writer']

        widgets = {
            "video_id": forms.HiddenInput(),
            "thumbnail_url": forms.HiddenInput()
        }


## Comment Form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post', 'writer', 'parent']

