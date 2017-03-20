
$(document).ready(function() {

    var path = $('#current_path').val()
    console.log(path)
    if (path=="/"){
        $('#home_label').addClass('active')
    }else if (path=="/search/") {
        $('#cards_label').addClass('active')
    }

})