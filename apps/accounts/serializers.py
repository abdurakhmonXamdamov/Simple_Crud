from rest_framework import serializers 
from .models import User 

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User 
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password', 'phone', 'photo', 'bio', 'gender', 'birth_date']



        