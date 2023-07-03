from django.contrib import admin
from django.urls import path, include
from users.views import SignUp,Login ,VerifyEmail ,Home

urlpatterns = [
    path('signup/', SignUp.as_view()),
    path('home/',Home.as_view()),
    path('', Login.as_view()),
    path('user/verification/<str:code>',VerifyEmail.as_view())
    
]   