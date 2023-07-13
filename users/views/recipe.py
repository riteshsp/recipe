from rest_framework.views import APIView
from django.shortcuts import render ,redirect
from adminuser.models import Category, Recipe,Favourites
from adminuser.serializer import CategorySerializer,Recipe_IngredientSerializer
from users.serializer import RecipeListSerializer
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from recipe.pagination import PagePagination
import math



class Home(APIView):

    # def get(self, request):
    #     try:
    #         data={}
    #         data["category"] = Category.objects.all().values()
    #         data["recipe"] = Recipe.objects.all().order_by('calculated_rating').values("id","name","thumbnail")    
    #         return render(request, "users/home.html",{"data":data})
    #     except Exception as e:
    #         return render(request, "users/home.html",{"data":data})



            # page_number=request.GET.get("page","1")
            # data = paginator.get_paginated_response(serializer.data).data
            # data["search_data"]=name
            # data["page"]=page_number
            # data["last_page"]=math.ceil(recipe.count()/paginator.get_page_size(request))



    def get(self, request):
        try:
            data={}
            data["category"] = Category.objects.all().values()
            recipe= Recipe.objects.all().order_by('calculated_rating').values("id","name","thumbnail")

            paginator = PagePagination()
            results = paginator.paginate_queryset(recipe , request , view=self)
            paginated_data = paginator.get_paginated_response(results).data
            data["recipe"] = paginated_data
            page_number=request.GET.get("page","1")
            data["recipe"]["page"]=page_number
            data["recipe"]["last_page"]=math.ceil(recipe.count()/paginator.get_page_size(request))


            return render(request, "users/home.html",{"data":data})
        except Exception as e:
            return render(request, "users/home.html",{"data":data})




class SearchByCategory(LoginRequiredMixin,APIView):
    def get(self, request):
        id = request.GET.get("categoryid")
        recipe = Recipe.objects.filter(category = id)
        return render(request, "users/recipebycategory.html",{"data":recipe})
    
   


class RecipeDescription(APIView):
    def get(self, request):
        try:
            id = request.GET.get("id")
            recipe = Recipe.objects.get(id=id)
            serializer = Recipe_IngredientSerializer(recipe)
            item = serializer.data

            item["isFavourite"] = Favourites.objects.filter(user =request.user , recipe = recipe )

            if item['thumbnail'].startswith("/http"):
                item['thumbnail'] = item['thumbnail'][1:]
                item['thumbnail'] = item['thumbnail'].replace("%3A", ":/")

            else:
                pass
            recipe = Recipe.objects.filter(category__name = item['category']).values('id','name','thumbnail','category')
            try:
                item['similar_items']=list(recipe)   
            except Exception as e:
                pass       
            return render(request, "users/description.html", {"data": item})
        except Exception as e:
            return render(request, "users/description.html", {"errors": str(e)})   
   





class SearchRecipe(APIView):
    def get(self,request):
        try:
            name=request.GET.get("search_data","")
            recipe=Recipe.objects.filter(name__icontains=name)
          
            paginator = PagePagination()
            results = paginator.paginate_queryset(recipe , request , view=self)
            serializer= RecipeListSerializer(results ,many=True)

            page_number=request.GET.get("page","1")
            data = paginator.get_paginated_response(serializer.data).data
            data["search_data"]=name
            data["page"]=page_number
            data["last_page"]=math.ceil(recipe.count()/paginator.get_page_size(request))


            for item in data['results']:
                if item['thumbnail'].startswith("/http"):
                    item['thumbnail'] = item['thumbnail'][1:]
                    item['thumbnail'] = item['thumbnail'].replace("%3A",":/")
                else:
                    pass
            return render(request,"users/search_recipe.html" ,{'data': data})
            # return Response(data)
        except Exception as e:
            # return Response(str(e))
            return render(request,"users/search_recipe.html" ,{'data': str(e)})
        


class AddFavourites(APIView):
    def get(self,request):
        try:
            id = request.GET.get("id")
            user = request.user
            recipe = Recipe.objects.get(id=id)
            if Favourites.objects.filter(recipe__id=id):
                pass
            else:
                Favourites.objects.create(user = user, recipe = recipe)
            # return render(request,"users/search_recipe.html" ,{'data': id})
            return redirect(f"/recipe/description/?id={id}")
        except Exception as e:
            return render(request,"users/search_recipe.html" ,{'data': str(e)})
        

class ListFavourites(LoginRequiredMixin, APIView):
    def get(self,request):
        try:           
            user = request.user
            data = Favourites.objects.filter(user = user)
            return render(request,"users/favourites.html" ,{'data': data})
            # return redirect(f"/recipe/description/?id={id}")
        except Exception as e:
            return render(request,"users/favourites.html" ,{'data': str(e)})



class DeleteFavourites(APIView):
    def get(self,request):
        try:
            id = request.GET.get("id")
            favourite_obj = Favourites.objects.get(id=id)
            favourite_obj.delete()
            return redirect("/favourites")
        except Exception as e:
            return render(request,"users/favourites.html" ,{'data': str(e)})