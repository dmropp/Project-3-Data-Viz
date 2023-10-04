//https://towardsdatascience.com/talking-to-python-from-javascript-flask-and-the-fetch-api-e0ef3573c451, add to readme for general project reference

// from https://www.tutorialspoint.com/most-efficient-method-to-groupby-on-an-array-of-objects-in-javascript
function groupBy(objectArray, property) {
    return objectArray.reduce((acc, obj) => {
       const key = obj[property];
       if (!acc[key]) {
          acc[key] = [];
       }
       // Add object to list for given key's value
       acc[key].push(obj);
       return acc;
    }, {});
}

function justYear (crashData){
    for (let i = 0; i < crashData.length; i++) {

    }
    crashMarkerArray.push(crashMarker)
}
var dashboardQueryURL = "http://127.0.0.1:5000/dashboard_data";

// D3 call for dashboard data
d3.json(dashboardQueryURL).then(function(data) { // https://stackoverflow.com/questions/53716527/request-data-from-front-end-d3-json-from-python-flask-backend, referenced for how to call flask data from javascript    
    console.log("Hello");
    const newArray = justYear(data);
    const groupedYear = groupBy(newArray, 'date');
    console.log(groupedYear);
});