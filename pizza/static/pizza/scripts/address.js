document.addEventListener('DOMContentLoaded', () =>{
  username = document.querySelector('#username').value;
  items_in_cart = JSON.parse(localStorage.getItem(username))['items'];
  total_price = JSON.parse(localStorage.getItem(username))['total'];
  console.log(items_in_cart);
});
