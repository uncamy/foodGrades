var width = 1200;
var height = 800;

var svg;
var scores;
//var data = d3.json('./data/NYC_mean_scores.json');
var data = d3.json('data/data2.json', function(d){
    scores = d;
});
//mapping + center point
var projection = d3.geo.mercator()
    .center([-73.955541, 40.795780])
    .scale(95000);

var path = d3.geo.path().projection(projection);


var setSVG = function () {
    svg = d3.select("body").append("svg")
        .attr("class", "Blues")
        .attr("width", width)
        .attr("height", height);
};

//quantize and colors
var setColors = d3.scale.quantize()
    .domain([0, 30])
    .range(d3.range(9).map(function(i) {
        var ret= "q" + (i) + "-9";
        console.log(ret);
        return ret;
 }));

//map mean resturant health score by zipcode color
var zipColor = function(zip, data) {
    if(zip in data) {
        return setColors(data[zip]);
    }else{
        return "q1-9";
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
        .attr("class", function(d) {
            return zipColor(d.id, scores)})
        .attr("d", path);
}


// Create legend
var setLegend = function () {
    var tick = dataMax / n_ticks;
    var range = [];
    for (k = 0; k< n_ticks; k++){
        range.push(Math.floor(k*tick));
    }
    var legend = svg.selectAll ('g.legend')
        .data(range)
        .enter().append('g')
        .attr("class", "legend");

    legend.append("rect")
        .attr("x", 20)
        .attr("y", function(d, i){ return height/3.5 - (i*ls_h) -2*ls_h;})
        .attr("width", ls_w)
        .attr("height", ls_h)
        .attr("class", function(d, i){
            console.log(d)
            return setColors(d); })
    legend.append("text")
        .attr("x", 40 +2)
        .attr("y", function (d,i) {return height/3.5 - (i*ls_h) - ls_h -4;})
        .attr("class", "mapSubtext")
        .text(function(d, i){return d});

}
// alllow view data on mouseover
document.body.get
var mouseOver = function (){
    $("path").hover(function (){
        zip = $(this).attr("title");
        meanScore = scores[zip];
        console.log(meanScore)
        $("#infoBox").html("Zipcode: " + zip + " Mean score: " + Math.round(meanScore));
        }
    );
};

//Add labels
var dataMax = 40;
var ls_w = 20;
var ls_h = 20;
var n_ticks  = 9;

//Read in Json for map outline of ZIPS
d3.json('./data/zipcodes.json', function(zips){
    setSVG();
    mapCreate(zips);
    setLegend();
    mouseOver();
});
