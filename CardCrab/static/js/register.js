$(document).ready(function() {
    $('#username_error').hide();
    $('#password_error').hide();




})

function register() {

    $('#username_error').hide();
    $('#password_error').hide();


    var data = $('#register_form').serialize()

    $.ajax({
            url: '/register/',
            type: 'POST',
            data: data,
            success: function(data){
                if (data != 'SUCCESS'){
                console.log(data)
                    errors = JSON.parse(data)
                    for (i = 0; i < errors.length; i++){
                        console.log(errors[i])
                        if (errors[i] == 'USER_EXISTS')
                                $('#username_error').show();
                        else if (errors[i] == 'PASSWORD_MISMATCH')
                                $('#password_error').show();
                    }

                } else {
                $('#user_modal_body').html('Account created!')
                }


            }
       })





}