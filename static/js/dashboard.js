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

var currentDataset;

d3.json(dashboardQueryURL).then(function(data) { // https://stackoverflow.com/questions/53716527/request-data-from-front-end-d3-json-from-python-flask-backend, referenced for how to call flask data from javascript    

   // console.log("Hello");
   // console.log(data);
   const groupedYear = groupBy(data, 'year');
   console.log(groupedYear);
   currentDataset = groupedYear;
   console.log(currentDataset);

   let dropdownRow = d3.selectAll("#selDate");
   let years = Object.keys(groupedYear);
   //console.log(years);



   for (let i = 0; i < years.length; i++) {
      let row = dropdownRow.append("option").text(`${years[i]}`);
   }
   
   let year2016 = groupedYear[2016];
   // console.log(year2016);

   // for (let j = 0; j < year2016.length; j++){
   //    let row = year2016[j];
   //    console.log(row);
   // }
   init(currentDataset[2016]);
});

d3.selectAll("#selDate").on("change", optionChanged);

function optionChanged() {
    
   let dropdownMenu = d3.select("#selDate");
   let dataset = dropdownMenu.property("value");

   console.log(dataset);

   let yearData = currentDataset[dataset];
   init(yearData);
}

function init(data) {
   console.log(data);

   let hwy_grouped = groupBy(data, "hwy_name");
   let highways = {};
   for (let i = 0; i < Object.keys(hwy_grouped).length; i++){
      let name = Object.keys(hwy_grouped)[i];
      let count = Object.keys(hwy_grouped)[i].length;
      highways[name] = count;
   }
   console.log(highways);

   let x_data = Object.values(highways);
   let y_data = Object.keys(highways);

   let barChartData = [{
      x: x_data.slice(0, 10).reverse(),
      y: y_data.slice(0, 10).reverse(),
      type: "bar",
      orientation: "h"
   }];

   let barChartLayout = {
    height: 600,
    width: 600
   };

   Plotly.newPlot("bar", barChartData, barChartLayout);
   let yearlyCrashes = {};

   for (let i = 0; i < Object.keys(data).length; i++){
     let name2 = Object.keys(data)[i];
     let count2 = Object.keys(data)[i].length;
     yearlyCrashes[name2] = count2;
   }

   let x_data2 = Object.values(yearlyCrashes);
   let y_data2 = Object.keys(yearlyCrashes);

   let lineChartData = [{
      x: x_data2,
      y: y_data2,
      type: "plot"
   }];

   let lineChartLayout = {
      height: 600,
      width: 600
     };
  
     Plotly.newPlot("plot", lineChartData, lineChartLayout);
}
