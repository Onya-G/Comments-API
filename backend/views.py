from rest_framework.viewsets import ModelViewSet

from .serializers import ArticleSerializer, CommentSerializer
from .models import Article, Comment


class ArticleViewSet(ModelViewSet):
    """ViewSet для статей"""
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class CommentViewSet(ModelViewSet):
    """ViewSet для комментариев"""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

