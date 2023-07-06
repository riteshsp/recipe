from rest_framework.views import APIView
from django.shortcuts import render,redirect
import requests ,json ,math
from adminuser.models import Recipe,Category, User,Ingredient, Recipe_Ingredient
from recipe.pagination import PagePagination
from adminuser.serializer import RecipeListSerializer,Recipe_IngredientSerializer
from rest_framework.response import Response
from django.contrib import messages




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
             
            #search by name
            data1=requests.get(f"https://www.themealdb.com/api/json/v1/1/search.php?s={request.data['mainIngredient']}") 
            #search by ingredient
            data = requests.get(f"https://www.themealdb.com/api/json/v1/1/filter.php?i={request.data['mainIngredient']}")
            data1 = json.loads(data1.content) 
            data = json.loads(data.content)   
            data1['search_item']=request.data['mainIngredient']
            try:
                for items in data["meals"]:
                    data1["meals"].append(items)
            except Exception as e:
                pass
            return render(request, "recipe/add_recipe.html", {'data': data1})
        except Exception as e:
            return render(request, "recipe/add_recipe.html")




# recipe description


class Description(APIView):
    def get(self, request):
        try:
            item = request.GET.get("search_item")
            recipedata = requests.get(
                f"https://www.themealdb.com/api/json/v1/1/filter.php?i={item}")
            recipedata = json.loads(recipedata.content)

            id = request.GET.get("idMeal")
            data = requests.get(
                f'https://www.themealdb.com/api/json/v1/1/lookup.php?i={id}')
            data = json.loads(data.content)


            ingredient = {}
            for num in range(1,21):
                item1 = "strIngredient"+str(num)
                item2 = "strMeasure"+str(num)

                if data["meals"][0][item1] and data["meals"][0][item2]:
                    ingredient[data["meals"][0][item1]]=data["meals"][0][item2]
                else:
                    pass
            data['meals'][0]["ingredient"] = ingredient
            data['meals'][0]["searchMeals"] = recipedata["meals"][0:6]

            return render(request, "recipe/recipe_description.html", {"data": data['meals'][0]})
        except Exception as e :
            return render(request, "recipe/recipe_description.html", {"errors": str(e)})






class AddRecipeToDB(APIView):
    def get(self, request):
        try:
            id = request.GET.get("idMeal")
            data = requests.get(
                f'https://www.themealdb.com/api/json/v1/1/lookup.php?i={id}')
            data = json.loads(data.content)
            data = data['meals'][0]
            recipe = Recipe.objects.filter(idMeal=id)

            if recipe:
                messages.success(
                    request, "Recipe alrea'.dy exists, Try another recipe")
                return redirect('/adminuser/add/recipe/')

            else:
                if Category.objects.filter(name=data['strCategory']).exists():
                    category_object = Category.objects.get(
                        name=data['strCategory'])
                    recipe_object = Recipe.objects.create(name=data['strMeal'], thumbnail=data['strMealThumb'], idMeal=data['idMeal'], is_approved=True, user=User.objects.get(
                        roles__name="admin"), category=category_object,description=data['strInstructions'],youtube_link=data['strYoutube'])
                    for num in range(1,21):
                        item1 = "strIngredient"+str(num)
                        item2 = "strMeasure"+str(num)

                        if data[item1] and data[item2]:
                            ingredient=Ingredient.objects.filter(name=data[item1])[0]

                            if ingredient:
                                Recipe_Ingredient.objects.create(ingredient=ingredient,recipe=recipe_object,quantity= data[item2])
                            else:
                                return("ingredient doesn't exist")   
                        else:
                            pass
                    messages.success(request, "Recipe added successfully !!!")
                    return redirect('/adminuser/recipe/')
                else:
                    return Response('create category first')

        except Exception as e:
            return render(request, "recipe/recipe_description.html", {"errors": str(e)})






class DescriptionDB(APIView):
    def get(self, request):
        try:
            id = request.GET.get("id")
            recipe = Recipe.objects.get(id=id)
            serializer = Recipe_IngredientSerializer(recipe)

            item = serializer.data
            if item['thumbnail'].startswith("/http"):
                item['thumbnail'] = item['thumbnail'][1:]
                item['thumbnail'] = item['thumbnail'].replace("%3A", ":/")
            else:
                pass
            return render(request, "recipe/recipe_descriptionDB.html", {"data": item})
        
        except Exception as e:
            return render(request, "recipe/recipe_descriptionDB.html",{"errors": str(e)})




class DeleteRecipe(APIView):
    def get(self,request):
        id = request.GET.get("id")
        recipeIngredientObj=Recipe_Ingredient.objects.filter(recipe=id)
        recipeObj=Recipe.objects.get(id=id)
        recipeIngredientObj.delete()
        recipeObj.delete()
        return redirect("/adminuser/recipe/")