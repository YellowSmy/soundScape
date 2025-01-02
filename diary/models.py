from django.db import models

# Create your models here.

#음악 일기 Base
class Diary(models.Model):
    #제목, 내용, 일시
    title = models.CharField(max_length=200)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

    #댓글, 좋아요


    #Return
    def __str__(self):
        return self.title