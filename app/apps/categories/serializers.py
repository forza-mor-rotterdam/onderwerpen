from apps.categories.models import Category
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers
from rest_framework.reverse import reverse


class CategoryLinksSerializer(serializers.Serializer):
    self = serializers.SerializerMethodField()

    @extend_schema_field(OpenApiTypes.URI)
    def get_self(self, obj):
        return reverse(
            "v1:group-category",
            kwargs={
                "group_uuid": obj.group.uuid,
                "category_uuid": obj.uuid,
            },
            request=self.context.get("request"),
        )


class CategoryListSerializer(serializers.ModelSerializer):
    """
    Category list
    """

    _links = CategoryLinksSerializer(source="*", read_only=True)
    _display = serializers.CharField(source="public_name")
    group_uuid = serializers.CharField(source="group.uuid")
    priority = serializers.SerializerMethodField()

    def get_priority(self, obj):
        return "normal" if int(obj.meta.get("priority", 0)) <= 0 else "high"

    class Meta:
        model = Category
        fields = (
            "_links",
            "_display",
            "uuid",
            "name",
            "slug",
            "public_name",
            "description_private",
            "description_public",
            "is_public_accessible",
            "is_active",
            "group_uuid",
            "meta",
        )
        read_only_fields = (
            "_links",
            "_display",
            "uuid",
            "name",
            "slug",
            "public_name",
            "description_private",
            "description_public",
            "is_public_accessible",
            "is_active",
            "group_uuid",
            "meta",
            "priority",
        )


class CategorySerializer(CategoryListSerializer):
    """
    Category
    """

    _links = CategoryLinksSerializer(source="*", read_only=True)
    questions = serializers.SerializerMethodField()
    group_uuid = serializers.CharField(source="group.uuid")

    def get_questions(self, obj):
        from apps.questions.serializers import QuestionSerializer

        serializer = QuestionSerializer(obj.questions.all(), many=True)
        return serializer.data

    class Meta:
        model = Category
        fields = (
            "_links",
            "uuid",
            "name",
            "slug",
            "public_name",
            "description_private",
            "description_public",
            "is_public_accessible",
            "is_active",
            "meta",
            "group_uuid",
            "questions",
            "priority",
        )
        read_only_fields = (
            "_links",
            "uuid",
            "name",
            "slug",
            "public_name",
            "description_private",
            "description_public",
            "is_public_accessible",
            "is_active",
            "meta",
            "group_uuid",
            "questions",
            "priority",
        )
        lookup_field = "category_uuid"
