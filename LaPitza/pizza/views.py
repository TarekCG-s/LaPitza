from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Type, Food, Topping
# Create your views here.
def index(request):
    return render(request, 'pizza/home.html', context=None)


def menu(request):
    types = Type.objects.all().exclude(name='sub_topping')
    context = {
        'title':'Menu',
        'types': types,
    }
    return render(request, 'pizza/menu.html', context=context)


def get_food_items(request, type_id):
    items = Food.objects.filter(type_id = type_id).all()
    type = Type.objects.get(pk=type_id)
    items_list = []
    for item in items:
        item_dict = {
            'name':item.name,
            'toppings':item.toppings,
            'id':item.id,
            'small':item.small,
            'large':item.large,
            'type':type.name,
        }
        items_list.append(item_dict)

    return JsonResponse(items_list, safe=False)


def get_toppings(request):
    toppings = Topping.objects.all();
    items_list = []
    for topping in toppings:
        items_list.append(topping.name)
    return JsonResponse(items_list, safe=False)
