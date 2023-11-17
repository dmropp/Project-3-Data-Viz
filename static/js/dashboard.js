// Function to group data by a desired value
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

var currentDataset; // Variable to store dataset to be passed to each function

// Function to call data and populate dropdown menu with years
d3.json(dashboardQueryURL).then(function(data) { // https://stackoverflow.com/questions/53716527/request-data-from-front-end-d3-json-from-python-flask-backend, referenced for how to call flask data from javascript    

   const groupedYear = groupBy(data, 'year');
   currentDataset = groupedYear;

   let dropdownRow = d3.selectAll("#selDate");
   let years = Object.keys(groupedYear);
   
   for (let i = 0; i < years.length; i++) {
      let row = dropdownRow.append("option").text(`${years[i]}`);
   }
   
   let year2016 = groupedYear[2016];
   let currentSelection = d3.select("#selDate");
   let currentYear = currentSelection.property("value");

   init(currentDataset[currentYear]);
});

d3.selectAll("#selDate").on("change", optionChanged); // Method called when new value is selected in the dropdown menu

// Function to assign value selected in the dropdown menu to a variable, and pass the variable to update plots
function optionChanged() {
    
   let dropdownMenu = d3.select("#selDate");
   let dataset = dropdownMenu.property("value");

   let yearData = currentDataset[dataset];
   init(yearData);
}

// Function to build plots
function init(data) {

   // Group by highway name and add to object where highway name is the key and the count of crashes on that highway is the value
   let hwy_grouped = groupBy(data, "hwy_name");
   let highways = {}; // https://code.mu/en/javascript/book/prime/loops/objects-filling/, referenced for how to populate object with for loop
   for (let i = 0; i < Object.keys(hwy_grouped).length; i++){ 
      let name = Object.keys(hwy_grouped)[i];
      let count = Object.keys(hwy_grouped)[i].length;
      highways[name] = count;
   }

   // https://medium.com/@gmcharmy/sort-objects-in-javascript-e-c-how-to-get-sorted-values-from-an-object-142a9ae7157c, referenced for how to sort object
   let highways_sorted = Object.entries(highways).sort((a,b) => b[1] - a[1]); 

   // Push highway names and counts to arrays for use in the bar chart
   let bar_x_data = [];
   let bar_y_data = [];
   for (let j = 0; j < highways_sorted.length; j++) {
      bar_x_data.push(highways_sorted[j][0]);
      bar_y_data.push(highways_sorted[j][1]);
   }

   let barChartData = [{
      x: bar_x_data.slice(0, 20),
      y: bar_y_data.slice(0, 20),
      type: "bar"
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
      title: "# of Collisions",
      automargin: true
   }
   };

   let barChartConfig = {responsive: true}

   Plotly.newPlot("bar", barChartData, barChartLayout, barChartConfig);

   // Group by crash date and add to object where the key is the date and the value is the number of crashes on that date
   let dateGrouped = groupBy(data, "date");
   let dateGroups = {};
   for (let k = 0; k < Object.keys(dateGrouped).length; k++){ 
      let date = Object.keys(dateGrouped)[k];
      let count = Object.values(dateGrouped)[k].length;
      dateGroups[date] = count;
   }

   // Push dates and counts to arrays for use in the bar chart plotting collisions over time
   let plot_x_data = [];
   let plot_y_data = [];
   for (let l = 0; l < Object.keys(dateGroups).length; l++) {
      plot_x_data.push(Object.keys(dateGroups)[l]);
      plot_y_data.push(Object.values(dateGroups)[l]);
   }

   let timeseriesData = [{
      x: plot_x_data,
      y: plot_y_data,
      type: "bar"
   }];

   let timeseriesLayout = {
      height: 600,
      width: 800, 
      title: "Vehicle Collisions with Animals Over Time",
      xaxis: {
         tickangle: -45, 
         title: "Date",
         automargin: true
      },
      yaxis: {
         title: "# of Collisions",
         automargin: true
      }
   };

   let timeseriesConfig = {responsive: true}
  
   Plotly.newPlot("plot", timeseriesData, timeseriesLayout, timeseriesConfig);

   // Group by crash severity and add to object where the key is the crash severity and the value is the related number of crashes by severity category
   let severityGrouped = groupBy(data, "crash_severity_desc");
   let severityGroups = {};
   for (let m = 0; m < Object.keys(severityGrouped).length; m++){ 
      let severity = Object.keys(severityGrouped)[m];
      let count = Object.values(severityGrouped)[m].length;
      severityGroups[severity] = count;
   }

   // Push severity category and crash counts to arrays for use in the pie chart plotting % of crashes by severity
   let pie_x_data = [];
   let pie_y_data = [];
   for (let n = 0; n < Object.keys(severityGroups).length; n++) {
      pie_x_data.push(Object.keys(severityGroups)[n]);
      pie_y_data.push(Object.values(severityGroups)[n]);
   }

   // https://plotly.com/javascript/pie-charts/, referenced for how to create a pie chart
   let pieChartData = [{
      values: pie_y_data,
      labels: pie_x_data,
      type: "pie", 
      textinfo: "label+percent"
   }];

   let pieChartLayout = {
      height: 600,
      width: 600, 
      title: "Collisions by Severity",
      automargin: true
   }

   let pieChartConfig = {responsive: true}

   Plotly.newPlot("pie", pieChartData, pieChartLayout, pieChartConfig);
}