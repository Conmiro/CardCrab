$ (document).ready(function() {

        loadShippingBilling()
        loadCart()



})

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
