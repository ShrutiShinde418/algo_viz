from django import forms
from django.contrib.auth.forms import UserChangeForm,UserCreationForm 
from .models import AccountUser 
 
class AccountUserCreationForm(UserCreationForm):    
    class Meta:        
        model = AccountUser        
        fields = ('email', ) 

class AccountUserChangeForm(UserChangeForm):    
    class Meta:        
        model = AccountUser        
        fields = UserChangeForm.Meta.fields