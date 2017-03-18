

$(document).keydown(function(e) {
    console.log(e.which)
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
    console.log(pageNum)
    $("#page").val(pageNum)
    document.getElementById("change_page_form").submit()


}