from django.contrib import admin
from firstapp.models import User


class UserAdmin(admin.ModelAdmin):
    """Диалоги"""
    list_display = ("full_name",'telefon')

admin.site.register(User, UserAdmin)
