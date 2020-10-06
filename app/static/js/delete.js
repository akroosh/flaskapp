function Delete(elm) {
    $.ajax({
        url: '/movies/$(elm.slug)/delete',

        type: 'POST',
        success: function(res) {
            console.log(res);
        },
        error: function(error) {
            console.log(error);
        }
    });
}