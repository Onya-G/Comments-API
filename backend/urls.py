from rest_framework.routers import DefaultRouter

from .views import ArticleViewSet, CommentViewSet

router = DefaultRouter()
router.register('articles', ArticleViewSet)
router.register('comments', CommentViewSet)

urlpatterns = router.urls

