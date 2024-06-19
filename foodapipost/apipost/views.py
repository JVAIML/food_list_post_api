from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import foodlistpost
# Create your views here.

class food_list_post(APIView):
    def get(self,request):
        allfood = foodlistpost.objects.all().values()
        print(allfood)
        return Response({"Message":"List of food","food list":allfood})

    def post(self,request):
        foodlistpost.objects.create(recipe_name=request.data["recipe_name"],
                               description=request.data["description"],
                               ingredients=request.data["ingredients"],
                               category=request.data["category"],
                               method=request.data["method"])

        foodpost = foodlistpost.objects.all().filter(recipe_name=request.data["recipe_name"]).values()
        return Response({"Message":"New List of food","food list":foodpost})