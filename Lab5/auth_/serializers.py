from rest_framework import serializers
from auth_.models import MainUser


class MainUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainUser
        fields = ('id', 'first_name', 'last_name')
