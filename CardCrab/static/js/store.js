$ (document).ready(function() {

        loadStore()



})


function loadStore() {

       $.ajax({
            url: '/my_store_body/',
            success: function(data){

                $('#my_store_body').html(data)

            }
       })

}


function removeFromStore(card_id) {

           var data = {'action': 'remove', 'card_id': card_id}
           $.ajax({
            url: '/my_store/',
            type: 'POST',
            data: data,
            success: function(data){

                loadStore()

            }
           })



}

function updateAll(button) {

    $('.qty-input').each(function() {
        var id = $(this).attr('id')
        var qty = $(this).val()
        card_id = /qty-(\d+)/.exec(id)[1]

        var data = data = {'action': 'set', 'card_id': card_id, 'quantity': qty}
        $.ajax({
                url: '/my_store/',
                type: 'POST',
                data: data,
                success: function(data){
                    if (data != 'Set!') {
                        console.log("Not enough...")
                    }
                    $(button).text('Done!')

                    setTimeout(function() {
                            loadStore()
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
                    url: '/my_store/',
                    type: 'POST',
                    data: data,
                    success: function(data){
                        if (data != 'Set!') {
                            console.log("Not enough...")
                        }
                        textbox.css('background-color','palegreen');

                        setTimeout(function() {
                            loadStore()
                        }, 500)

                    }
               })

        }

}