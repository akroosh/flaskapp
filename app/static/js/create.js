$(function() {
    $('#btn-create').click(function() {
        $.ajax({
            url: '/movies/create_movie',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});
