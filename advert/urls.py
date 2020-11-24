from .urgent_views import index, AdDetail
from .api import AdViewSet, CategoryViewSet
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
urlpatterns = [
    path('', index, name='index'),
    path("annonce/<str:slug>", AdDetail.as_view(), name="ad_detail")
]
router.register(r'annonces',AdViewSet, basename='annonces')
router.register(r'categories',CategoryViewSet, basename='categories')

urlpatterns += router.urls 