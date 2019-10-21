from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('menu', views.menu, name='menu'),
    path('food/<int:type_id>', views.get_food_items),
    path('toppings', views.get_toppings),
]
