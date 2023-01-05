const attr_breaks = {
    "Abb7_1":{"0":0.01,"1":0.04,"2":0.08,"3":0.13,"4":0.19,"5":0.26,"6":0.38,"7":0.56,"8":0.8,"9":1.0},
    "Abw14_1":{"0":0.01,"1":0.03,"2":0.07,"3":0.13,"4":0.21,"5":0.3,"6":0.42,"7":0.56,"8":0.69,"9":1.0},
    "Flu18_1":{"0":0.01,"1":0.06,"2":0.13,"3":0.2,"4":0.27,"5":0.33,"6":0.41,"7":0.5,"8":0.71,"9":1.0},
    "Gew1_1":{"0":0.03,"1":0.09,"2":0.17,"3":0.26,"4":0.35,"5":0.46,"6":0.6,"7":0.76,"8":0.91,"9":1.0},
    "Hel19_1":{"0":0.0,"1":0.01,"2":0.02,"3":0.03,"4":0.04,"5":0.05,"6":0.07,"7":0.08,"8":0.1,"9":0.11},
    "Keh15_1":{"0":0.0,"1":0.02,"2":0.04,"3":0.11,"4":0.17,"5":0.2,"6":0.24,"7":0.28,"8":0.41,"9":0.53},
    "Lan10_1":{"0":0.06,"1":0.19,"2":0.3,"3":0.41,"4":0.53,"5":0.64,"6":0.75,"7":0.86,"8":0.95,"9":1.0},
    "Lan17_1":{"0":0.02,"1":0.06,"2":0.11,"3":0.18,"4":0.29,"5":0.45,"6":0.6,"7":0.69,"8":0.88,"9":1.0},
    "Sak13_1":{"0":0.0,"1":0.01,"2":0.03,"3":0.06,"4":0.11,"5":0.21,"6":0.36,"7":0.57,"8":0.75,"9":1.0},
    "Ueb5_1":{"0":0.01,"1":0.03,"2":0.06,"3":0.09,"4":0.13,"5":0.19,"6":0.31,"7":0.5,"8":0.8,"9":1.0},
    "Ver11_1":{"0":0.0,"1":0.02,"2":0.05,"3":0.09,"4":0.13,"5":0.19,"6":0.27,"7":0.4,"8":0.6,"9":1.0},
    "Was16_1":{"0":0.0,"1":0.01,"2":0.03,"3":0.05,"4":0.08,"5":0.13,"6":0.21,"7":0.35,"8":0.67,"9":1.0},
    "Dac1":{"0":0.395,"1":1.05,"2":1.77,"3":2.63,"4":4.29,"5":7.855,"6":13.13,"7":19.295,"8":29.66,"9":47.34},
    "Fas2":{"0":2.685,"1":7.31,"2":11.9,"3":16.235,"4":20.545,"5":25.345,"6":31.83,"7":41.915,"8":59.265,"9":99.1},
    "Geb12":{"0":2.125,"1":4.895,"2":7.44,"3":9.865,"4":12.605,"5":16.69,"6":24.07,"7":38.5,"8":67.75,"9":100.0},
    "Kue8":{"0":5.46,"1":15.095,"2":23.18,"3":29.52,"4":33.885,"5":37.11,"6":39.55,"7":41.465,"8":43.67,"9":61.41},
    "Nat3":{"0":4.03,"1":10.84,"2":19.77,"3":30.98,"4":40.94,"5":47.71,"6":53.81,"7":61.47,"8":77.62,"9":100.0},
    "Veg3":{"0":7.765,"1":13.54,"2":18.035,"3":22.5,"4":27.645,"5":33.925,"6":42.13,"7":52.92,"8":66.28,"9":100.0},
    "Ver6":{"0":0.87,"1":2.465,"2":4.215,"3":6.025,"4":8.04,"5":10.63,"6":14.37,"7":20.795,"8":31.77,"9":65.8},
    "sky":{"0":11.54,"1":21.98,"2":28.48,"3":32.9,"4":36.35,"5":39.25,"6":41.84,"7":44.065,"8":46.125,"9":52.3},
    "prob":{"0":0.0400471143,"1":0.1081081081,"2":0.1903409091,"3":0.2926829268,"4":0.4151472651,"5":0.5352112676,"6":0.6454545455,"7":0.7678571429,"8":0.9117647059,"9":1.0},
    "z_resid":{"0":-6.9927525054,"1":-2.4518766177,"2":-1.2116360794,"3":-0.4652309489,"4":0.0542535574,"5":0.502108377,"6":1.0134915866,"7":1.6407808679,"8":2.4751938426,"9":5.1049555894},
    "net_income_ptp":{"0":62.1009756098,"1":72.8,"2":85.16,"3":102.4314666667,"4":125.4779220779,"5":162.92456,"6":227.310106383,"7":300.14,"8":705.1871428571,"9":965.08},
    "slope_median":{"0":2.7491133213,"1":5.7342841625,"2":9.0996456146,"3":12.8564176559,"4":16.8125171661,"5":20.8959541321,"6":25.1678504944,"7":29.7307367325,"8":35.0857982635,"9":50.3575305939},
    "rich":{"0":14.0,"1":40.0,"2":81.0,"3":137.0,"4":208.0,"5":297.0,"6":413.0,"7":582.0,"8":852.0,"9":1351.0},
    "med":{"0":75.2230682373,"1":83.0710525513,"2":89.1394348145,"3":94.2605056763,"4":99.8994903564,"5":107.4875564575,"6":117.1840438843,"7":129.658203125,"8":150.9007568359,"9":206.5233306885},
    "bldg_count":{"0":39.0,"1":107.0,"2":198.0,"3":314.0,"4":453.0,"5":617.0,"6":808.0,"7":1051.0,"8":1379.0,"9":2233.0},
    "gini":{"0":0.0132154034,"1":0.0302427539,"2":0.0414943015,"3":0.0541968385,"4":0.0675846114,"5":0.0815278311,"6":0.0972849566,"7":0.119344607,"8":0.1610778078,"9":0.2929458407},
    "cmpx_rh":{"0":3.5,"1":4.5,"2":5.5,"3":6.0,"4":7.0,"5":8.0,"6":9.0,"7":10.0,"8":11.5,"9":16.0},
    "snt_Neg":{"0":0.4504,"1":1.226,"2":2.0515,"3":2.994,"4":4.355,"5":6.676,"6":11.27,"7":19.06,"8":28.5,"9":42.6},
    "snt_Pos":{"0":16.92,"1":26.67,"2":30.83,"3":33.86,"4":37.02,"5":40.6,"6":44.89,"7":50.27,"8":57.63,"9":100.0},
    "rh_snt_0":{"0":1.5,"1":2.5,"2":3.5,"3":4.0,"4":4.5,"5":5.0,"6":6.0,"7":7.0,"8":8.0,"9":10.0},
    "pano_sum":{"0":1.783,"1":3.52,"2":5.65,"3":8.093,"4":10.748,"5":13.755,"6":17.46,"7":22.28,"8":29.34,"9":46.5},
    "pano_rh":{"0":4.0,"1":7.0,"2":10.0,"3":13.0,"4":16.5,"5":19.5,"6":23.0,"7":26.0,"8":29.5,"9":43.0},
    "refuge":{"0":0.27515,"1":0.4827,"2":0.61555,"3":0.72465,"4":0.8688,"5":1.071,"6":1.3615,"7":1.849,"8":2.875,"9":5.55},
    "cmpx_shanon":{"0":0.83085,"1":0.9885,"2":1.0975,"3":1.182,"4":1.265,"5":1.3475,"6":1.42475,"7":1.4925,"8":1.569,"9":1.801},
    "cmpx_gini":{"0":0.8125,"1":0.8255,"2":0.8355,"3":0.845,"4":0.85525,"5":0.8653,"6":0.87545,"7":0.88735,"8":0.90225,"9":0.952},
    "dist_gini":{"0":0.3345,"1":0.39965,"2":0.44525,"3":0.48195,"4":0.51305,"5":0.5386,"6":0.5665,"7":0.6097,"8":0.67505,"9":0.75}
};


