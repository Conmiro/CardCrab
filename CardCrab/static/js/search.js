
$( document ).ready(function() {
    changePage(1)
});

$(":checkbox").click(function() {  changePage(1) } )

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