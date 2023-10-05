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
   console.log(groupedYear);
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
   console.log(currentYear);
   //console.log(currentDataset[currentYear]);

   init(currentDataset[currentYear]);
});

d3.selectAll("#selDate").on("change", optionChanged);

function optionChanged() {

   console.log("hello");
   
   let dropdownMenu = d3.select("#selDate");
   let dataset = dropdownMenu.property("value");

   console.log(dataset);

   let yearData = currentDataset[dataset];
   console.log(yearData);
   init(yearData);
}

// function init(data) {
//    console.log(data);
// }

function init(data) {
    
   let hwy_grouped = groupBy(data, "hwy_name");
   let highways = {};
   for (let i = 0; i < Object.keys(hwy_grouped).length; i++) {
      let name = Object.keys(hwy_grouped)[i];
      let count = Object.keys(hwy_grouped)[i].length;
      highways[name] = count;
   }
   console.log(highways);
   let highways_sorted = Object.entries(highways).sort((a,b) => b[1] - a[1]);
   console.log(highways_sorted);
   // let new_sorted = Object.fromEntries(highways_sorted);
   // console.log(new_sorted);
   
   let x_data = [];
   let y_data = [];
   for (let z = 0; z < highways_sorted.length; z++) {
      //console.log(highways_sorted[z][0]);
      x_data.push(highways_sorted[z][0]);
      y_data.push(highways_sorted[z][1]);
   }

   // let x_data = Object.keys(highways);
   // let y_data = Object.values(highways);
   // console.log(x_data);
   // console.log(y_data);

   // Create bar plot
   let barChartData = [{
       x: x_data.slice(0, 10),
       y: y_data.slice(0, 10),
       //text: hoverText.slice(0, 10).reverse(), // https://plotly.com/javascript/hover-text-and-formatting/, referenced for how to format hovertext
       type: "bar"
   }];

   let barChartLayout = {
       tickvals: y_data.slice(0, 10), // https://plotly.com/javascript/tick-formatting/, referenced for tick formatting
       height: 800,
       width: 600
   };

   Plotly.newPlot("bar", barChartData, barChartLayout);

   // // Create bubble plot
   // let bubbleChartData = [{ //https://plotly.com/javascript/bubble-charts/, referenced for creating bubble chart
   //     x: otuIDNumbers,
   //     y: otuCounts,
   //     text: hoverText,
   //     mode: "markers",
   //     marker: {
   //         size: otuCounts,
   //         color: otuIDNumbers,
   //     }
   // }];

   // let bubbleChartLayout = {
   //     xaxis: {title: "OTU ID"}, // https://plotly.com/javascript/line-charts/, referenced for how to set x axis title
   //     height: 400,
   //     width: 1200
   // };

   // Plotly.newPlot("bubble", bubbleChartData, bubbleChartLayout);
}

// Function to create x axis tick labels for bar plot, converting from int to string with 'OTU' preceding the OTU ID number
// function createLabels(subjectData) {

//    let sampleOTUIDs = Object.values(subjectData.hwy_name);
//    let sampleOTUIDArray = [];
   
//    for (let i = 0; i < sampleOTUIDs.length; i++) { 
//        otu = `${sampleOTUIDs[i]}`;
//        sampleOTUIDArray.push(otu);
//    } 

//    return sampleOTUIDArray;
// }

// // Function to create plot hovertext
// function createHoverText(data) {

//    let microbeNames = Object.values(data.hwy_name);
//    let microbeNameArray = [];

//    for (let j = 0; j < microbeNames.length; j++) {
//        microbes = microbeNames[j];
//        microbeNameArray.push(microbes);
//    }

//    return microbeNameArray;
// }

// // Function to store OTU counts
// function setOTUCounts(data) {
//    return data.length;
// }

// // Function to store just OTU id integer
// function setOTUIDNumbers(data) {
//    return Object.values(data.otu_ids);
// }


// function init (){
//    let data = d3.json(dashboardQueryURL).then(function(data) { // https://stackoverflow.com/questions/53716527/request-data-from-front-end-d3-json-from-python-flask-backend, referenced for how to call flask data from javascript    
//       console.log("Hello");
//       const groupedYear = groupBy(data, 'date');
//       console.log(groupedYear);

//       let dates = groupedYear;

//       init_dropdown (dates);

//       console.log("Date: "+ dates);
    
//       plotBarChart(dates[0]);
//    });
// }

// function plotBarChart (crashes){

//    let numSamples = (samples.sample_values.slice(0,10));
//    numSamples = numSamples.reverse();
   
//    let axis = samples.otu_ids.slice(0,10).map(sample => `OTU ${sample}`);
//    axis = axis.reverse();


//    let labels =  (samples.otu_labels.slice(0,10));
//    labels = labels.reverse();
   
   
//    let trace = {
//        x: numSamples,
//        y: axis,
//        text: labels,
//        name: "OTU",
//        type: "bar",
//        orientation: "h"
//   };
  
//   let traceData = [trace];
  
//   let layout = {
//     title: "<b>Top 10 OTUs</b>",
//     margin: {
//       l: 100,
//       r: 100,
//       t: 100,
//       b: 100
//     }
//   };
  
//   Plotly.newPlot("bar", traceData, layout);
// }

// function init_dropdown (dates){
//   let dropdownMenu = d3.select("#selDataset");
  
//   for (let i = 0; i<dates.length;i++){
//     dropdownMenu.append("option").text(dates[i]).property("value", i);
//   }
// }

// function optionChanged (){
//    let dropdownMenu = d3.select("#selDataset");

//    let dataset = dropdownMenu.property("value");

//    let data = d3.json(url).then(function(data) {
//      console.log(data);
  
//      let crashes = data;
  
//      plotBarChart(crashes[dataset]);
//   });
//  }
//init();