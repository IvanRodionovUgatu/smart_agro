from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from core import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'fullname')


# @admin.register(models.Field)
# class FieldAdmin(admin.ModelAdmin):
#     list_display = ('name', 'location', 'area')
