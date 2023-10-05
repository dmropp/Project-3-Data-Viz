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

   const groupedYear = groupBy(data, 'year');
   //console.log(groupedYear);
   currentDataset = groupedYear;
   console.log(currentDataset);

   let dropdownRow = d3.selectAll("#selDate");
   let years = Object.keys(groupedYear);
   
   for (let i = 0; i < years.length; i++) {
      let row = dropdownRow.append("option").text(`${years[i]}`);
   }
   
   let year2016 = groupedYear[2016];
   let currentSelection = d3.select("#selDate");
   let currentYear = currentSelection.property("value");
   //console.log(currentYear);

   init(currentDataset[currentYear]);
});

d3.selectAll("#selDate").on("change", optionChanged);

function optionChanged() {
    
   let dropdownMenu = d3.select("#selDate");
   let dataset = dropdownMenu.property("value");

   //console.log(dataset);

   let yearData = currentDataset[dataset];
   init(yearData);
}

function init(data) {
   //console.log(data);

   let hwy_grouped = groupBy(data, "hwy_name");
   let highways = {}; // https://code.mu/en/javascript/book/prime/loops/objects-filling/, referenced for how to populate object with for loop
   for (let i = 0; i < Object.keys(hwy_grouped).length; i++){ 
      let name = Object.keys(hwy_grouped)[i];
      let count = Object.keys(hwy_grouped)[i].length;
      highways[name] = count;
   }
   //console.log(highways);

   // https://medium.com/@gmcharmy/sort-objects-in-javascript-e-c-how-to-get-sorted-values-from-an-object-142a9ae7157c, referenced for how to sort object
   let highways_sorted = Object.entries(highways).sort((a,b) => b[1] - a[1]); 
   //console.log(highways_sorted);

   let bar_x_data = [];
   let bar_y_data = [];
   for (let j = 0; j < highways_sorted.length; j++) {
      bar_x_data.push(highways_sorted[j][0]);
      bar_y_data.push(highways_sorted[j][1]);
   }

   let barChartData = [{
      x: bar_x_data.slice(0, 20),
      y: bar_y_data.slice(0, 20),
      type: "bar", 
      automargin: true
   }];

   let barChartLayout = {
    height: 800,
    width: 800, 
    title: "Top 10 Roadways for Animal Collisions", 
    xaxis: {
      title: "Roadway", 
      tickangle: -45,
      automargin: true
   },
   yaxis: {
      title: "# of Collisions"
   }
   };

   Plotly.newPlot("bar", barChartData, barChartLayout);

   let dateGrouped = groupBy(data, "date");
   //console.log(dateGrouped);

   //console.log(dateGrouped);

   let dateGroups = {};
   for (let k = 0; k < Object.keys(dateGrouped).length; k++){ 
      let date = Object.keys(dateGrouped)[k];
      let count = Object.values(dateGrouped)[k].length;
      dateGroups[date] = count;
   }

   //console.log(Object.keys(dateGroups).length);

   let plot_x_data = [];
   let plot_y_data = [];

   for (let l = 0; l < Object.keys(dateGroups).length; l++) {
      plot_x_data.push(Object.keys(dateGroups)[l]);
      plot_y_data.push(Object.values(dateGroups)[l]);
   }

   //console.log(plot_x_data);
   //console.log(plot_y_data);

   let lineChartData = [{
      x: plot_x_data,
      y: plot_y_data,
      type: "bar", 
      automargin: true
   }];

   let lineChartLayout = {
      height: 600,
      width: 800, 
      title: "Vehicle Collisions with Animals Over Time",
      xaxis: {
         tickangle: -45, 
         title: "Date"
      },
      yaxis: {
         title: "# of Collisions"
      }
   };
  
   Plotly.newPlot("plot", lineChartData, lineChartLayout);

   let severityGrouped = groupBy(data, "crash_severity_desc");
   
   console.log(severityGrouped);

   //console.log(dateGrouped);

   let severityGroups = {};
   for (let m = 0; m < Object.keys(severityGrouped).length; m++){ 
      let severity = Object.keys(severityGrouped)[m];
      let count = Object.values(severityGrouped)[m].length;
      severityGroups[severity] = count;
   }

   console.log(severityGroups);

   let pie_x_data = [];
   let pie_y_data = [];

   for (let n = 0; n < Object.keys(severityGroups).length; n++) {
      //console.log(Object.keys(severityGroups)[n]);
      pie_x_data.push(Object.keys(severityGroups)[n]);
      pie_y_data.push(Object.values(severityGroups)[n]);
   }

   console.log(pie_x_data);
   console.log(pie_y_data);

   // https://plotly.com/javascript/pie-charts/, referenced for how to create a pie chart
   let pieChartData = [{
      values: pie_y_data,
      labels: pie_x_data,
      type: "pie", 
      automargin: true,
      textinfo: "label+percent"
   }];

   let pieChartLayout = {
      height: 600,
      width: 600, 
      title: "Collisions by Severity"
   }

   Plotly.newPlot("pie", pieChartData, pieChartLayout);

}