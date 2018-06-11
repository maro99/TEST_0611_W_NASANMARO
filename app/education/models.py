from django.db import models  # 장고 내부의 db페키지의 models라는 모듈.
from django.conf import settings
from django.utils import timezone


class School(models.Model):

    name= models.CharField(max_length=200) # 길이재한 있을때
    description = models.CharField(max_length=1000)  # 길이 제한 없을때., blank

    def __str__(self):
        return self.name


class Student(models.Model):
    school= models.ForeignKey(School, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)  # 길이재한 있을때
    created_at = models.DateTimeField(default=timezone.now)  # 데이트,타임저장에 특화된 필드

    def __str__(self):
        return self.name
