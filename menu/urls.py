# menu/urls.py
from django.urls import path
from .views import index # or whatever views you have

app_name = "menu"  # <--- ADD THIS LINE

urlpatterns = [
    path("", index, name="index"),
    #Dish Views
    path("dishes/", DishListView.as_view(), name="dishes-list"),
    path("dishes/create/",DishCreateView.as_view(), name="dish-create"),
    path("dishes/<int:pk>/update", DishUpdateView.as_view(), name="dish-update"),
    path("dishes/<int:pk>/delete", DishDeleteView.as_view(), name="dish-delete"),
    #Dishtype views
    path("dish-types/", DishTypeListView.as_view(), name="dish-types-list"),
    path("dish-types/create/",DishTypeCreateView.as_view(), name="dish-type-create"),
    path("dish-types/<int:pk>/update", DishTypeUpdateView.as_view(), name="dish-type-update"),
    path("dish-types/<int:pk>/delete", DishTypeDeleteView.as_view(), name="dish-type-delete"),
    #Cook views
    path("cooks/", CookListView.as_view(), name="cooks-list"),
    path("cooks/create/",CookCreateView.as_view(), name="cook-create"),
    path("cooks/<int:pk>/update", CookUpdateView.as_view(), name="cook-update"),
    path("cooks/<int:pk>/delete", CookDeleteView.as_view(), name="cook-delete"),
]