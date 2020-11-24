from rest_framework import viewsets, status, generics, permissions
from rest_framework.response import Response
from .permissions import IsProfileOrReadOnly, IsUserOrReadOnly, IsEnterpriseOrReadOnly
from .serializers import *
from .models import Profile, Enterprise
from django.contrib.auth import login
from django.contrib.auth.models import User
from rest_framework.decorators import action
from django.http import HttpResponseRedirect
from knox.models import AuthToken

class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = User.objects.all()
    # permission_classes = [permissions.IsAdminUser,IsUserOrReadOnly]
    def get_permission_class(self):
        return [permissions.AllowAny] if self.action == 'create' else [permissions.IsAdminUser,IsUserOrReadOnly]


    def get_serializer_class(self):
        return RegisterSerializer if self.action == 'create' else UserSerializer

    @action(detail=True, methods=['post'])
    def set_password(self, request, pk=None):
        user = self.get_object()
        serializer = PasswordSerializer(data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.data['password'])
            user.save()
            return Response({'status': 'password set'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
    


class ProfileViewSet(viewsets.ModelViewSet):
    """
    Vues pour lister et modifier des utilisateurs
    """
    queryset = Profile.objects.all()
    permissions_classes = [permissions.IsAdminUser,IsProfileOrReadOnly]
    serializer_class = ProfileSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class EnterpriseViewSet(viewsets.ModelViewSet):
    """
    Vues pour lister et modifier des entreprises
    """
    queryset = Enterprise.objects.all()
    permission_classes = [permissions.IsAdminUser,IsEnterpriseOrReadOnly]
    serializer_class = EnterpriseSerializer

    def perform_create(self, serializer):
        serializer.save(admin=self.request.user)


class LoginAPI(generics.GenericAPIView):
  serializer_class = LoginSerializer

  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data
        login(request,user)
        token = AuthToken.objects.create(user)
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": token[1]
        })
    else:
        return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)