from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.users.models import UserInfo


# Register your models here.

class UserInfoAdmin(admin.ModelAdmin):
    pass


# admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(UserInfo, UserAdmin)
