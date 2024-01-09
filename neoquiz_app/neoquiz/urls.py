from django.urls import path

from .views import (
    ArticlePaginationListAPIView,
    ArticleSearchListAPIView,
)


urlpatterns = [
    path('articles/', ArticlePaginationListAPIView.as_view(), name='articles_pagination'),
    path('articles/search/', ArticleSearchListAPIView.as_view(), name='article_search')
]
