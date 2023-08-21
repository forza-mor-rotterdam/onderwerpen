from apps.categories.serializers import CategoryListSerializer
from apps.groups.models import Group
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers
from rest_framework.reverse import reverse


class GroupLinksSerializer(serializers.Serializer):
    self = serializers.SerializerMethodField()

    @extend_schema_field(OpenApiTypes.URI)
    def get_self(self, obj):
        return reverse(
            "v1:group-detail",
            kwargs={"group_uuid": obj.uuid},
            request=self.context.get("request"),
        )


class GroupListSerializer(serializers.ModelSerializer):
    """
    Group
    """

    _links = GroupLinksSerializer(source="*", read_only=True)
    _display = serializers.CharField(source="name", read_only=True)

    def get_categories(self, obj):
        serializer = CategoryListSerializer(obj.categories.all(), many=True)
        return serializer.data

    class Meta:
        model = Group
        fields = (
            "_links",
            "_display",
            "uuid",
            "name",
            "slug",
            "public_name",
            "is_public_accessible",
            "is_active",
            "meta",
        )
        read_only_fields = (
            "_links",
            "_display",
            "uuid",
            "name",
            "slug",
            "public_name",
            "is_public_accessible",
            "is_active",
            "meta",
        )


class GroupSerializer(serializers.ModelSerializer):
    """
    Group
    """

    _links = GroupLinksSerializer(source="*", read_only=True)
    _display = serializers.CharField(source="name", read_only=True)
    categories = serializers.SerializerMethodField()

    def get_categories(self, obj):
        serializer = CategoryListSerializer(obj.categories.all(), many=True)
        return serializer.data

    class Meta:
        model = Group
        fields = (
            "_links",
            "_display",
            "uuid",
            "name",
            "slug",
            "public_name",
            "is_public_accessible",
            "is_active",
            "meta",
            "categories",
        )
        read_only_fields = (
            "_links",
            "_display",
            "uuid",
            "name",
            "slug",
            "public_name",
            "is_public_accessible",
            "is_active",
            "meta",
            "categories",
        )
