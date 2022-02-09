from unittest.util import _MAX_LENGTH
from django.contrib.auth.password_validation import validate_password
from django.db.transaction import atomic
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import NewUser

class NewUserCreateSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        label = _("Password Repeat"),
        max_length = 128,
        write_only = True,
        style = {"input_type":"password"}
    )
    password = serializers.CharField(
        label = _("Password"),
        max_length = 128,
        write_only = True,
        validators = [validate_password],
        style = {"input_type":"password"}
    )
    class Meta:
        model = NewUser
        fields = ("email","user_name","first_name","password","password2")
        
    def validate(self,attrs):
        attrs = super().validate(attrs)
        password = attrs["password"]
        password2 = attrs["password2"]
        if password != password2:
            raise ValidationError('Must be same')
        return attrs

    def create(self, validated_data):
        validated_data.pop("password2",None)
        instance = NewUser.objects.create_user(**validated_data)
        return instance