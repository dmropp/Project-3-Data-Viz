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

function init (){
   let data = d3.json(dashboardQueryURL).then(function(data) { // https://stackoverflow.com/questions/53716527/request-data-from-front-end-d3-json-from-python-flask-backend, referenced for how to call flask data from javascript    
      console.log("Hello");
      const groupedYear = groupBy(data, 'date');
      console.log(groupedYear);

      let dates = groupedYear;

      init_dropdown (dates);

      console.log("Date: "+ dates);
    
      plotBarChart(dates[0]);
   });
}

function plotBarChart (crashes){

   let numSamples = (samples.sample_values.slice(0,10));
   numSamples = numSamples.reverse();
   
   let axis = samples.otu_ids.slice(0,10).map(sample => `OTU ${sample}`);
   axis = axis.reverse();


   let labels =  (samples.otu_labels.slice(0,10));
   labels = labels.reverse();
   
   
   let trace = {
       x: numSamples,
       y: axis,
       text: labels,
       name: "OTU",
       type: "bar",
       orientation: "h"
  };
  
  let traceData = [trace];
  
  let layout = {
    title: "<b>Top 10 OTUs</b>",
    margin: {
      l: 100,
      r: 100,
      t: 100,
      b: 100
    }
  };
  
  Plotly.newPlot("bar", traceData, layout);
}

function init_dropdown (dates){
  let dropdownMenu = d3.select("#selDataset");
  
  for (let i = 0; i<dates.length;i++){
    dropdownMenu.append("option").text(dates[i]).property("value", i);
  }
}

function optionChanged (){
   let dropdownMenu = d3.select("#selDataset");

   let dataset = dropdownMenu.property("value");

   let data = d3.json(url).then(function(data) {
     console.log(data);
  
     let crashes = data;
  
     plotBarChart(crashes[dataset]);
  });
 }
 init();