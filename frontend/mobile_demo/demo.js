$(document).ready(function () {
  function getWindowPosition(relativePosition) {
    return ($(window).width() * relativePosition - wid / 4) + 'px';
  }

  $('#addPhone').css({
    left: $(document).width() - 75,
    top: $(document).height() - 75
  });

  var wid = 879;
  var hei = 1697;
  $('#iphone').css('left', getWindowPosition(0.5));

  $('#addPhone').click(function () {
    $('#iphone').animate({
      left: getWindowPosition(0.66),
      easing: 'easeOutExpo'
    }, {
      complete : function () {
          $('#iphone2').animate({
            left: getWindowPosition(0.33),
            easing: 'easeOutExpo'
          });
        }
    });
    $('#addPhone').hide();
  });
});
