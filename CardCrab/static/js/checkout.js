$ (document).ready(function() {

        loadShippingBilling()
        loadCart()



})


function updateAll() {
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
                    loadCart()

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
                        }
                        loadCart()

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

            }
       })
}