function getColor(d, attr) {
        
    return d > attr_breaks[attr][8]  ? '#ffffd9' :
        d > attr_breaks[attr][7]  ? '#edf8b1' :
        d > attr_breaks[attr][6]  ? '#c7e9b4' :
        d > attr_breaks[attr][5]   ? '#7fcdbb' :
        d > attr_breaks[attr][4] ? '#41b6c4' :
        d > attr_breaks[attr][3]  ? '#1d91c0' :
        d > attr_breaks[attr][2]  ? '#225ea8' :
        d > attr_breaks[attr][1]  ? '#253494' :
        d > attr_breaks[attr][0]   ? '#081d58' :
                                    '#0c2c84';
    };

var button0Names = ["communes", "hexbins"];
var selectedData = 'hexbins';
var button0List = document.createElement("ul");
for (var i = 0; i < button0Names.length; i++) {
    var navBarpanel = document.getElementById("group_panel");
    var list0Item = document.createElement("li");
    var button0 = document.createElement("button");
    button0.innerHTML = button0Names[i];
    button0.classList.add('btn', 'btn-outline-secondary')
    button0.onclick = function() {
        selectedData = this.innerHTML;
        // console.log("Selected Data: " + selectedData);
        console.log(selectedData);
        updateMap(mapUrl[selectedData],mapVectorTileOptions);
        CartoDB_VoyagerOnlyLabels.addTo(map)
        console.log('here')
        // console.log("no of layers: "+vectorTileLayer.getLayers().length+10);
    }
    list0Item.appendChild(button0);
    button0List.appendChild(list0Item);
}
navBarpanel.appendChild(button0List);
// sidepanel.appendChild(buttonList);
var attr_names = {
    'All-Measure' : Object.keys(attr_breaks),
    'Scarce-Elements' : Object.keys(attr_breaks).slice(0, 12),
    'Abundant-Elements': Object.keys(attr_breaks).slice(12, 20), 
    'Urban-Natural-Form': Object.keys(attr_breaks).slice(20, 27), 
    'View-Configuration':Object.keys(attr_breaks).slice(27, 35),
}

