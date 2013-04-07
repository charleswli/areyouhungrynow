/*global google, Constants, Helpers*/

/**
 * Super hacky code to load the business information page
 **/
$(document).delegate('#business', 'pageshow', function () {
  $(document).ready(function () {
    var yelpInfo;

    // get info from server
    $.ajax({
      url : Constants.HOST_ENDPOINT + Constants.Business.BusinessInfo + 'sushi-maki-seattle',
      dataType: 'json',
      success : function (data) {
        yelpInfo = data;
        renderPage(data);
      },
      error : function () {
        console.log('fake it like a boss');
        renderPage(backupYelpInfo);
      }
    });

    Handlebars.registerHelper('displayList', function (list) {
      var string = "";

      for (var listItem in list) {
        string += list[listItem] + "<br/>";
      }

      return new Handlebars.SafeString(string);
    });

    var backupYelpInfo = {
      "categories": [ ["Sushi Bars", "sushi"] ],
      "display_phone": "+1-206-264-0725",
      "distance": 226.73779308489082,
      "id": "sushi-maki-seattle",
      "image_url": "http://s3-media3.ak.yelpcdn.com/bphoto/XftVke2UTJ3CC40Vb_5OHQ/ms.jpg",
      "is_claimed": false,
      "is_closed": false,
      "location": {
        "address": ["1633 Bellevue Ave"],
        "city": "Seattle",
        "coordinate": {
            "latitude": 47.6161678,
            "longitude": -122.3269584
          },
          "country_code": "US",
          "cross_streets": "Pine St & Olive St",
          "display_address": ["1633 Bellevue Ave", "(b/t Pine St & Olive St)", "Capitol Hill", "Seattle, WA 98122"],
          "geo_accuracy": 8,
          "neighborhoods": ["Capitol Hill"],
          "postal_code": "98122",
          "state_code": "WA"
        },
        "mobile_url": "http://m.yelp.com/biz/sushi-maki-seattle",
        "name": "Sushi Maki",
        "phone": "2062640725",
        "rating": 4.0,
        "rating_img_url": "http://s3-media4.ak.yelpcdn.com/assets/2/www/img/c2f3dd9799a5/ico/stars/v1/stars_4.png",
        "rating_img_url_large": "http://s3-media2.ak.yelpcdn.com/assets/2/www/img/ccf2b76faa2c/ico/stars/v1/stars_large_4.png",
        "rating_img_url_small": "http://s3-media4.ak.yelpcdn.com/assets/2/www/img/f62a5be2f902/ico/stars/v1/stars_small_4.png",
        "review_count": 169,
        "snippet_image_url": "http://s3-media3.ak.yelpcdn.com/photo/dUfdP1VpZKhGAPo5W0C5Eg/ms.jpg",
        "snippet_text": "I stopped in to Sushi Maki the other day, right before I was about to begin a take-home final exam for a class. I got a spicy tuna roll and a salmon roll...",
        "url": "http://www.yelp.com/biz/sushi-maki-seattle"
      };

      // initialize the google maps
    function initializeMap() {
        var mapOptions = {
          center: new google.maps.LatLng(yelpInfo.location.coordinate.latitude, yelpInfo.location.coordinate.longitude),
          zoom: 16,
          mapTypeId: google.maps.MapTypeId.ROADMAP
        };

        var map = new google.maps.Map($("#map-canvas")[0], mapOptions);
        var marker = new google.maps.Marker({
          position: new google.maps.LatLng(yelpInfo.location.coordinate.latitude, yelpInfo.location.coordinate.longitude),
          map: map
        });
      }

    function renderHeader(yelpInfo) {
      var source = $('#pageHeader').html(),
          template = Handlebars.compile(source);

      $('#business').prepend(template(yelpInfo));
    }

    function renderPage() {
      Helpers.renderTemplate($('#businessDetailsTemplate'), $('#business-details'), yelpInfo);
      Helpers.renderTemplate($('#businessInfoTemplate'), $('#business-info'), yelpInfo);
      renderHeader(yelpInfo);
      initializeMap();
    }

    return {
      renderPage : renderPage
    };
  });
});
