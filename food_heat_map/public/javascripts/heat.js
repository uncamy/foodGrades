var width = 960;
var height = 500;

var svg;
var zips;

var data = d3.json('./data/NYC_mean_scores.json');
//mapping + center point
var projection = d3.geo.mercator()
    .center([-73.955541, 40.795780])
    .scale(95000);

var path = d3.geo.path().projection(projection);


var setSVG = function () {
    svg = d3.select("body").append("svg")
        .attr("width", width)
        .attr("height", height);
};

//quantize and colors
var setColors = d3.scale.quantize()
    .domain([0, 40])
    .range(d3.range(9).map(function(i){return "q" + (i) + "-9";}));

//map mean resturant health score by zipcode color
var zipColor = function(zip, data) {
    if(zip in data) {
        return setColors(data[zip]);
    }else{
        return "white";
    }
};

//mapping setup
var mapCreate = function (zips) {
    svg.append("g")
        .selectAll("path")
        .data(zips.features)
        .enter()
        .append("path")
        .attr("title", function(d) {return d.id})
        .attr("stroke", '#fff')
        .attr("class", function(d) {return zipColor(d.id, data) ;})
        .attr("d", path);
}
//Read in Json for map outline of ZIPS
d3.json('./data/zipcodes.json', function(zips){
    setSVG();
    mapCreate(zips);
});

/*
var rateById = d3.map();

var quantize = d3.scale.quantize()
    .domain([0, .15])
    .range(d3.range(9).map(function(i) { return "q" + i + "-9"; }));

var path = d3.geo.path();


queue()
    .defer(d3.json, "./data/zipcodes.json")
    .defer(d3.json, "./data/NYC_mean_scores.json"), function(d) { rateById.set(d.id, +d.rate); })
      .await(ready);

   function ready(error, us) {
     svg.append("g")
         .attr("class", "counties")
      .selectAll("path")
         .data(topojson.feature(us, us.objects.counties).features)
      .enter().append("path")
         .attr("class", function(d) { return quantize(rateById.get(d.id)); })
         .attr("d", path);

  svg.append("path")
      .datum(topojson.mesh(us, us.objects.states, function(a, b) { return a !== b; }))
      .attr("class", "states")
      .attr("d", path);
}
*/
