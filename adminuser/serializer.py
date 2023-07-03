from rest_framework import serializers
from adminuser.models import Category, Ingredient,Recipe,RecipeDescription,RecipeDescription_Ingredient

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
        fields = ["id","name","thumbnail","calculated_rating","category","category_name"]






class RecipeIngredientSerializer(serializers.ModelSerializer):
    ingredient_name=serializers.CharField(source='ingredient.name', read_only=True)
    # recipeDescription=serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = RecipeDescription_Ingredient
        fields = ["id","ingredient_name","recipeDescription","quantity"]




class RecipeSerializer(serializers.ModelSerializer):
    ingredient_list=RecipeIngredientSerializer()
    category_name=serializers.CharField(source='category.name', read_only=True)
    # description=serializers.CharField(source='recipeRecipeDescription.description', read_only=True)
    class Meta:
        model = Recipe
        fields = ["id","name","thumbnail","calculated_rating","category","category_name","ingredient_list"]


