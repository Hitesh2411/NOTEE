
$(document).ready(function () {
    $('.note-btn').click(function () {
        var title = $(this).data('title');
        var notes = $(this).data('notes');
        
        $('#title').val(title);
        $('#description').val(notes);

        console.log(title);
        console.log(description)
    });
});
