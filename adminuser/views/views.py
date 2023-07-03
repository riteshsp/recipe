from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from adminuser.serializer import CategorySerializer
from adminuser.models import Category
from django.contrib import messages
from django.shortcuts import redirect
import requests
import json



