from django import forms
from django.forms import TextInput
from .models import Diary, Comment

## Main Content Form
class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ['title', 'content',
                  'video_id', 'thumbnail_url', 'music_title', 'artist', 'theme'] #hidden method
        exclude = ['writer']

        widgets = {
            'title': TextInput(attrs={
                'class': "form-title",
                'placeholder': '제목',
                'autocomplete' : 'off',
                'autofocus' : True,
                'spellcheck' : False,
            },),

            "video_id": forms.HiddenInput(),
            "thumbnail_url": forms.HiddenInput(),
            "music_title": forms.HiddenInput(),
            "artist": forms.HiddenInput(),
            "theme": forms.HiddenInput(),
        }

class MusicForm(forms.ModelForm):
    model = Diary
    fields = []


## Comment Form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post', 'writer', 'parent']
        widgets = {
            'content': TextInput(attrs={
                'class': "form-control",
                'placeholder': '댓글을 입력하세요...',
                'autocomplete' : 'off'
            },)
        }