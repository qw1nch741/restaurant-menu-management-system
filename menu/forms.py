from django import forms
from django.contrib.auth.forms import UserCreationForm
from menu.models import Cook, Dish, DishType

class CookForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = ("username", "first_name", "last_name", "email", "years_of_experience")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # This adds the 'form-control' class to every field for styling
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class DishTypeForm(forms.ModelForm):
    class Meta:
        model = DishType
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'