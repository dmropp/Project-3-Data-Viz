var mapQueryURL = "http://127.0.0.1:5000/map_data";

// D3 call for map data
d3.json(mapQueryURL).then(function(data) { 
    createMarkers(data);
})

function createMarkers(crashData) {

    var crashMarkerArray = [];

    for (let i = 0; i < crashData.length; i++) {

        var lng = crashData[i].lng;
        var lat = crashData[i].lat; 

        // Create circle markers for each crash location with popup description. 
        var crashMarker = L.circle([lat, lng], { // https://stackoverflow.com/questions/43015854/large-dataset-of-markers-or-dots-in-leaflet
            color: "red",
            fillColor: "red",
            fillOpacity: 0.5,
            radius: 500
        }).bindPopup(`<b3>Location of Crash: ${crashData[i].hwy_name}</b3><br>
                      <b3>Date of Crash: ${crashData[i].date}</b3><br>
                      <b3>Type of Crash: ${crashData[i].crash_type_desc}</b3><br>
                      <b3>Severity of Crash: ${crashData[i].crash_severity}</b3><br>
                      <b3>Causes of Crash 1: ${crashData[i].crash_cause_1_desc}</b3><br>
                      <b3>Causes of Crash 1: ${crashData[i].crash_cause_2_desc}</b3><br>
                      <b3>Causes of Crash 1: ${crashData[i].crash_cause_3_desc}</b3><br>
                      <b3>Factors in Crash: ${crashData[i].crash_event_1_desc}</b3><br>
                      <b3>Factors in Crash: ${crashData[i].crash_event_2_desc}</b3><br>
                      <b3>Factors in Crash: ${crashData[i].crash_event_3_desc}</b3><br>`
                      );
        

        crashMarkerArray.push(crashMarker);
    }

    createMap(L.layerGroup(crashMarkerArray));
};

// Function to create map with marker layer
function createMap(crashLocations) {

    var streetmap = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    });  

    var map = L.map("map", {

        center: [43.521, -120.587], // http://www.cogeographica.com/?post=oregon-s-geographic-centers&tag=high-desert, referenced for center of Oregon
        zoom: 5,
        layers: [streetmap, crashLocations],
        preferCanvas: true // https://stackoverflow.com/questions/43015854/large-dataset-of-markers-or-dots-in-leaflet, referenced for how to improve performance on maps with thousands of markers
    });
};