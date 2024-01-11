from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

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
    swagger_schema_fields = {
        'operation_description': 'Get a list of articles with pagination.',
        'manual_parameters': [
            openapi.Parameter('page', openapi.IN_QUERY, description='Page number', type=openapi.TYPE_INTEGER),
            openapi.Parameter('page_size', openapi.IN_QUERY, description="Number of items per page",
                              type=openapi.TYPE_INTEGER),
        ],
        'responses': {
            200: ArticleSerializer(many=True),
            400: 'Bad Request',
        }
    }


class ArticleSearchListAPIView(generics.ListAPIView):
    serializer_class = ArticleSerializer
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(
        operation_description='Get a list of articles based on search query',
        manual_parameters=[
            openapi.Parameter(
                'query',
                openapi.IN_QUERY,
                description='Search query to filter articles by title or content.',
                type=openapi.TYPE_STRING,
                required=False
            ),
        ],
        responses={
            200: ArticleSerializer(many=True),
            400: 'Bad Request',
        }
    )
    def get_queryset(self):
        query = self.request.query_params.get('query', '')
        return Article.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )

