from users.models import User, UserProfile
from rest_framework import serializers
from adminuser.models import Recipe



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




class RecipeListSerializer(serializers.ModelSerializer):
    category_name=serializers.CharField(source='category.name', read_only=True)
    class Meta:
        model = Recipe
        fields = ["id","name","thumbnail","category_name",]
