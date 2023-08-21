from apps.categories.models import Category
from apps.categories.serializers import CategorySerializer
from rest_framework import mixins, viewsets


class CategoryViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    """
    Category
    """

    queryset = Category.objects.all()

    permission_classes = ()

    serializer_class = CategorySerializer
    lookup_field = "uuid"
