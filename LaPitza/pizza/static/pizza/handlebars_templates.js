document.addEventListener('DOMContentLoaded', () =>{

  food_item = Handlebars.compile(`<div class="item food-item" data-type="{{type}}" data-foodid="{{foodid}}" data-name="{{type}} - {{name}}" data-small="{{small}}"
   data-large="{{large}}" data-toppings="{{toppings}}">
        <h6> {{name}} </h6>
        <h6> {{small}}$ </h6>
        <h6> {{large}}$ </h6>
      </div>`);

  popup_window = Handlebars.compile(`<div>
    <form id="order-details" data-name ="{{name}}" data-foodid ="{{foodid}}" data-small="{{small}}" data-large="{{large}}">
      <p>Please select size:</p>
      {{#if small}}
        <input type="radio" name="size" value="small" data-size="small" data-price="{{small}}" checked> Small - {{small}}$
      {{/if}}
      {{#if large}}
        <input type="radio" name="size" value="large" data-size="large" data-price="{{large}}" checked> Large {{large}}$
      {{/if}}

      {{#if is_topping}}
        <legend>Select your topping?</legend>
        {{#each toppings}}
          <input type="checkbox" name="topping" value="{{this}}" onclick="select_topping(this)">{{this}}
        {{/each}}
      {{/if}}
      <br>
      <button name="button" onclick="submit_to_card()">Add to card</button>
      <button id="cancel-btn" onclick="close_popup()">Cancel</button>
    </form>
  </div>`);

  cart_item = Handlebars.compile(`
    <li><span>{{name}} {{size}} - {{price}}$ <button data-index={{index_in_cart}} onclick="remove_from_cart(this)">Remove</button></li>
    `);
});
