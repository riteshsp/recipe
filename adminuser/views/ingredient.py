from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from adminuser.serializer import IngredientSerializer
from adminuser.models import Ingredient
from django.contrib import messages
from django.shortcuts import redirect
from recipe.pagination import PagePagination
import requests
import json
import math

        

# class ListIngredient(APIView, PageNumberPagination):
  
#     def get(self,request):
        
#         try:
#             name=request.GET.get("search_data" , "")
#             ingredient=Ingredient.objects.filter(name__icontains=name)
#             self.page_query_param = 'page'
#             self.page_size=10
#             results = self.paginate_queryset( ingredient,request, view=self)
#             serializer= IngredientSerializer(results ,many=True)
#             return render(request,"ingredient/ingredient.html" ,{'data':serializer.data})
#         except Exception as e:
#             return render(request,"ingredient/ingredient.html" ,{'errors':str(e)})




class ListIngredient(APIView):
  
    def get(self,request):        
        try:
            name=request.GET.get("search_data" , "")
            ingredient=Ingredient.objects.filter(name__icontains=name)
            paginator = PagePagination()
            results = paginator.paginate_queryset( ingredient , request , view=self)
            serializer= IngredientSerializer(results ,many=True)
            page_number=request.GET.get("page","")
            data = paginator.get_paginated_response(serializer.data).data
            data["page"]=page_number
            data["last_page"]=math.ceil(ingredient.count()/paginator.get_page_size(request))
            return render(request,"ingredient/ingredient.html" ,{'data':data})
        except Exception as e:
            # return Response(str(e))
            return render(request,"ingredient/ingredient.html" ,{'errors':str(e)})






class AddIngredient(APIView):
    def get(self,request):
        ingredient=Ingredient.objects.all()
        serializer= IngredientSerializer(ingredient ,many=True)
        return render(request,"ingredient/add_ingredient.html" ,{'data': serializer.data})
    

    
    def post(self,request):
        try:
            data = {
                    "name": request.data["ingredient_name"],
                    "image": request.data["ingredient_image"]               
                }
            serializer=IngredientSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                messages.success(request, f"ingredient '{data['name']}' created Successfully!!!")
                return redirect ('/adminuser/add/ingredient/')
            else:
                return render(request, "ingredient/add_ingredient.html", {"errors": serializer.errors})    
        except Exception as e:
            return render(request, 'ingredient/add_ingredient.html', {"errors": str(e)})

class FetchIngredient(APIView):
    def get(self,request):        
        try:
            apidata = requests.get("http://www.themealdb.com/api/json/v1/1/list.php?i=list")   
            apidata = json.loads(apidata.content)
            data=apidata['meals']
            count=0
            for items in data:
                if not Ingredient.objects.filter(id_ingrediant=items["idIngredient"]):
                    count += 1
                    image_url = f"http://www.themealdb.com/images/ingredients/{items['strIngredient']}.png"

                    Ingredient.objects.create(name=items["strIngredient"],image=image_url,id_ingrediant=items["idIngredient"])
                    
            messages.success(request, f"{count} Ingredients added")
            return redirect('/adminuser/ingredient/')
  
        except Exception as e:
            return render(request, 'ingredient/add_ingredient.html', {"errors": str(e)})






class DeleteIngredient(APIView):
    def get(self,request,id):
        item=Ingredient.objects.get(id=id)
        item.delete()
        messages.success(request,"ingredient Deleted Successfully")
        return redirect ('/adminuser/ingredient/')


class UpdateIngredient(APIView):
    def get(self, request, id):
        ingredient = Ingredient.objects.get(id=id)
        serializer = IngredientSerializer(ingredient)
        return render(request, "ingredient/update_ingredient.html", {"formdata": serializer.data})


    def post(self, request, id):      
        try:
            data={
                "name":request.data['ingredient_name'],
                "image":request.data['ingredient_image'],
            }


            ingredient = Ingredient.objects.get(id=id)
            serializer = IngredientSerializer(ingredient, data)

            if serializer.is_valid():
                serializer.save()
                messages.success(request,"ingredient Updated Successfully")
                return redirect ('/adminuser/ingredient/')
            else:
                return render(request, 'ingredient/add_ingredient.html', {"errors": serializer.errors})

        except Exception as e:
                return render(request, 'ingredient/add_ingredient.html', {"errors": serializer.errors})
