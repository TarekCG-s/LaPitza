var items_in_cart = [];
var total_price = 0;
var food_item;
var popup_window;
var cart_item;
var selected_toppings = 0;
var selectable_toppings = 0;

function show_order_box(){
  let is_topping, small, large;
  if(this.dataset.toppings > 0){
    is_topping = true;
    selectable_toppings = this.dataset.toppings;
  }
  if(this.dataset.small > 0){
    small = this.dataset.small;
  }
  if(this.dataset.large > 0){
    large = this.dataset.large;
  }
  const content = popup_window({toppings:toppings, is_topping:is_topping, small:small, large:large, name:this.dataset.name, foodid:this.dataset.foodid});
  let div = document.createElement('div');
  div.id = 'pop-up';
  div.innerHTML = content;
  document.querySelector('body').append(div);
}

function submit_to_card() {

  var form = document.querySelector('#order-details');
  let item = {
    'name':form.dataset.name,
    'foodid':form.dataset.foodid,
  }
  for (var i = 0; i < form.length - 2; i++){
    if (form.elements[i].checked == true){
      if(i < 2){
        item['size'] = form.elements[i].value;
        item['price'] = form.elements[i].dataset.price;
      }
      else{
        if(!item['toppings']){
          item['toppings'] = []
        }
        item['toppings'].push(form.elements[i].value);
      }
    }
  }
  items_in_cart.push(item);
  close_popup();
  refresh_cart_items();
}

function close_popup() {
  document.querySelector('#pop-up').remove();
  selectable_toppings = 0;
  selected_toppings = 0;
  return false;
}

function select_topping(element){
  if(element.checked == true){
    if (selected_toppings >= selectable_toppings) {
      element.checked = false;
    }
    else{
      selected_toppings += 1;
    }
  }
  else {
    selected_toppings -= 1;
  }
}

function remove_from_cart(element){
  const index = element.dataset.index;
  items_in_cart.splice(index, 1);
  refresh_cart_items();
}

function refresh_cart_items(){
  let cart = document.querySelector('#cart');
  total_price = 0;
  cart.innerHTML='';
  if(items_in_cart.length > 0){
    for (var i = 0; i < items_in_cart.length; i++){
      const new_item = cart_item({name:items_in_cart[i]['name'], size:items_in_cart[i]['size'], price:items_in_cart[i]['price'], index_in_cart:i});
      let div = document.createElement('div');
      div.className += 'cart-item';
      div.innerHTML += new_item;
      cart.append(div);
      total_price += parseFloat(items_in_cart[i]['price']);
    }
    let total = document.createElement('h6');
    total.innerHTML = 'Total : ' + total_price;
    cart.append(total);
    let submit = document.createElement('button');
    submit.innerHTML = 'Order Now';
    cart.append(submit);
  }
}
