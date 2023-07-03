from django.urls import path
from adminuser.views.category import AddCategory,DeleteCategory,ListCategory,FetchCategory,UpdateCategory
from adminuser.views.ingredient import AddIngredient,DeleteIngredient,ListIngredient,FetchIngredient,UpdateIngredient
from adminuser.views.recipe import AddRecipe ,ListRecipe
from adminuser.views.recipeDescription import Description ,AddRecipeToDB ,DescriptionDB


urlpatterns=[

    #############CATEGORY################

    path("add/category/",AddCategory.as_view()),
    path("delete/category/<int:id>",DeleteCategory.as_view()),
    path("category/",ListCategory.as_view()),
    path("fetch/category/",FetchCategory.as_view()),
    path("update/category/<int:id>",UpdateCategory.as_view()),

    #############INGREDIENT###############

    path("add/ingredient/",AddIngredient.as_view()),
    path("delete/ingredient/<int:id>",DeleteIngredient.as_view()),
    path("ingredient/",ListIngredient.as_view()),
    path("fetch/ingredient/",FetchIngredient.as_view()),
    path("update/ingredient/<int:id>",UpdateIngredient.as_view()),

    #############RECIPE################
    path("recipe/",ListRecipe.as_view()),
    path("add/recipe/",AddRecipe.as_view()),
    # path("delete/ingredient/<int:id>",DeleteIngredient.as_view()),
    # path("fetch/ingredient/",FetchIngredient.as_view()),
    # path("update/ingredient/<int:id>",UpdateIngredient.as_view()),


    #############RECIPE-DESCRIPTION################
    path("add/recipe/description/",Description.as_view()),
    path("recipe/description/",DescriptionDB.as_view()),

    path("add/recipe/toDB/",AddRecipeToDB.as_view()),





]