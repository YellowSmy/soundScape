from django import forms
from .models import Diary, Comment

## Main Content Form
class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ['title', 'content']
        exclude = ['writer']
    

## Comment Form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post', 'writer']

