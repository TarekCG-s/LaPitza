var toppings;
document.addEventListener('DOMContentLoaded', () =>{
  get_toppings_ajax();
  get_food_ajax(1);
  document.querySelectorAll('.category').forEach(category => {
    category.onclick = () =>{
      const categoryID = category.dataset.category;
      get_food_ajax(categoryID);
    }
  });
});

function get_food_ajax(categoryID) {
  const xhr = new XMLHttpRequest();
  xhr.open('GET', `food/${categoryID}`);
  xhr.onload = () =>{
    const response = JSON.parse(xhr.responseText);
    var items = document.querySelector('#items');
    items.innerHTML = '';
    response.forEach(add_item);
  }
  xhr.send();

  function add_item(item){
    const content = food_item({name: item['name'], type: item['type'], small: item['small'], large:item['large'], foodid:item['id'], toppings:item['toppings']});
    var items = document.querySelector('#items');
    items.innerHTML += content;
    document.querySelectorAll('.food-item').forEach(item => {
      item.onclick = show_order_box;
    });
  }
}

function get_toppings_ajax() {
  const xhr = new XMLHttpRequest();
  xhr.open('GET', 'toppings');
  xhr.onload = () =>{
    toppings = JSON.parse(xhr.responseText);
  }
  xhr.send();
}
