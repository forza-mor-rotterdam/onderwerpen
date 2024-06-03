from apps.categories.models import Category
from django import forms
from utils.forms import RadioSelect


class CategoryAanpassenForm(forms.ModelForm):
    priority = forms.ChoiceField(
        widget=RadioSelect(
            attrs={
                "class": "list--form-radio-input",
            }
        ),
        label="Prioriteit",
        choices=(
            (1, "Hoog"),
            (0, "Normaal"),
        ),
        required=True,
    )

    class Meta:
        model = Category
        fields = (
            "name",
            "priority",
            "is_active",
        )


class CategoryAanmakenForm(forms.ModelForm):
    priority = forms.ChoiceField(
        widget=RadioSelect(
            attrs={
                "class": "list--form-radio-input",
            }
        ),
        label="Prioriteit",
        choices=(
            (1, "Hoog"),
            (0, "Normaal"),
        ),
        required=True,
    )

    class Meta:
        model = Category
        fields = (
            "name",
            "priority",
            "is_active",
            "group",
        )
