// 1. Resize content height to fit between footer and header
// 2. Distribute buttons evenly
$(document).delegate('[data-role=page]', 'pageshow', function () {
	// 1
	var windowHeight = $(window).height();
	var headerHeight = $(this).find('[data-role="header"]').height();
	var footerHeight = $(this).find('[data-role="footer"]').height();
    var buttonAreaHeight = (windowHeight - headerHeight - footerHeight - 30);
    $(this).height($(window).height()).find('[data-role="content"]').height(buttonAreaHeight);
    // 2
    var buttonList = $(this).find('.vertical_button');
    var buttonHeight = $(buttonList[0]).height();
    var buttonSpace = buttonAreaHeight / buttonList.length;
    for (var i = 0; i < buttonList.length; ++i) {
    	var y = headerHeight + (i * buttonSpace) + (buttonSpace * 0.5) - (buttonHeight * 0.5);
    	$(buttonList[i]).offset({top: y});
    }
});