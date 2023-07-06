from django.contrib import admin
from adminuser.models import Ingredient,Category,Recipe,Rating,Recipe_Ingredient,Reports,Request

admin.site.register(Ingredient)
admin.site.register(Category)
admin.site.register(Recipe)
admin.site.register(Rating)
admin.site.register(Recipe_Ingredient)
admin.site.register(Reports)
admin.site.register(Request)

