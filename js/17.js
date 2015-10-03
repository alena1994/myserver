$(function(){
	$(".search-control .search-icon").click(function (e) {
		$(this).parent().find(".searchform").toggle();
		if($(this).hasClass("active")){
			$(this).removeClass("active");
		} else {
			$(this).addClass("active");
		}
		e.preventDefault();
	});
});