// update map and remove previous layer on map
function updateMap(url,style){  
    // var grp_var = $('input[name="grp_radio"]:checked').val();
    // var metric_var = $('input[name="metric_radio"]:checked').val();
    var layersToRemove = [];
    var vectorTileLayer = new L.VectorGrid.Protobuf(url, style);
    map.eachLayer(function(layer){
        // console.log(layer)
        layersToRemove.push(layer)})
    // console.log('this  ' + layersToRemove)
    var arrayLength = layersToRemove.length;
    for (var i = 1; i < arrayLength; i++) {
        console.log(i);
        //Do something
        map.removeLayer(layersToRemove[i])
        console.log(layersToRemove[i])
    }

    return vectorTileLayer.addTo(map);
};
    
 // Initialize map and set view to Lausanne, Switzerland
 var map = L.map('map', {
    center: [46.8480, 7.9474],//[46.4414,6.5295],// [46.9480, 7.4474]
    minZoom: 9,
    maxZoom: 16,
    zoomControl: true,
    zoom: 8,
});
//  // add background basemap
// var mapBaseLayer = L.tileLayer(
//     'https://{s}.basemaps.cartocdn.com/rastertiles/light_all/{z}/{x}/{y}.png', {
//         attribution: '(C) OpenStreetMap contributors (C) CARTO'
//     }
// ).addTo(map);

var CartoDB_VoyagerNoLabels = L.tileLayer('https://{s}.basemaps.cartocdn.com/rastertiles/voyager_nolabels/{z}/{x}/{y}{r}.png', {
	attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
	subdomains: 'abcd',
	maxZoom: 20
}).addTo(map);

var CartoDB_VoyagerOnlyLabels = L.tileLayer('https://{s}.basemaps.cartocdn.com/rastertiles/voyager_only_labels/{z}/{x}/{y}{r}.png', {
	attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
	subdomains: 'abcd',
	maxZoom: 20
});

// get vector tiles URL
var mapUrl = {
    "hexbins": "tiles_hexbin_151222/{z}/{x}/{y}.pbf",
    "communes": "tiles_commune_151222/{z}/{x}/{y}.pbf",
};

