
$(document).ready(function() {


    var path = $('#current_path').val()
    console.log(path)
    if (path=="/"){
        $('#home_label').addClass('active')
    }else if (path=="/search/") {
        $('#cards_label').addClass('active')
    }

})


function open_register() {


$('#user_modal_title').text('Register')
$('#user_modal').modal('show');
var data = { }
    $.ajax({
            url: '/register/',
            type: 'POST',
            data: data,
            success: function(data){
                $('#user_modal_body').html(data)

            }
       })


}

function open_login() {
$('#user_modal_title').text('Login')
$('#user_modal').modal('show');

var data = { }
    $.ajax({
            url: '/login/',
            type: 'POST',
            data: data,
            success: function(data){
                $('#user_modal_body').html(data)

            }
       })


}

function logout() {

    var data = { }
    $.ajax({
            url: '/logout/',
            async: false,
            data: data,
            success: function(data){
                window.location.replace("/");

            }
       })

}


function open_sell_card() {



    var data = { };
    $('#user_modal_title').text('Add Card for Sale')
    $('#user_modal').modal('show');
        $.ajax({
            url: '/add_card/',
            data: data,
            success: function(data){
               $('#user_modal_body').html(data)
               $('#card_added').hide();


            }
       })


}

function add_card(button) {
    $('#add_card_submit').addClass('disabled');
    $('#card_added').show();


     setTimeout(function() {
                 window.location.replace("/my_store/");
            }, 2500)

    return false


}