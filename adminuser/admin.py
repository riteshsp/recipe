from django.contrib import admin
from adminuser.models import Ingredient,Category,Recipe,RecipeDescription,Rating,RecipeDescription_Ingredient,Reports,Request

admin.site.register(Ingredient)
admin.site.register(Category)
admin.site.register(Recipe)
admin.site.register(RecipeDescription)
admin.site.register(Rating)
admin.site.register(RecipeDescription_Ingredient)
admin.site.register(Reports)
admin.site.register(Request)

