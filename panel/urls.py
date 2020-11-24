from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .api import ProfileViewSet, EnterpriseViewSet, UserViewSet, LoginAPI
from rest_framework.routers import DefaultRouter
from .urgent_views import index, loginPage, panel


urlpatterns = [
    path("profil/<str:usr>", index, name="panel"),
    path("panel/", panel, name="panel_dashboard"),
    path('login/', LoginAPI.as_view(), name='panel_login'),
    path('logout/', auth_views.LogoutView.as_view(), name='panel_logout'),

]

router  = DefaultRouter()
router.register(r'users',UserViewSet, basename='users')
router.register(r'profils',ProfileViewSet, basename='profils')
router.register(r'entreprises',EnterpriseViewSet, basename='enterprises')

urlpatterns += router.urls 
