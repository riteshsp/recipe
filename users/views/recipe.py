from rest_framework.views import APIView
from django.shortcuts import render
from adminuser.models import Category, Recipe
from adminuser.serializer import CategorySerializer
from users.serializer import RecipeListSerializer




class Home(APIView):
    def get(self, request):
        # category=Category.objects.all()
        data={}
        data["category"] = Category.objects.all().values()
        data["recipe"] = Recipe.objects.all().order_by('calculated_rating').values()       


        return render(request, "users/home.html",{"data":data})
    

class SearchByCategory(APIView):
    def get(self, request):
        id = request.GET.get("categoryid")
        recipe = Recipe.objects.filter(category = id)
        return render(request, "users/recipebycategory.html",{"data":recipe})
    
   
   
   
