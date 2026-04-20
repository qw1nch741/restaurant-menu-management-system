from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from menu.forms import (CookForm,
                        DishSearchForm,
                        DishTypeSearchForm,
                        CookSearchForm)
from menu.models import (Dish,
                         DishType,
                         Cook)


class Index(LoginRequiredMixin, generic.TemplateView):
    template_name = "menu/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["num_dish"] = Dish.objects.count()
        context["num_dishtype"] = DishType.objects.count()
        context["num_cook"] = Cook.objects.count()

        return context


#Dish views
class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    context_object_name = "dish_list"
    template_name = "menu/dish_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("title", "")

        context["search_form"] = DishSearchForm(
            initial={"title": name})
        return context

    def get_queryset(self):
        queryset = Dish.objects.all()
        name = self.request.GET.get("title")

        if name:
            return queryset.filter(name__icontains=name)

        return queryset


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish
    template_name = "menu/dish_detail.html"


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("menu:dish-list")

    def form_valid(self, form):
        # Check if the logged-in user is the public 'tester'
        if self.request.user.username == "tester":
            messages.warning(
                self.request,
                "Demo Mode: Your changes were validated but not saved to the database."
            )
            return redirect("menu:dish-list")

        # If it's YOU (the admin), save normally
        return super().form_valid(form)


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("menu:dish-list")

    def form_valid(self, form):
        # Check if the logged-in user is the public 'tester'
        if self.request.user.username == "tester":
            messages.warning(
                self.request,
                "Demo Mode: Your changes were validated but not saved to the database."
            )
            return redirect("menu:dish-list")

        # If it's YOU (the admin), save normally
        return super().form_valid(form)


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("menu:dish-list")

#DishType views
class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    context_object_name = "dishtype_list"
    template_name = "menu/dishtype_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishTypeListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("title", "")

        context["search_form"] = DishTypeSearchForm(
            initial={"title": name})
        return context

    def get_queryset(self):
        queryset = DishType.objects.all()
        name = self.request.GET.get("title")

        if name:
            return queryset.filter(name__icontains=name)

        return queryset


class DishTypeDetailView(LoginRequiredMixin, generic.DetailView):
    model = DishType
    template_name = "menu/dishtype_detail.html"


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("menu:dish-type-list")

    def form_valid(self, form):
        # Check if the logged-in user is the public 'tester'
        if self.request.user.username == "tester":
            messages.warning(
                self.request,
                "Demo Mode: Your changes were validated but not saved to the database."
            )
            return redirect("menu:dish-list")

        # If it's YOU (the admin), save normally
        return super().form_valid(form)


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("menu:dish-type-list")

    def form_valid(self, form):
        # Check if the logged-in user is the public 'tester'
        if self.request.user.username == "tester":
            messages.warning(
                self.request,
                "Demo Mode: Your changes were validated but not saved to the database."
            )
            return redirect("menu:dish-list")

        # If it's YOU (the admin), save normally
        return super().form_valid(form)


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("menu:dish-type-list")


#Cook views
class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    context_object_name = "cook_list"
    template_name = "menu/cook_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CookListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("title", "")

        context["search_form"] = CookSearchForm(
            initial={"title": name})
        return context

    def get_queryset(self):
        queryset = Cook.objects.all()
        name = self.request.GET.get("title")

        if name:
            return queryset.filter(username__icontains=name)

        return queryset



class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook
    template_name = "menu/cook_detail.html"


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    form_class = CookForm
    success_url = reverse_lazy("menu:cook-list")

    def form_valid(self, form):
        # Check if the logged-in user is the public 'tester'
        if self.request.user.username == "tester":
            messages.warning(
                self.request,
                "Demo Mode: Your changes were validated but not saved to the database."
            )
            return redirect("menu:dish-list")

        # If it's YOU (the admin), save normally
        return super().form_valid(form)


class CookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    form_class = CookForm
    success_url = reverse_lazy("menu:cook-list")

    def form_valid(self, form):
        # Check if the logged-in user is the public 'tester'
        if self.request.user.username == "tester":
            messages.warning(
                self.request,
                "Demo Mode: Your changes were validated but not saved to the database."
            )
            return redirect("menu:dish-list")

        # If it's YOU (the admin), save normally
        return super().form_valid(form)


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("menu:cook-list")


class HelpPageView(generic.TemplateView):
    template_name = "menu/help_page.html"
