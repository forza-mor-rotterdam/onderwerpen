from apps.categories.forms import CategoryAanmakenForm, CategoryAanpassenForm
from apps.categories.models import Category
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

Gebruiker = get_user_model()


def http_404(request):
    return render(
        request,
        "404.html",
    )


def http_500(request):
    return render(
        request,
        "500.html",
    )


@login_required
def root(request):
    if request.user.has_perms(["authorisatie.beheer_bekijken"]):
        return redirect(reverse("beheer"))
    return render(
        request,
        "home.html",
        {},
    )


@permission_required("authorisatie.beheer_bekijken", raise_exception=True)
def beheer(request):
    return render(
        request,
        "beheer/beheer.html",
        {},
    )


class OnderwerpView(View):
    model = Category
    success_url = reverse_lazy("onderwerp_lijst")


@method_decorator(login_required, name="dispatch")
@method_decorator(
    permission_required("authorisatie.onderwerp_lijst_bekijken", raise_exception=True),
    name="dispatch",
)
class OnderwerpLijstView(OnderwerpView, ListView):
    queryset = Category.objects.all().order_by("group__name", "name")


class OnderwerpAanmakenAanpassenView(OnderwerpView):
    form_class = CategoryAanpassenForm
    template_name = "categories/category_aanpassen.html"

    def form_valid(self, form):
        form.instance.meta["priority"] = int(form.cleaned_data.get("priority"))
        form.instance.public_name = form.cleaned_data.get("name")
        return super().form_valid(form)


@method_decorator(login_required, name="dispatch")
@method_decorator(
    permission_required("authorisatie.onderwerp_aanpassen", raise_exception=True),
    name="dispatch",
)
class OnderwerpAanpassenView(OnderwerpAanmakenAanpassenView, UpdateView):
    form_class = CategoryAanpassenForm
    template_name = "categories/category_aanpassen.html"

    def get_initial(self):
        initial = self.initial.copy()
        obj = self.get_object()
        initial["priority"] = int(obj.meta.get("priority", 0))
        return initial


@method_decorator(login_required, name="dispatch")
@method_decorator(
    permission_required("authorisatie.onderwerp_aanmaken", raise_exception=True),
    name="dispatch",
)
class OnderwerpAanmakenView(OnderwerpAanmakenAanpassenView, CreateView):
    template_name = "categories/category_aanmaken.html"
    form_class = CategoryAanmakenForm
