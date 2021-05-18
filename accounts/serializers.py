from rest_framework import serializers
from accounts.models import AccountUser

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=AccountUser
        fields=('email', 'username', 'password', 'created_at')