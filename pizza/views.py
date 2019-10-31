from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.views import login_required
from django.contrib.auth.models import User
from .forms import Address as AddressForm
from .models import Type, Food, Topping, Status, Order, Order_Item, Address as AddressModel
import json


def index(request):
    return render(request, 'pizza/home.html', context=None)


def menu(request):
    types = Type.objects.all().exclude(name='sub_topping')
    context = {
        'title':'Menu',
        'types': types,
    }
    return render(request, 'pizza/menu.html', context=context)

@login_required
def address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('address')
    else:
        form = AddressForm()
    addresses = AddressModel.objects.filter(user_id=request.user.id).all()
    context ={
        'form':form,
        'addresses':addresses,
    }
    return render(request, 'pizza/address.html', context=context)

@login_required
def user_orders(request):
    user = User.objects.get(pk=request.user.id)
    order_groups = Order.objects.filter(user=user).order_by('-id')
    orders=[]
    for order in order_groups:
        order_items = Order_Item.objects.filter(order=order).all()
        new_order = {'order_group':order, 'orders':order_items}
        orders.append(new_order)
    context = {
        'orders':orders,
        'title': 'My Orders'
    }
    return render(request, 'pizza/user_orders.html', context=context)

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

@require_POST
def submit_order(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        order = Order(user_id=request.user.id, total_price=body['total_price'], address_id=body['address'])
        order.save()
        for item in body['orders']:
            item.setdefault('toppings','')
            order_item = Order_Item(order_id=order.id, food_id=item['foodid'], size=item['size'], price=item['price'], toppings=''.join(item['toppings']))
            order_item.save()
    print('redirect')
    return redirect('menu')
