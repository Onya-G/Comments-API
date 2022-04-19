from django.db import models


class Article(models.Model):
    """Простейшая модель статей"""
    text = models.TextField()


class Comment(models.Model):
    """Модель комментариев"""
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', default=None, blank=True, null=True, related_name='children',
                               on_delete=models.SET_NULL)
    text = models.TextField()
    author = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
