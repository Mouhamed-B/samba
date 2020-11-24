from rest_framework import viewsets, permissions
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from .serializers import AdSerializer, CategorySerializer
from .models import Ad, Category
from .permissions import IsAuthorOrReadOnly, IsAdminUserOrReadOnly

class AdViewSet(viewsets.ModelViewSet):
    """
    Vues pour lister et modifier des publicités
    """
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    serializer_class = AdSerializer
    queryset = Ad.objects.all()

    def get_permission_class(self):
        return [permissions.IsAuthenticated] if self.action == 'create' else [permissions.IsAdminUser,IsAuthorOrReadOnly]

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)

class CategoryViewSet(viewsets.ModelViewSet):
    """
    Vues pour lister et modifier des catégories
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAdminUserOrReadOnly]