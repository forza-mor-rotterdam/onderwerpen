from apps.categories.filtersets import CategoryFilter
from apps.categories.models import Category
from apps.categories.serializers import CategorySerializer
from django_filters import rest_framework as filters
from rest_framework import mixins, viewsets


class CategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    Category
    """

    queryset = Category.objects.all()

    permission_classes = ()

    serializer_class = CategorySerializer
    lookup_field = "uuid"

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CategoryFilter
