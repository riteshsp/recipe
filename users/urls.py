from django.contrib import admin
from django.urls import path, include
from users.views.views import SignUp,Login ,VerifyEmail ,LogOutUser
from users.views.recipe import Home, SearchByCategory,RecipeDescription,ListFavourites,SearchRecipe,AddFavourites, DeleteFavourites

urlpatterns = [
    path('signup/', SignUp.as_view()),
    path('', Login.as_view()),
    path('logout',LogOutUser.as_view()),
    path('user/verification/<str:code>',VerifyEmail.as_view()),
    
    path('search/bycategory/',SearchByCategory.as_view()),
    path('home/',Home.as_view()),
    path('recipe/description/',RecipeDescription.as_view()),
    path('search/recipe/',SearchRecipe.as_view()),
    path('add/tofavourite/',AddFavourites.as_view()),
    path('favourites/',ListFavourites.as_view()),
    path('favourites/delete/',DeleteFavourites.as_view()),





]   