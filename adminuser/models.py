from django.db import models
from users.models import User



class Ingredient(models.Model):
    name = models.CharField(max_length=255,unique=True)
    image = models.ImageField(upload_to='static/ingredients/')
    id_ingrediant = models.CharField(max_length=255)



class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    categoryImage = models.ImageField(upload_to='static/category/', null=True)
    description = models.TextField(null=True, blank=True)




class Recipe(models.Model):
    name = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='static/thumbnails/')
    idMeal = models.CharField(max_length=255,null=True)
    calculated_rating = models.FloatField(default = 0)
    is_approved = models.BooleanField(default=0)
    user = models.ForeignKey(User, null=True ,blank=True, related_name= 'userRecipe',on_delete=models.PROTECT)
    category = models.ForeignKey(Category, null=True ,blank=True ,related_name= 'categoryRecipe',on_delete=models.PROTECT)



class RecipeDescription(models.Model):
    recipe = models.OneToOneField(Recipe, related_name= 'recipeRecipeDescription',on_delete=models.PROTECT)
    description = models.TextField()
    youtube_link = models.CharField(max_length=255, null=True)
    dateModified =models.DateField(auto_now_add=True)




class Rating(models.Model):
    recipeDescription = models.ForeignKey(RecipeDescription, null=True ,blank=True ,related_name= 'recipeDescriptionRating',on_delete=models.PROTECT)
    rating = models.IntegerField(choices=[(1,1),(2,2),(3,3),(4,4),(5,5)])




class RecipeDescription_Ingredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, null=True ,blank=True ,related_name = 'ingredientRecipeDescription_Ingredient',on_delete=models.PROTECT)
    recipeDescription = models.ForeignKey(RecipeDescription, null=True ,blank=True ,related_name = 'recipeDescriptionRecipeDescription_Ingredient',on_delete=models.PROTECT)
    quantity = models.CharField(max_length=255)



class Reports(models.Model):
    user = models.ForeignKey(User, null=True ,blank=True ,related_name= 'userReports',on_delete=models.PROTECT)
    recipe = models.ForeignKey(Recipe, null=True ,blank=True ,related_name= 'recipeReports',on_delete=models.PROTECT)
    description= models.CharField(max_length=255)



class Request(models.Model):
    name = models.CharField(max_length=255)
    description= models.CharField(max_length=255)