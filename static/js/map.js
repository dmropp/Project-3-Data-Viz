var mapQueryURL = "http://127.0.0.1:5000/map_data";

// Perform a GET request to the query URL/
d3.json(mapQueryURL).then(function (data) {
  // Once we get a response, send the data.features object to the createFeatures function.
  console.log(data)
  createFeatures(data.features);
});

function createFeatures(earthquakeData) {

  // Define a function that we want to run once for each feature in the features array.
  // Give each feature a popup that describes the place and time of the earthquake.
  function onEachFeature(feature, layer) {
    layer.bindPopup(`<h3>${feature.properties.place}</h3><hr><p>${new Date(feature.properties.time)}</p>`);
  }

  // Create a GeoJSON layer that contains the features array on the earthquakeData object.
  // Run the onEachFeature function once for each piece of data in the array.
  // this is where the ColorPick and MarkerSize functions will likely come into play
  var earthquakes = L.geoJSON(earthquakeData, {
    onEachFeature: onEachFeature,
    
    //use pointToLayer to alter the markers
    pointToLayer: function (feature, latlng) {
        var markers = {
            radius: MarkerSize(feature.properties.mag),
            fillColor: ColorPick(feature.geometry.coordinates[2]),
            fillOpacity: 0.6,
            color: "black",
            stroke: true,
            weight: 0.5
          }
        return L.circleMarker(latlng, markers);
    }
  });
  // Send our earthquakes layer to the createMap function/
  createMap(earthquakes);
}

function createMap(earthquakes) {

  // Create the base layers.
  var street = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  });

  // Create an overlay object to hold our overlay.

  // Create our map, giving it the streetmap and earthquakes layers to display on load.
  var myMap = L.map("map", {
    center: [
      37.09, -95.71
    ],
    zoom: 5,
    layers: [street, earthquakes]
  });
  
  var legend = L.control({position: "bottomright"});
  legend.onAdd = function() {
    var div = L.DomUtil.create("div", "info legend"),
    depth = [-10, 10, 30, 50, 70, 90];

    div.innerHTML += "<h3 style='text-align: center'>Depth</h3>"

    for (var i = 0; i < depth.length; i++) {
      div.innerHTML +=
      '<i style="background:' + ColorPick(depth[i] + 1) + '"></i> ' + depth[i] + (depth[i + 1] ? '&ndash;' + depth[i + 1] + '<br>' : '+');
    }
    return div;
  };
  legend.addTo(myMap)  
}