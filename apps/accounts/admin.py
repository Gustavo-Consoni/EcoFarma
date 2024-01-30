from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from apps.accounts.forms import UserChangeForm, UserCreationForm
from apps.accounts import models


@admin.register(models.User)
class UsersAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = models.User
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        ('Informações Adicionais', {'fields': ('phone', 'image')}),
    )
