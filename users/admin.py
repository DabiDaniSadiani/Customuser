from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm

from .models import CustomUser


class CustomAdminUser(UserAdmin):
    form =  CustomUserChangeForm
    add_form =  CustomUserCreationForm
    model = CustomUser
    list_display = ['email', 'username', 'age']


admin.site.register(CustomUser, CustomAdminUser)
