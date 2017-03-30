$(document).ready(function() {
    // Initially hide error message
    $('#error_message').hide();

    $('#username').on("click", function() {
        $('#error_message').hide();
    });

    $('#password').on("click", function() {
        $('#error_message').hide();
    });

});

function login() {

      var data = $('#login_form').serialize()

    $.ajax({
            url: '/login/',
            type: 'POST',
            async: false,
            data: data,
            success: function(data){

                if (data.includes("login_form")){
                    console.log("Bad login")
                    $('#error_message').show();
                }else {
                    console.log("Good login");
                    location.reload();
                }


            }
       })



    return false;


}