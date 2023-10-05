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

var dashboardQueryURL = "http://127.0.0.1:5000/dashboard_data";

function init (data){

}

d3.json(dashboardQueryURL).then(function(data) { // https://stackoverflow.com/questions/53716527/request-data-from-front-end-d3-json-from-python-flask-backend, referenced for how to call flask data from javascript    

   console.log("Hello");
   console.log(data);
   const groupedYear = groupBy(data, 'year');
   console.log(groupedYear);

   let dropdownRow = d3.selectAll("#selDate");
   let years = Object.keys(groupedYear);
   console.log(years);


   for (let i = 0; i < years.length; i++) {
      let row = dropdownRow.append("option").text(`${years[i]}`);
   }
   init(years[0]);
});

d3.selectAll("#selDataset").on("change", optionChanged);

function optionChanged() {
    
   let dropdownMenu = d3.select("#selDataset");
   let dataset = dropdownMenu.property("value");

   // Function to filter sample data to select sample data for subject ID chosen in the dropdown menu
   function selectValue(selectedID) {
       return selectedID.id === dataset;
   }

   let yearData = years.filter(selectValue);

   init(yearData[0]); // Call function to update plotswith selected subject
}