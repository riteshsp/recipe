from rest_framework.views import APIView
from django.shortcuts import render, redirect
import requests
import json
import math
from adminuser.models import Recipe, RecipeDescription, Category, User,Ingredient, RecipeDescription_Ingredient
from recipe.pagination import PagePagination
from adminuser.serializer import RecipeListSerializer, RecipeSerializer
from rest_framework.response import Response
from django.contrib import messages


class Description(APIView):
    def get(self, request):
        item = request.GET.get("search_item")
        recipedata = requests.get(
            f"https://www.themealdb.com/api/json/v1/1/filter.php?i={item}")
        recipedata = json.loads(recipedata.content)

        id = request.GET.get("idMeal")
        data = requests.get(
            f'https://www.themealdb.com/api/json/v1/1/lookup.php?i={id}')
        data = json.loads(data.content)

        ingrediantList = []
        measureList = []
        for i in data['meals'][0]:
            item = i.startswith("strIngredient")
            item2 = i.startswith("strMeasure")
            if item:
                ingrediantList.append(data['meals'][0][i])
            if item2:
                measureList.append(data['meals'][0][i])
        data['meals'][0]["ingredient"] = ingrediantList
        data['meals'][0]["measure"] = measureList
        data['meals'][0]["searchMeals"] = recipedata["meals"][0:6]
        return render(request, "recipe/recipe_description.html", {"data": data['meals'][0]})


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
                    request, "Recipe already exists, Try another recipe")
                return redirect('/adminuser/add/recipe/')

            else:
                if Category.objects.filter(name=data['strCategory']).exists():
                    category_object = Category.objects.get(
                        name=data['strCategory'])
                    recipe_object = Recipe.objects.create(name=data['strMeal'], thumbnail=data['strMealThumb'], idMeal=data['idMeal'], is_approved=True, user=User.objects.get(
                        roles__name="admin"), category=category_object)
                    recipeDescription_object = RecipeDescription.objects.create(
                        recipe=recipe_object,  description=data['strInstructions'], youtube_link=data['strYoutube'],)
                    

                    for num in range(1,20):
                        item1 = "strIngredient"+str(num)
                        item2 = "strMeasure"+str(num)

                        if data[item1] and data[item2]:
                            ingredient=Ingredient.objects.filter(name=data[item1])[0]

                            if ingredient:
                                RecipeDescription_Ingredient.objects.create(ingredient=ingredient,recipeDescription=recipeDescription_object,quantity= data[item2])

                            else:
                                return("ingredient doesn't exist")   
                        else:
                            pass


                   
                    messages.success(request, "Recipe added successfully !!!")
                    return redirect('/adminuser/recipe/')
                else:
                    return Response('create category first')

        except Exception as e:
            print(str(e))
            return render(request, "recipe/recipe_description.html", {"errors": str(e)})


class DescriptionDB(APIView):
    def get(self, request):
        try:
            id = request.GET.get("id")
            recipe = Recipe.objects.get(id=id)
            print(recipe)
            serializer = RecipeSerializer(recipe)

            item = serializer.data
            print(item)

            if item['thumbnail'].startswith("/http"):
                item['thumbnail'] = item['thumbnail'][1:]
                item['thumbnail'] = item['thumbnail'].replace("%3A", ":/")
                print(item)
            else:
                pass

            return render(request, "recipe/recipe_descriptionDB.html", {"data": item})

        except Exception as e:
            print(str(e))
            return render(request, "recipe/recipe_descriptionDB.html")
