from django import forms
from .models import Diary, Comment

## Main Content Form
class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ['title', 'content',
                  'video_id', 'thumbnail_url', 'music_title', 'artist', 'theme'] #hidden method
        exclude = ['writer']

        widgets = {
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

