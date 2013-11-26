/*javascript needed for google maps rendering */

/*var latlng= new google.maps.LatLng(document.getElementById("user_loc").innerHTML);*/
var map, pointarray, heatmap;
/*
var gradeData = [
    new google.maps.LatLng(man_grades.geocodes)]; */

console.log(man_grades.geocodes);



//var latlng = new google.maps.LatLng(40.72078, -74.001119);
/*graffiti_locations passed in as graffiti_loc*/

function initialize(){
    var mapOptions = {
          center: latlng,
          zoom: 15
    }

    var map = new google.maps.Map(document.getElementById("map-canvas"),
            mapOptions);

    /*adds a marker to the map for the user's location*/
    var marker = new google.maps.Marker({
        position: latlng,
        title: "user location",
        map: map
    });
    /*add marker for graffiti locations */
    var image = {
        url:'http://www.alispagnola.com/Free/spraypaint2.jpg',
        scaledSize: new google.maps.Size(32, 32),
        origin: new google.maps.Point(0,0)
    };


}


google.maps.event.addDomListener(window, 'load', initialize);
