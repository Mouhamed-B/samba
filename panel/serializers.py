from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework import serializers
from  .models import Profile, Enterprise
from django.contrib.auth.models import User



class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['password']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name','last_name','email', 'username']



class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name','last_name','email', 'username','password']
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            user = User.objects.create_user(   
                validated_data['username'],
                validated_data['email'],
                validated_data['password'],
                validated_data['first_name'],
                validated_data['last_name']              
            )           
            return user



class LoginSerializer(serializers.Serializer):
  username = serializers.CharField()
  password = serializers.CharField()

  def validate(self, data):
    user = authenticate(**data)
    if user and user.is_active:
       return user
    raise serializers.ValidationError("Identifiants Incorrects")


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        #exclude = ('password', 'is_active', 'is_staff', 'groups', 'user_permissions')
        fields = ('user','phone','civility','avatar','address')

class EnterpriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enterprise
        exclude = ('created', 'updated')

