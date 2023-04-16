from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
GENDER_CHOICES = (
    ('male', '男'),
    ('female', '女')
)


class BaseMode(models.Model):
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        abstract = True


class UserInfo(AbstractUser):
    nickname = models.CharField(max_length=50, verbose_name='昵称', default='')
    birthday = models.DateField(verbose_name='生日', null=True, blank=True)
    gender = models.CharField(verbose_name='性别', choices=GENDER_CHOICES, max_length=6)
    address = models.CharField(max_length=100, verbose_name='地址', default='')
    phone = models.CharField(max_length=11, verbose_name='电话', unique=True)
    avatar = models.ImageField(upload_to='avatar/%Y%m%d/', default='avatar/default.jpg', blank=True, verbose_name='头像')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.nickname:
            return self.nickname
        else:
            return self.username
