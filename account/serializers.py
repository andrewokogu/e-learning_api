from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['id','first_name','last_name','username','password','email','is_active','date_joined']
        
        
class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=500)
    new_password = serializers.CharField(max_length=500)
    re_password = serializers.CharField(max_length=500)
    
    
    # def password_validate(self):
    #     if self.initial_data['new_password'] != self.initial_data['re_password']:
    #         raise serializers.ValidationError("Please enter matching passwords")
    #     return True
    
    def validate_new_password(self, value):
        if value != self.initial_data['re_password']:
            raise serializers.ValidationError("Please enter matching passwords")
        return value

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=500)
    password = serializers.CharField(max_length=500)
    # email = serializers.CharField(max_length=500)
    