var vectorTileStyling = {
  // call original geojson file name
  suisse_commune_4326: function(properties, zoom) {
  
    // get corresponding color 
    var fillColor = getColor(properties[select_attr], select_attr)
    var opacity = .9;
    var weight = 0;
    if (zoom > 12) {
        weight = 1.0;
        opacity = .5;
  }
  return ({
      fill: true,
      fillColor: fillColor,
      fillOpacity: opacity,
      weight: weight,
      color: "#ffffff",
  });
    },
    suisse_hexbin_4326: function(properties, zoom) {

        // get corresponding color 
        var fillColor = getColor(properties[select_attr], select_attr)
        var opacity = 1.0;
        var weight = 0;
        if (zoom > 12) {
            weight = 1.0;
            opacity = .5;
    }
    return ({
        fill: true,
        fillColor: fillColor,
        fillOpacity: opacity,
        weight: weight,
        color: "#ffffff",
    })}
    };
// define options of vector tiles
var mapVectorTileOptions = {
  
    rendererFactory: L.canvas.tile,
    interactive: true,
    attribution: '(C) A.R. Swietek',
    maxNativeZoom: 15,
    minZoom: 6,
    vectorTileLayerStyles:vectorTileStyling,
  };

var buttonNames = Object.keys(attr_names);
var buttonList = document.createElement("ul");
var select_attr = 'slope_median';
var select_metrics = 'All-Measure';
// Add the vector tiles to the map using default data
var vectorTileLayer = new L.VectorGrid.Protobuf(mapUrl[selectedData], mapVectorTileOptions).addTo(map);
CartoDB_VoyagerOnlyLabels.addTo(map)
// Create Series of Buttons starting from Groups -> Metric Type -> Metric
for (var i = 0; i < buttonNames.length; i++) {
    var metrcPanel = document.getElementById("metrics_panel");
    var listItem = document.createElement("li");
    var button = document.createElement("button");
    button.innerHTML = buttonNames[i];
    button.classList.add('btn', 'btn-outline-primary')
    button.onclick = function() {
        select_metrics = this.innerHTML;
        console.log("Selected metric: " + select_metrics);
        var existingLists = document.getElementsByTagName("ul");
            console.log(existingLists)
            while (existingLists.length > 3) {
                existingLists[3].parentNode.removeChild(existingLists[3]);
            }
        // Create new button list
        var newButtonNames = attr_names[select_metrics];
        var newButtonList = document.createElement("ul");

        for (var i = 0; i < newButtonNames.length; i++) {
            var newListItem = document.createElement("li");
            var newButton = document.createElement("button");
            newButton.innerHTML = newButtonNames[i];
            newButton.classList.add('btn', 'btn-outline-secondary')
            newButton.onclick = function() {
                select_attr = this.innerHTML;
                console.log("Selected attribute: " + select_attr);
                updateMap(mapUrl[selectedData],mapVectorTileOptions);
                CartoDB_VoyagerOnlyLabels.addTo(map)
            }
            
            newListItem.appendChild(newButton);
            newButtonList.appendChild(newListItem);
        }
        // Add new button list to the page
        metrcPanel.appendChild(newButtonList);
    }

    button.innerHTML = buttonNames[i];
    listItem.appendChild(button);
    buttonList.appendChild(listItem);
}
metrcPanel.appendChild(buttonList);

// Create new button list
var newButtonNames = attr_names[select_metrics];
var newButtonList = document.createElement("ul");

for (var i = 0; i < newButtonNames.length; i++) {
    var newListItem = document.createElement("li");
    var newButton = document.createElement("button");
    newButton.innerHTML = newButtonNames[i];
    newButton.classList.add('btn', 'btn-outline-secondary')
    newButton.onclick = function() {
        select_attr = this.innerHTML;
        console.log("Selected attribute: " + select_attr);
        updateMap(mapUrl[selectedData],mapVectorTileOptions);
        CartoDB_VoyagerOnlyLabels.addTo(map)
    }
    
    newListItem.appendChild(newButton);
    newButtonList.appendChild(newListItem);
}
// Add new button list to the page
metrcPanel.appendChild(newButtonList);
