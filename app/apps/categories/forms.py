from apps.categories.models import Category
from django import forms


class CategoryAanpassenForm(forms.ModelForm):
    priority = forms.ChoiceField(
        widget=forms.RadioSelect(
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

    is_active = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={
                "class": "form-check-input",
            }
        ),
        label="Is actief",
        required=False,
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
        widget=forms.RadioSelect(
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

    is_active = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={
                "class": "form-check-input",
            }
        ),
        label="Is actief",
        required=False,
    )

    class Meta:
        model = Category
        fields = (
            "name",
            "priority",
            "is_active",
            "group",
        )
