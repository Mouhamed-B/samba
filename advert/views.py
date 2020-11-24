#from .models import Ad, Category
#from .serializers import AdSerializer, CategorySerializer
#from rest_framework import status
#from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
#from django.http import Http404
#from django.shortcuts import render
#from django.contrib.auth.mixins import LoginRequiredMixin
#from django.views.decorators.csrf import csrf_protect
#from django.contrib.auth.decorators import login_required
# Create your views here.

@api_view(['GET'])
def index(request):
    """
    Api de gestion des publicités et catégories
    """
    urls = {
       'ad list' : "ads/",
       'ad detail' : "ads/<str:pk>/",
       'category list' : "categories/",
       'category detail' : "categories/<str:pk>/"
    }

    return Response(urls)


"""
Ad Model
"""


"""
Category Model
"""