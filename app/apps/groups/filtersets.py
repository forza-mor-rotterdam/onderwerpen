from apps.groups.models import Group
from django.forms.fields import CharField, MultipleChoiceField
from django_filters import rest_framework as filters


class MultipleValueField(MultipleChoiceField):
    def __init__(self, *args, field_class, **kwargs):
        self.inner_field = field_class()
        super().__init__(*args, **kwargs)

    def valid_value(self, value):
        return self.inner_field.validate(value)

    def clean(self, values):
        return values and [self.inner_field.clean(value) for value in values]


class MultipleValueFilter(filters.Filter):
    field_class = MultipleValueField

    def __init__(self, *args, field_class, **kwargs):
        kwargs.setdefault("lookup_expr", "in")
        super().__init__(*args, field_class=field_class, **kwargs)


class GroupFilter(filters.FilterSet):
    meldr_category = MultipleValueFilter(
        field_class=CharField, method="get_categories_by_meldr_category"
    )

    def get_categories_by_meldr_category(self, queryset, name, value):
        if value:
            print(value)
            print(queryset.filter(categories__meta__meldr="Grofvuil"))
            return queryset.filter(categories__meta__meldr__in=value).distinct()
        return queryset

    class Meta:
        model = Group
        fields = [
            "meldr_category",
        ]
