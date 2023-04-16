from django.db import models

from django.contrib.auth import get_user_model

from apps.courses.models import Course
from apps.users.models import BaseMode

UserInfo = get_user_model()


# Create your models here.
class UserConsult(BaseMode):
    name = models.CharField(max_length=20, verbose_name='姓名')
    phone = models.CharField(max_length=11, verbose_name='手机号')
    course_name = models.CharField(max_length=50, verbose_name='课程名称')

    class Meta:
        verbose_name = '用户咨询'
        verbose_name_plural = verbose_name


class CourseComments(BaseMode):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name='用户')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='课程')
    comments = models.CharField(max_length=200, verbose_name='评论')

    class Meta:
        verbose_name = '课程评论'
        verbose_name_plural = verbose_name


class UserCollection(BaseMode):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name='用户')
    col_id = models.IntegerField(default=0, verbose_name='数据ID')
    col_type = models.IntegerField(choices=((1, '课程'), (2, '课程机构'), (3, '老师')), default=1, verbose_name='收藏类型')

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name


class UserMessage(BaseMode):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name='用户')
    message = models.CharField(max_length=500, verbose_name='消息内容')
    is_read = models.BooleanField(default=False, verbose_name='是否已读')

    class Meta:
        verbose_name = '用户消息'
        verbose_name_plural = verbose_name


class UserCourse(BaseMode):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name='用户')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='课程')

    class Meta:
        verbose_name = '用户课程'
        verbose_name_plural = verbose_name
