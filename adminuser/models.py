from django.db import models
from users.models import User



class Ingredient(models.Model):
    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='static/ingredients/')
    id_ingrediant = models.CharField(max_length=255, null=True, blank = True )



class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    categoryImage = models.ImageField(upload_to='static/category/', null=True)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self) -> str:
        return self.name



class Recipe(models.Model):
    name = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='static/thumbnails/')
    idMeal = models.CharField(max_length=255,null=True)
    calculated_rating = models.FloatField(default = 0)
    is_approved = models.BooleanField(default=0)
    user = models.ForeignKey(User, null=True ,blank=True, related_name= 'recipe',on_delete=models.PROTECT)
    category = models.ForeignKey(Category, null=True ,blank=True ,related_name= 'recipe',on_delete=models.PROTECT)
    description = models.TextField()
    youtube_link = models.CharField(max_length=255, null=True)
    dateModified =models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default = True)




class Rating(models.Model):
    recipe = models.ForeignKey(Recipe, null=True ,blank=True ,related_name= 'rating',on_delete=models.PROTECT)
    rating = models.IntegerField(choices=[(1,1),(2,2),(3,3),(4,4),(5,5)])
    user = models.ForeignKey(User, related_name='rating', on_delete=models.PROTECT)




class Recipe_Ingredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, null=True ,blank=True ,related_name = 'recipe_Ingredient',on_delete=models.PROTECT)
    recipe = models.ForeignKey(Recipe, null=True ,blank=True ,related_name = 'recipe_Ingredient',on_delete=models.PROTECT)
    quantity = models.CharField(max_length=255)



class Reports(models.Model):
    user = models.ForeignKey(User, null=True ,blank=True ,related_name= 'reports',on_delete=models.PROTECT)
    recipe = models.ForeignKey(Recipe, null=True ,blank=True ,related_name= 'reports',on_delete=models.PROTECT)
    description= models.CharField(max_length=255)



class Request(models.Model):
    name = models.CharField(max_length=255)
    description= models.CharField(max_length=255)


class Favourites(models.Model):
    user = models.ForeignKey(User, null=True ,blank=True ,related_name = 'favourites',on_delete=models.PROTECT)
    recipe = models.ForeignKey(Recipe, null=True ,blank=True ,related_name = 'favourites',on_delete=models.PROTECT)
