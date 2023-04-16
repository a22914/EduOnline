from django.db import models

from apps.users.models import BaseMode
from apps.institutions.models import Teacher


# Create your models here.

class Course(BaseMode):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='老师')
    name = models.CharField(max_length=50, verbose_name='课程名')
    desc = models.CharField(max_length=300, verbose_name='课程描述')
    duration = models.IntegerField(default=0, verbose_name='课程时长(分钟数)')
    degree = models.CharField(verbose_name="难度", choices=(("cj", "初级"), ("zj", "中级"), ("gj", "高级")), max_length=2)
    students = models.IntegerField(default=0, verbose_name='学习人数')
    col_nums = models.IntegerField(default=0, verbose_name='收藏人数')
    click_nums = models.IntegerField(default=0, verbose_name="点击数")

    category = models.CharField(default=u"后端开发", max_length=20, verbose_name="课程类别")
    tag = models.CharField(default="", verbose_name="课程标签", max_length=10)
    course_notes = models.CharField(default="", max_length=300, verbose_name="课程须知")
    teacher_tell = models.CharField(default="", max_length=300, verbose_name="老师寄语")

    detail = models.TextField(verbose_name='课程详情')
    image = models.ImageField(upload_to='courses/%Y/%m', verbose_name='封面图', max_length=100)

    class Meta:
        verbose_name = '课程信息'
        verbose_name_plural = verbose_name


class Lesson(BaseMode):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='课程')
    name = models.CharField(max_length=100, verbose_name='章节名')
    duration = models.IntegerField(default=0, verbose_name='章节时长(分钟数)')

    class Meta:
        verbose_name = '章节信息'
        verbose_name_plural = verbose_name


class Video(BaseMode):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='章节')
    name = models.CharField(max_length=100, verbose_name='视频名称')
    url = models.CharField(max_length=200, default='', verbose_name='访问地址')
    duration = models.IntegerField(default=0, verbose_name='视频时长(分钟数)')

    class Meta:
        verbose_name = '视频信息'
        verbose_name_plural = verbose_name


class CourseRes(BaseMode):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='课程')
    name = models.CharField(max_length=100, verbose_name='名称')
    download = models.FileField(upload_to='course/resource/%Y/%m', verbose_name='资源文件', max_length=200)

    class Meta:
        verbose_name = '课程资源'
        verbose_name_plural = verbose_name
