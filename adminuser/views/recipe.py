from rest_framework.views import APIView
from django.shortcuts import render
import requests ,json ,math
from adminuser.models import Recipe
from recipe.pagination import PagePagination
from adminuser.serializer import RecipeListSerializer
from rest_framework.response import Response



class ListRecipe(APIView):

    def get(self,request):
        try:

            name=request.GET.get("search_data","")
            recipe=Recipe.objects.filter(name__icontains=name)


            paginator = PagePagination()
            results = paginator.paginate_queryset(recipe , request , view=self)
            serializer= RecipeListSerializer(results ,many=True)


            page_number=request.GET.get("page","")
            data = paginator.get_paginated_response(serializer.data).data
            data["page"]=page_number
            data["last_page"]=math.ceil(recipe.count()/paginator.get_page_size(request))
            for item in data['results']:
                if item['thumbnail'].startswith("/http"):
                    item['thumbnail'] = item['thumbnail'][1:]
                    item['thumbnail'] = item['thumbnail'].replace("%3A",":/")
                else:
                    pass
            return render(request,"recipe/recipe.html" ,{'data': data})
            # return Response(data)


        except Exception as e:
            # return Response(str(e))
            return render(request,"recipe/recipe.html" ,{'data': str(e)})





class AddRecipe(APIView):
    def get(self, request):
        return render(request, "recipe/add_recipe.html")

    def post(self, request):
        try:
            data = requests.get(f"https://www.themealdb.com/api/json/v1/1/filter.php?i={request.data['mainIngredient']}")   
            data = json.loads(data.content)   
            data['search_item']=request.data['mainIngredient']
            return render(request, "recipe/add_recipe.html", {'data': data})
        except Exception as e:
            return render(request, "recipe/add_recipe.html")




