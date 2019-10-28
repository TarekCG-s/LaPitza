document.addEventListener('DOMContentLoaded', () =>{

  // food_item = Handlebars.compile(`<div class="item food-item" data-type="{{type}}" data-foodid="{{foodid}}" data-name="{{type}} - {{name}}" data-small="{{small}}"
  //  data-large="{{large}}" data-toppings="{{toppings}}">
  //       <h6> {{name}} </h6>
  //       <h6> {{small}}$ </h6>
  //       <h6> {{large}}$ </h6>
  //     </div>`);
  food_item = Handlebars.compile(`<div class="row justify-content-md-center align-items-center item food-item"
        data-type="{{type}}" data-foodid="{{foodid}}" data-name="{{type}} - {{name}}" data-small="{{small}}"
         data-large="{{large}}" data-toppings="{{toppings}}">
          <div class="col-6">
            <p>{{name}}</p>
          </div>
          <div class="col">
            <p>{{small}}$</p>
          </div>
          <div class="col">
            <p>{{large}}$</p>
          </div>
        </div>`);

  popup_order_box = Handlebars.compile(`<div>
    <form id="order-details" data-name ="{{name}}" data-foodid ="{{foodid}}" data-small="{{small}}" data-large="{{large}}">
      <p>Please select size:</p>
      {{#if small}}
        <div class="input-group">
          <div class="input-group-prepend">
            <div class="input-group-text">
              <input type="radio" name="size" value="small" data-size="small" data-price="{{small}}" checked> Small - {{small}}$
            </div>
          </div>
        </div>
      {{/if}}
      {{#if large}}
        <div class="input-group">
          <div class="input-group-prepend">
            <div class="input-group-text">
                <input type="radio" name="size" value="large" data-size="large" data-price="{{large}}" checked> Large {{large}}$
            </div>
          </div>
        </div>
      {{/if}}

      {{#if is_topping}}
        <legend>Select your topping?</legend>
        <div class="input-group">
          {{#each toppings}}
            <div class="input-group-text">
              <input type="checkbox" name="topping" value="{{this}}" onclick="select_topping(this)">{{this}}
            </div>
          {{/each}}
        </div>
      {{/if}}
      <br>
      <button class="btn btn-warning" name="button" type="submit" onclick="submit_to_card()">Add to card</button>
      <button class ="btn btn-danger" id="cancel-btn" onclick="close_popup()">Cancel</button>
    </form>
  </div>`);

  popup_confirm_box = Handlebars.compile(`<div class="confirm-order-box">
    <form  id="confirm-order">
      <h5>Are you sure you want to submit your order?</h5>
      <br>
      <div class="text-center">
        <button class="btn btn-warning" name="button" type="submit" onclick="submit_order()">Yes</button>
        <button class ="btn btn-danger" id="cancel-btn" onclick="close_popup()">No</button>
      </div>
    </form>
  </div>`);

  cart_item = Handlebars.compile(`
    <li><span>{{name}} {{size}} - {{price}}$ <button class="btn btn-danger" data-index={{index_in_cart}} onclick="remove_from_cart(this)">Remove</button></li>
  `);

  confirm_order = Handlebars.compile(`<div>
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
      <button name="button" type="submit" onclick="submit_to_card()">Add to card</button>
      <button id="cancel-btn" onclick="close_popup()">Cancel</button>
    </form>
  </div>`);
});
