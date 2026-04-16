from rest_framework import serializers 
from .models import User 

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    photo = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = User 
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password', 'phone', 'photo', 'bio', 'gender', 'birth_date']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
            
        if password:
            instance.set_password(password)
            
        instance.save()
        return instance


class RegisterSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(
        write_only=True, 
        min_length=8,
        style={'input_type': 'password'},
        help_text="Password (minimum 8 characters)"
        )
    password_confirm = serializers.CharField(
        write_only=True,
        style={'input_type': 'password'},
        help_text="Confirm password"
    )

    class Meta:
        model = User
        fields = [
                'id', 'username', 'email',
                'first_name', 'last_name',
                'password', 'password_confirm',
                'phone', 'gender'
            ]

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError("Passwords don't match")
        return data
    
    def create(self, validated_data):
        validated_data.pop('password_confirm', None)
        return User.objects.create_user(**validated_data)
