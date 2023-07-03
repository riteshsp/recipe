from users.models import User, UserProfile
from rest_framework import serializers



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model =UserProfile
        fields=['profession'] 


class UserSerializer(serializers.ModelSerializer):
    userprofilee = UserProfileSerializer()

    class Meta:
        model =User
        fields=['first_name','last_name','username','userprofilee','password','is_active']


    def create(self, validated_data):

        profile=validated_data.pop("userprofilee")
        user=User.objects.create(**validated_data)
        UserProfile.objects.create(user = user, **profile)
        return user 

