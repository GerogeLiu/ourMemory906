from django.contrib import admin
from .models import UserProfile

# 在管理页面注册，管理新增用户信息
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth', 'phone')
    list_filter = ('phone', )
