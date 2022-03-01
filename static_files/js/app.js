$('#playerModal').on('show.bs.modal', function(event) {
    var button = $(event.relatedTarget)
    var giveawayId = button.data('whatever')

    var $modal = $(this)
    $modal.find('.modal-body #giveaway_id').val(giveawayId)
})


$('#playerverifybtn').click(function(e) {

    e.preventDefault();

    $('#player_verify_form').submit();

});





$('.timer-span').startTimer({
    elementContainer: "span"
});