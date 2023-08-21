from apps.questions.models import Question
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers
from rest_framework.reverse import reverse


class QuestionLinksSerializer(serializers.Serializer):
    self = serializers.SerializerMethodField()

    @extend_schema_field(OpenApiTypes.URI)
    def get_self(self, obj):
        return reverse(
            "v1:group-question",
            kwargs={
                "group_uuid": obj.category.group.uuid,
                "category_uuid": obj.category.uuid,
                "question_uuid": obj.uuid,
            },
            request=self.context.get("request"),
        )


class QuestionSerializer(serializers.ModelSerializer):
    """
    Question
    """

    _links = QuestionLinksSerializer(source="*", read_only=True)
    category_uuid = serializers.CharField(source="category.uuid")

    class Meta:
        model = Question
        fields = (
            "_links",
            "uuid",
            "sort",
            "key",
            "name",
            "public_name",
            "field_type",
            "description",
            "required",
            "required",
            "category_uuid",
            "meta",
        )
        read_only_fields = (
            "_links",
            "uuid",
            "sort",
            "key",
            "name",
            "public_name",
            "field_type",
            "description",
            "required",
            "required",
            "category_uuid",
            "meta",
        )
