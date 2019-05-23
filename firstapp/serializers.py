from rest_framework import serializers

from firstapp.models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериализация пользователя"""
    class Meta:
        model = User
        fields = ("id", "first_name",'patronymic','full_name','telefon')

