from apps.categories.models import Category
from apps.categories.serializers import CategorySerializer
from apps.groups.models import Group
from apps.groups.serializers import GroupListSerializer, GroupSerializer
from apps.questions.models import Question
from apps.questions.serializers import QuestionSerializer
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class GroupViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    """
    Group
    """

    queryset = Group.objects.all()

    permission_classes = ()

    serializer_class = GroupListSerializer
    serializer_detail_class = GroupSerializer
    lookup_field = "group_uuid"

    def get_serializer_class(self):
        if self.action == "retrieve":
            return self.serializer_detail_class
        return super().get_serializer_class()

    def get_object(self):
        if self.action == "retrieve":
            return get_object_or_404(self.get_queryset(), pk=self.kwargs["group_uuid"])
        return super().get_object()

    @action(detail=True, methods=["get"], url_path="category/(?P<category_uuid>[^/.]+)")
    def category(self, request, group_uuid, category_uuid):
        try:
            category = Category.objects.get(pk=category_uuid)
        except Category.DoesNotExist:
            raise Http404("No Category matches the given query.")

        return Response(
            data=CategorySerializer(category).data,
            status=status.HTTP_200_OK,
        )

    @action(
        detail=True,
        methods=["get"],
        url_path="category/(?P<category_uuid>[^/.]+)/question/(?P<question_uuid>[^/.]+)",
    )
    def question(self, request, group_uuid, category_uuid, question_uuid):
        try:
            question = Question.objects.get(pk=question_uuid)
        except Question.DoesNotExist:
            raise Http404("No Question matches the given query.")

        return Response(
            data=QuestionSerializer(question).data,
            status=status.HTTP_200_OK,
        )
