from apps.questions.models import Question
from apps.questions.serializers import QuestionSerializer
from rest_framework import mixins, viewsets


class QuestionViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    """
    Question
    """

    queryset = Question.objects.all()

    permission_classes = ()

    serializer_class = QuestionSerializer
    lookup_field = "uuid"
