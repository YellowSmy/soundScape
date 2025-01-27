from django.db import models
from accounts.models import Profile


## 게시물 작성
class Diary(models.Model):
    #Content
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True)
    create_at = models.DateTimeField(auto_now_add=False)
    is_temp_save = models.BooleanField(default=False)

    #music info
    video_id = models.CharField(max_length=50, null=True)
    thumbnail_url = models.URLField(default="")
    music_title = models.CharField(max_length=50, default="알 수 없음")
    artist = models.CharField(max_length=30, default="알 수 없음")

    #사용자 정보
    writer = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="diaries")
    like_users = models.ManyToManyField(Profile, related_name="like_diary", blank=True) 
 
    def __str__(self):
        return self.title
    

## 댓글
class Comment(models.Model):
    #구분자
    post = models.ForeignKey(Diary, on_delete=models.CASCADE, related_name="comments")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="replies") #대댓글 구분
    
    #Content
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=False)
    writer = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="comments", blank=True)

    def __str__(self):
        return self.content