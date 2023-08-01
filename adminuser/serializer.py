from rest_framework import serializers
from adminuser.models import Category, Ingredient,Recipe,Recipe,Recipe_Ingredient



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id","name","categoryImage"]




class IngredientSerializer(serializers.ModelSerializer):
    image2 = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Ingredient
        fields = ["id","name","image","image2"]
    def get_image2(self, obj):
        if  str(obj.image).startswith("http"):
            return str(obj.image)
        else:
            return None
        



class RecipeListSerializer(serializers.ModelSerializer):
    category_name=serializers.CharField(source='category.name', read_only=True)
    class Meta:
        model = Recipe
        fields = ["id","name","thumbnail","category_name"]




class Recipe_IngredientSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name', read_only=True)

    ingredients = serializers.SerializerMethodField()
    class Meta:
        model = Recipe
        fields = ["id","name","thumbnail","calculated_rating","is_active","category","description","youtube_link","ingredients"]

    def get_ingredients(self,obj):
        objects=Recipe_Ingredient.objects.filter(recipe = obj)
        data={}
        for items in objects:
            data[items.ingredient.name]=items.quantity
        return data



