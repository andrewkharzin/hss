from rest_framework import serializers
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_active', 'start_date', ]
        read_only_field = ['is_active', 'start_date']
