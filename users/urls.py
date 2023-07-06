from django.contrib import admin
from django.urls import path, include
from users.views.views import SignUp,Login ,VerifyEmail 
from users.views.recipe import Home, SearchByCategory

urlpatterns = [
    path('signup/', SignUp.as_view()),
    path('', Login.as_view()),
    path('user/verification/<str:code>',VerifyEmail.as_view()),
    
    path('search/bycategory/',SearchByCategory.as_view()),
    path('home/',Home.as_view()),

]   