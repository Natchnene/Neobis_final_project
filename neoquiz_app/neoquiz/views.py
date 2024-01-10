from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q

from .serializers import ArticleSerializer
from .models import Article


class ArticleResultsPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 120


class ArticlePaginationListAPIView(generics.ListAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    permission_classes = [permissions.AllowAny]
    pagination_class = ArticleResultsPagination


class ArticleSearchListAPIView(generics.ListAPIView):
    serializer_class = ArticleSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        query = self.request.query_params.get('query', '')
        return Article.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )

