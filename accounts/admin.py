from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin 

from .forms import AccountUserChangeForm, AccountUserCreationForm
from .models import AccountUser

class AccountUserAdmin(UserAdmin):    
    add_form = AccountUserCreationForm
    form = AccountUserChangeForm
    model = AccountUser
    list_display = ['email']
    
admin.site.register(AccountUser, AccountUserAdmin)
