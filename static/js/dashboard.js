//https://towardsdatascience.com/talking-to-python-from-javascript-flask-and-the-fetch-api-e0ef3573c451, add to readme for general project reference

var dashboardQueryURL = "http://127.0.0.1:5000/api/v1.0/dashboard";
//var dashboardQueryURL = "http://localhost:5000/api/v1.0/dashboard";
//var dashboardQueryURL = "/api/v1.0/dashboard";

// D3 call for map viz
d3.json(dashboardQueryURL).then(function(data) { // https://stackoverflow.com/questions/53716527/request-data-from-front-end-d3-json-from-python-flask-backend, referenced for how to call flask data from javascript
    //console.log(data);
    //createMarkers(data) 
    console.log("Hello");
    console.log(data);
});

//console.log("hello")

// fetch(dashboardQueryURL, {mode: "no-cors"}).then(function(data) {
//     console.log(data);
// });