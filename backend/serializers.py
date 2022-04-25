from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from .models import Article, Comment


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для получения всего дерева комментариев"""
    children = RecursiveField(many=True, required=False, read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'article', 'text', 'author', 'created_at', 'parent', 'children',)


class ChildrenSerializer(serializers.ModelSerializer):
    """Промежуточный сериализатор вложенных комментариев для статьи"""

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'created_at', 'parent', 'children',)
        depth = 1


class RootCommentSerializer(serializers.ModelSerializer):
    """Сериализатор для вершины комментариев"""
    children = ChildrenSerializer(read_only=True, many=True)

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'created_at', 'parent', 'children',)


class ArticleSerializer(serializers.ModelSerializer):
    """Сериализатор для статьи с первыми тремя уровнями комментариев"""
    comments = RootCommentSerializer(read_only=True, many=True)

    class Meta:
        model = Article
        fields = ('id', 'text', 'comments',)
