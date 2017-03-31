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