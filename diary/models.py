from django.db import models
from accounts.models import Member


## 게시물 작성
class Diary(models.Model):
    #Content
    title = models.CharField(max_length=200)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

    #사용자 정보
    writer = models.ForeignKey(Member, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

## 댓글