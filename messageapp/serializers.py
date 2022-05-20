from rest_framework import serializers
from .models import Msg
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class MsgSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(source="created_by_usr", many=False, read_only=True)
    class Meta:
        model = Msg
        fields = ['id', 'message', 'created_at', 'updated_at', 'created_by_usr', 'created_by']
        extra_kwargs = {
            'created_by_usr': {'write_only': True},
        }
        
