$ (document).ready(function() {

        loadShippingBilling()
        loadCart()

})


function updateAll(button) {
    $('.qty-input').each(function() {
        var id = $(this).attr('id')
        var qty = $(this).val()
        card_id = /qty-(\d+)/.exec(id)[1]

        var data = data = {'action': 'set', 'card_id': card_id, 'quantity': qty}
        $.ajax({
                url: '/shopping_cart/',
                type: 'POST',
                data: data,
                success: function(data){
                    if (data != 'Set!') {
                        console.log("Not enough...")
                    }
                    $(button).text('Done!')

                    setTimeout(function() {
                            loadCart()
                        }, 500)

                }
           })

        })
}

function updateQuantity(e, textBox, card_id) {

        if (e.which == 13) {
            //Disable textbox to prevent multiple submit
            var textbox = $(textBox)
            var quantity = textbox.val()

            var data = data = {'action': 'set', 'card_id': card_id, 'quantity': quantity}
            $.ajax({
                    url: '/shopping_cart/',
                    type: 'POST',
                    data: data,
                    success: function(data){
                        if (data != 'Set!') {
                            console.log("Not enough...")
                            textbox.css('background-color','red');

                        }else {
                            textbox.css('background-color','palegreen');
                        }


                        setTimeout(function() {
                            loadCart()
                        }, 500)

                    }
               })

        }

}


function removeFromCart(card_id) {

    var data = data = {'action': 'remove', 'card_id': card_id}
    $.ajax({
            url: '/shopping_cart/',
            type: 'POST',
            data: data,
            success: function(data){
                loadCart()
            }
       })
}

function loadShippingBilling() {
        $.ajax({
            url: '/shipping_billing_body/',
            success: function(data){
                $('#shipping_billing_body').html(data)

            }
       })
}

function loadCart() {
        $.ajax({
            url: '/cart_body/',
            success: function(data){
                $('#cart_body').html(data)
                $('[data-toggle="tooltip"]').tooltip();


            }
       })
}


function addToCart(button, card_id) {

    var button = $(button)
    var before_text = button.text()

    var quantity = 1 //set to textbox value later...

    var data = {'action': 'add', 'card_id': card_id, 'quantity': quantity}
    $.ajax({
            url: '/shopping_cart/',
            type: 'POST',
            data: data,
            success: function(data){
                loadCart()
                button.text(data)
                button.prop('disabled', true)
                setTimeout(function() {
                    button.text(before_text)
                    button.prop('disabled', false)
                }, 1000)

            }
       })

}

function detailView(card_id, card_name, chosen_id) {

$('#detail_modal_title').text(card_name)
$('#detail_modal').modal('show');

    data = {'card_id': card_id, 'chosen_id': chosen_id}
    $.ajax({
            url: '/card_details/',
            type: 'POST',
            data: data,
            success: function(data){
                $('#detail_modal_body').html(data)
                return false
            }
       })



}

function submitOrder() {
$('#order_modal').modal('show');
    $.ajax({
            url: '/submit_order/',
            success: function(data){
            }
       })

      loadCart();

}

function emptyCart() {

    var data = {'action': 'clear'}
    $.ajax({
            url: '/shopping_cart/',
            type: 'POST',
            data: data,
            success: function(data){
                loadCart()


            }
       })

}

function clearShipping() {
      $('#shipping_modal').find('input:text').val('');
      $('#shipping_modal').find('select').val('');


}


function clearBilling() {
      $('#billing_modal').find('input:text').val('');
      $('#billing_modal').find('input[type="number"]').val('');
      $('#billing_modal').find('select').val('');


}