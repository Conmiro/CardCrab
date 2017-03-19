
$( document ).ready(function() {
    changePage(1)
    loadCart()
});

$(":checkbox").click(function() {  changePage(1) } )

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

function addToCart(button, card_id) {

    var button = $(button)
    var before_text = button.text()

    var data = {'action': 'add', 'card_id': card_id}
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

function loadCart() {
 $.ajax({
            url: '/shopping_cart/',
            success: function(data){
                $('#cart_section').html(data)
                return false
            }
       })
}

function flipArt() {
    var oldArt = $('#art_preview').attr('src')
    var newArt = $('#flip').val()

    $('#art_preview').attr('src', newArt)
    $('#flip').val(oldArt)

    console.log(oldArt)
    console.log(newArt)

}


function submitFilters() {
    var data = $('#filter_form').serialize()
    $.ajax({
            url: '/search_body/',
            type: 'POST',
            data: data,
            success: function(data){
                $('#search_body').html(data)
                return false
            }
       })

    //$.post('/search_body/', $('#theForm').serialize())

}

$(document).keydown(function(e) {
    switch(e.which) {
        case 37: //left
        changePage($('#prevpage').val())
        break;

        case 39: //right
        changePage($('#nextpage').val())
        break;

        default:
        return;
    }

});

function changePage(pageNum) {
if (isNaN(pageNum)) return;
$('#page').val(pageNum)
submitFilters()
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