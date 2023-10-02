//https://towardsdatascience.com/talking-to-python-from-javascript-flask-and-the-fetch-api-e0ef3573c451, add to readme for general project reference

var dashboardQueryURL = "http://127.0.0.1:5000/dashboard_data";

// D3 call for dashboard data
d3.json(dashboardQueryURL).then(function(data) { // https://stackoverflow.com/questions/53716527/request-data-from-front-end-d3-json-from-python-flask-backend, referenced for how to call flask data from javascript
    
    console.log("Hello");
    console.log(data);
});