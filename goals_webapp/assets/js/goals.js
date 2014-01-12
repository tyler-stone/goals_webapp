$(document).ready(function(){
	$('.goal_detailview').hide();
})

$('.goal_flag').click(function() {
	alert("GOAL FLG");
});

$('.goal_minview').click(function() {
	$(this).siblings('.goal_detailview').slideDown();
});

$('.close').click(function() {
	$(this).parents('.goal_detailview').slideUp();
});