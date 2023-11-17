from rest_framework import serializers
from register.models import RegisterModel

class RegisterSerializer(serializers.ModelSerializer):
    class Meta :
        model = RegisterModel
        fields = (
            'name',
            'pic',
            'email',
            'pswd'
        )