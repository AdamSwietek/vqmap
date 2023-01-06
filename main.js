const attr_breaks ={
    "bldg_count":{"0":36.0,"1":96.0,"2":177.0,"3":279.0,"4":408.0,"5":562.0,"6":750.0,"7":995.0,"8":1337.0,"9":2233.0},
    "rich":{"0":12.0,"1":37.0,"2":77.0,"3":135.0,"4":207.0,"5":297.0,"6":416.0,"7":582.0,"8":852.0,"9":1351.0},
    "prob":{"0":0.03,"1":0.1,"2":0.18,"3":0.27,"4":0.36,"5":0.46,"6":0.58,"7":0.73,"8":0.9,"9":1.0},
    "cv":{"0":0.0199999996,"1":0.0599999987,"2":0.0799999982,"3":0.1000000015,"4":0.1299999952,"5":0.1599999964,"6":0.1899999976,"7":0.2399999946,"8":0.3400000036,"9":0.5699999928},
    "gini":{"0":0.01,"1":0.03,"2":0.04,"3":0.05,"4":0.06,"5":0.07,"6":0.09,"7":0.11,"8":0.15,"9":0.29},
    "med":{"0":73.0,"1":82.0,"2":89.0,"3":95.0,"4":101.0,"5":108.0,"6":117.0,"7":130.0,"8":151.0,"9":207.0},
    "avg":{"0":77.0,"1":84.0,"2":90.0,"3":96.0,"4":102.0,"5":110.0,"6":120.0,"7":133.0,"8":155.0,"9":203.0},
    "l_prob":{"0":0.05,"1":0.15,"2":0.26,"3":0.36,"4":0.45,"5":0.54,"6":0.65,"7":0.78,"8":0.92,"9":1.0},
    "net_income_ptp":{"0":62.0,"1":73.0,"2":85.0,"3":102.0,"4":126.0,"5":163.0,"6":230.0,"7":300.0,"8":705.0,"9":965.0},
    "z_resid":{"0":-6.79,"1":-2.26,"2":-1.03,"3":-0.33,"4":0.16,"5":0.6,"6":1.1,"7":1.71,"8":2.53,"9":5.1},
    "slope_median":{"0":2.0,"1":6.0,"2":9.0,"3":13.0,"4":17.0,"5":21.0,"6":26.0,"7":31.0,"8":36.0,"9":50.0},
    "slope_mean":{"0":2.0,"1":5.0,"2":9.0,"3":13.0,"4":17.0,"5":21.0,"6":25.0,"7":30.0,"8":35.0,"9":48.0},
    "cmpx_rh":{"0":3.0,"1":4.0,"2":5.0,"3":6.0,"4":7.0,"5":8.0,"6":9.0,"7":10.0,"8":11.0,"9":16.0},
    "cmpx_shanon":{"0":0.79,"1":0.95,"2":1.07,"3":1.16,"4":1.24,"5":1.33,"6":1.42,"7":1.49,"8":1.57,"9":1.8},
    "cmpx_gini":{"0":0.81,"1":0.82,"2":0.83,"3":0.84,"4":0.85,"5":0.86,"6":0.87,"7":0.88,"8":0.9,"9":0.95},
    "snt_0":{"0":28.0,"1":34.0,"2":38.0,"3":41.0,"4":44.0,"5":46.0,"6":49.0,"7":56.0,"8":74.0,"9":100.0},
    "snt_Neg":{"0":0.0,"1":1.0,"2":2.0,"3":3.0,"4":4.0,"5":6.0,"6":11.0,"7":19.0,"8":28.0,"9":43.0},
    "snt_Pos":{"0":17.0,"1":27.0,"2":31.0,"3":34.0,"4":37.0,"5":41.0,"6":46.0,"7":51.0,"8":57.0,"9":100.0},
    "rh_snt_0":{"0":1.0,"1":2.0,"2":3.0,"3":4.0,"4":5.0,"5":6.0,"6":7.0,"7":8.0,"8":9.0,"9":10.0},
    "dist_gini":{"0":0.33,"1":0.39,"2":0.43,"3":0.47,"4":0.5,"5":0.53,"6":0.55,"7":0.59,"8":0.65,"9":0.75},
    "pano_sum":{"0":1.0,"1":3.0,"2":5.0,"3":7.0,"4":9.0,"5":11.0,"6":14.0,"7":19.0,"8":26.0,"9":46.0},
    "pano_rh":{"0":4.0,"1":8.0,"2":11.0,"3":14.0,"4":17.0,"5":19.0,"6":22.0,"7":25.0,"8":28.0,"9":43.0},
    "Dac1":{"0":0.0,"1":1.0,"2":2.0,"3":3.0,"4":5.0,"5":9.0,"6":13.0,"7":19.0,"8":29.0,"9":47.0},
    "Fas2":{"0":3.0,"1":8.0,"2":13.0,"3":16.0,"4":20.0,"5":25.0,"6":31.0,"7":41.0,"8":58.0,"9":99.0},
    "Geb12":{"0":2.0,"1":4.0,"2":7.0,"3":9.0,"4":12.0,"5":16.0,"6":23.0,"7":38.0,"8":68.0,"9":100.0},
    "Kue8":{"0":3.0,"1":11.0,"2":19.0,"3":27.0,"4":33.0,"5":36.0,"6":39.0,"7":41.0,"8":44.0,"9":61.0},
    "Nat3":{"0":3.0,"1":9.0,"2":17.0,"3":28.0,"4":39.0,"5":47.0,"6":53.0,"7":60.0,"8":73.0,"9":100.0},
    "Veg3":{"0":7.0,"1":13.0,"2":18.0,"3":22.0,"4":27.0,"5":34.0,"6":42.0,"7":51.0,"8":63.0,"9":100.0},
    "Ver6":{"0":0.0,"1":2.0,"2":4.0,"3":6.0,"4":8.0,"5":12.0,"6":16.0,"7":23.0,"8":35.0,"9":66.0},
    "sky":{"0":7.0,"1":16.0,"2":24.0,"3":30.0,"4":33.0,"5":37.0,"6":40.0,"7":43.0,"8":45.0,"9":52.0},
    "Abb7_1":{"0":1.0,"1":4.0,"2":8.0,"3":13.0,"4":20.0,"5":29.0,"6":41.0,"7":57.0,"8":80.0,"9":100.0},
    "Abw14_1":{"0":1.0,"1":4.0,"2":9.0,"3":15.0,"4":22.0,"5":31.0,"6":42.0,"7":56.0,"8":69.0,"9":100.0},
    "Flu18_1":{"0":1.0,"1":6.0,"2":13.0,"3":20.0,"4":31.0,"5":41.0,"6":50.0,"7":71.0,"8":92.0,"9":100.0},
    "Gew1_1":{"0":2.0,"1":8.0,"2":15.0,"3":24.0,"4":34.0,"5":45.0,"6":59.0,"7":75.0,"8":91.0,"9":100.0},
    "Hel19_1":{"0":0.0,"1":1.0,"2":2.0,"3":3.0,"4":4.0,"5":5.0,"6":7.0,"7":8.0,"8":10.0,"9":11.0},
    "Keh15_1":{"0":0.0,"1":2.0,"2":4.0,"3":11.0,"4":17.0,"5":20.0,"6":24.0,"7":28.0,"8":41.0,"9":53.0},
    "Lan10_1":{"0":6.0,"1":19.0,"2":31.0,"3":43.0,"4":55.0,"5":65.0,"6":74.0,"7":84.0,"8":94.0,"9":100.0},
    "Lan17_1":{"0":1.0,"1":5.0,"2":11.0,"3":18.0,"4":29.0,"5":45.0,"6":60.0,"7":69.0,"8":88.0,"9":100.0},
    "Sak13_1":{"0":0.0,"1":1.0,"2":3.0,"3":6.0,"4":11.0,"5":21.0,"6":36.0,"7":57.0,"8":75.0,"9":100.0},
    "Ueb5_1":{"0":1.0,"1":3.0,"2":6.0,"3":9.0,"4":15.0,"5":24.0,"6":36.0,"7":50.0,"8":80.0,"9":100.0},
    "Ver11_1":{"0":1.0,"1":3.0,"2":6.0,"3":10.0,"4":15.0,"5":20.0,"6":27.0,"7":40.0,"8":60.0,"9":100.0},
    "Was16_1":{"0":0.0,"1":1.0,"2":3.0,"3":5.0,"4":9.0,"5":14.0,"6":22.0,"7":35.0,"8":67.0,"9":100.0}
}



const attr_pal = {
    "Abb7_1": "Spectral",
    "Abw14_1":"Spectral",
    "Flu18_1":"Spectral",
    "Gew1_1":"viridis",
    "Hel19_1":"Spectral",
    "Keh15_1":"Spectral",
    "Lan10_1":"Spectral",
    "Lan17_1":"Spectral",
    "Sak13_1":"Spectral",
    "Ueb5_1":"Spectral",
    "Ver11_1":"Spectral",
    "Was16_1":"Spectral",
    "Dac1":"Spectral",
    "Fas2":"Spectral",
    "Geb12":"Spectral",
    "Kue8":"Spectral",
    "Nat3":"viridis",
    "Veg3":"Spectral",
    "Ver6":"Spectral",
    "sky":"Spectral",
    "prob":'icefire',
    "z_resid":"icefire",
    "net_income_ptp":"Spectral",
    "slope_median":"mako",
    "rich":"cubehelix",
    "med":"cubehelix",
    "bldg_count":"cubehelix",
    "gini":"mako",
    "cmpx_rh":"mako",
    "snt_Neg":"mako",
    "snt_Pos":"mako",
    "rh_snt_0":"mako",
    "pano_sum":"mako",
    "pano_rh":"mako",
    "refuge":"mako",
    "cmpx_shanon":"mako",
    "cmpx_gini":"mako",
    "dist_gini":"mako",
};

icon_dict = {'bldg_count': 'images/icons/icon-01.png',
'rich': 'images/icons/icon-02.png',
'prob': 'images/icons/icon-03.png',
'cv': 'images/icons/icon-04.png',
'gini': 'images/icons/icon-05.png',
'med': 'images/icons/icon-06.png',
'avg': 'images/icons/icon-07.png',
'l_prob': 'images/icons/icon-08.png',
'net_income_ptp': 'images/icons/icon-09.png',
'z_resid': 'images/icons/icon-10.png',
'slope_median': 'images/icons/icon-11.png',
'slope_mean': 'images/icons/icon-12.png',
'cmpx_rh': 'images/icons/icon-13.png',
'cmpx_shanon': 'images/icons/icon-14.png',
'cmpx_gini': 'images/icons/icon-15.png',
'snt_0': 'images/icons/icon-16.png',
'snt_Neg': 'images/icons/icon-17.png',
'snt_Pos': 'images/icons/icon-18.png',
'rh_snt_0': 'images/icons/icon-19.png',
'dist_gini': 'images/icons/icon-20.png',
'pano_sum': 'images/icons/icon-21.png',
'pano_rh': 'images/icons/icon-22.png',
'refuge': 'images/icons/icon-23.png',
'Dac1': 'images/icons/icon-24.png',
'Fas2': 'images/icons/icon-25.png',
'Geb12': 'images/icons/icon-26.png',
'Kue8': 'images/icons/icon-27.png',
'Nat3': 'images/icons/icon-28.png',
'Veg3': 'images/icons/icon-29.png',
'Ver6': 'images/icons/icon-30.png',
'sky': 'images/icons/icon-31.png',
'Abb7_1': 'images/icons/icon-32.png',
'Abw14_1': 'images/icons/icon-33.png',
'Flu18_1': 'images/icons/icon-34.png',
'Gew1_1': 'images/icons/icon-35.png',
'Hel19_1': 'images/icons/icon-36.png',
'Keh15_1': 'images/icons/icon-37.png',
'Lan10_1': 'images/icons/icon-38.png',
'Lan17_1': 'images/icons/icon-39.png',
'Sak13_1': 'images/icons/icon-40.png',
'Sie9_1': 'images/icons/icon-41.png',
'Ueb5_1': 'images/icons/icon-42.png',
'Ver11_1': 'images/icons/icon-43.png',
'Was16_1': 'images/icons/icon-44.png',
'Abb7_10': 'images/icons/icon-45.png',
'Abw14_10': 'images/icons/icon-46.png',
'Flu18_10': 'images/icons/icon-47.png',
'Gew1_10': 'images/icons/icon-48.png',
'Hel19_10': 'images/icons/icon-49.png',
'Keh15_10': 'images/icons/icon-50.png',
'Lan10_10': 'images/icons/icon-51.png',
'Lan17_10': 'images/icons/icon-52.png',
'Sak13_10': 'images/icons/icon-53.png',
'Sie9_10': 'images/icons/icon-54.png',
'Ueb5_10': 'images/icons/icon-55.png',
'Ver11_10': 'images/icons/icon-56.png',
'Was16_10': 'images/icons/icon-57.png'}


const color_dict = {
    "YlGnBu":{"0":"#f2fabc","1":"#dcf1b2","2":"#bbe4b5","3":"#85cfba","4":"#57bec1","5":"#34a9c3","6":"#1d8dbe","7":"#2166ac","8":"#24479d","9":"#1d2e83"},
    "Spectral":{"0":"#d0384e","1":"#ee6445","2":"#fa9b58","3":"#fece7c","4":"#fff1a8","5":"#f4faad","6":"#d1ed9c","7":"#97d5a4","8":"#5cb7aa","9":"#3682ba"},
    "rocket":{"0":"#221331","1":"#451c47","2":"#691f55","3":"#921c5b","4":"#b91657","5":"#d92847","6":"#ed503e","7":"#f47d57","8":"#f6a47c","9":"#f7c9aa"},
    "flare":{"0":"#eb9973","1":"#e88366","2":"#e46c5d","3":"#db565d","4":"#cc4664","5":"#b73d6b","6":"#a1386f","7":"#8b3271","8":"#752d6f","9":"#602969"},
    "coolwarm":{"0":"#5673e0","1":"#7597f6","2":"#94b6ff","3":"#b5cdfa","4":"#d1dae9","5":"#e8d6cc","6":"#f5c1a9","7":"#f6a283","8":"#ea7b60","9":"#d44e41"},
    "RdBu":{"0":"#ab162a","1":"#cf5246","2":"#eb9172","3":"#fac8af","4":"#faeae1","5":"#e6eff4","6":"#bbdaea","7":"#7bb6d6","8":"#3c8abe","9":"#1e61a5"},
    "mako":{"0":"#231526","1":"#35264c","2":"#403974","3":"#3d5296","4":"#366da0","5":"#3487a6","6":"#35a1ab","7":"#44bcad","8":"#6dd3ad","9":"#aee3c0"},
    "viridis":{"0":"#482173","1":"#433e85","2":"#38588c","3":"#2d708e","4":"#25858e","5":"#1e9b8a","6":"#2ab07f","7":"#52c569","8":"#86d549","9":"#c2df23"},
    "cubehelix":{"0":"#19122b","1":"#17344c","2":"#185b48","3":"#3c7632","4":"#7e7a36","5":"#bc7967","6":"#d486af","7":"#caa9e7","8":"#c2d2f3","9":"#d6f0ef"},
    "icefire":{"0":"#7bbbce","1":"#3f90ce","2":"#475cbc","3":"#3b3866","4":"#22222b","5":"#2d1f21","6":"#622937","7":"#a83044","8":"#dc5534","9":"#f29558"}
}

// console.log(color_dict['YlGnBu'])
function getColor(d, attr) {
    // var break_val = attr_breaks[attr];
    // var pal = attr_pal[attr];
    // var colorlst = color_dict[pal];
    // console.log(pal);
    // breakvalue list is offset by 1 bc the last position is the maximum value of series
    return d > attr_breaks[attr][8]  ? color_dict[attr_pal[attr]][9] :
            d > attr_breaks[attr][7]  ? color_dict[attr_pal[attr]][8] :
            d > attr_breaks[attr][6]  ? color_dict[attr_pal[attr]][7] :
            d > attr_breaks[attr][5]  ? color_dict[attr_pal[attr]][6] :
            d > attr_breaks[attr][4]  ? color_dict[attr_pal[attr]][5] :
            d > attr_breaks[attr][3]  ? color_dict[attr_pal[attr]][4] :
            d > attr_breaks[attr][2]  ? color_dict[attr_pal[attr]][3] :
            d > attr_breaks[attr][1]  ? color_dict[attr_pal[attr]][2] :
            d > attr_breaks[attr][0]  ? color_dict[attr_pal[attr]][1] :
            color_dict[attr_pal[attr]][0];
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
    'Scarce-Elements' : ['Abb7_1','Abw14_1', 'Flu18_1', 'Gew1_1', 'Hel19_1', 'Keh15_1', 'Lan10_1','Lan17_1', 'Sak13_1', 'Ueb5_1', 'Ver11_1', 'Was16_1'],
    'Abundant-Elements': ['Dac1','Fas2', 'Geb12', 'Kue8', 'Nat3', 'Veg3', 'Ver6', 'sky'], 
    'Urban-Natural-Form': ['prob', 'z_resid', 'net_income_ptp', 'slope_median', 'rich', 'med','bldg_count','gini'], 
    'View-Configuration':['cmpx_rh', 'snt_Neg', 'snt_Pos', 'rh_snt_0',  'pano_sum', 'pano_rh', 'refuge','cmpx_shanon', 'cmpx_gini','dist_gini'],
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
var select_metrics = 'Urban-Natural-Form';
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
        // console.log("Selected metric: " + select_metrics);
        var existingLists = document.getElementsByTagName("ul");
            // console.log(existingLists)
            while (existingLists.length > 3) {
                existingLists[3].parentNode.removeChild(existingLists[3]);
            }
        // Create new button list
        var newButtonNames = attr_names[select_metrics];
        var newButtonList = document.createElement("ul");
        // var newicon = icon_dict[select_attr]

        for (var i = 0; i < newButtonNames.length; i++) {
            var newListItem = document.createElement("li");
            var newButton = document.createElement("button");
            var icon = document.createElement("img");
            icon.src = icon_dict[newButtonNames[i]];
            // console.log(icon.src)
            // console.log(newButtonNames[i])
            icon.style.height = '50px';
            icon.alt = "Icon " + (i+1);
            newButton.innerHTML = newButtonNames[i];
            newButton.classList.add('btn', 'unstyled-button')
            newButton.onclick = function() {
                select_attr = this.textContent;
                // console.log(this.textContent)
                console.log("Selected attribute: " + select_attr);
                updateMap(mapUrl[selectedData],mapVectorTileOptions);
                CartoDB_VoyagerOnlyLabels.addTo(map)
            }
            newButton.appendChild(icon);
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
var newicon = icon_dict[select_attr]
var newButtonList = document.createElement("ul");

for (var i = 0; i < newButtonNames.length; i++) {
    var newListItem = document.createElement("li");
    var newButton = document.createElement("button");
    var icon = document.createElement("img");
    icon.src = icon_dict[newButtonNames[i]];
    // console.log(icon.src)
    // console.log(newButtonNames[i])
    icon.style.height = '50px';
    icon.alt = "Icon " + (i+1);
    newButton.innerHTML = newButtonNames[i];
    newButton.classList.add('btn', 'unstyled-button')
    newButton.onclick = function() {
        // console.log(this)
        select_attr = this.textContent;
        console.log("Selected attribute: " + select_attr);
        updateMap(mapUrl[selectedData],mapVectorTileOptions);
        CartoDB_VoyagerOnlyLabels.addTo(map)
    }
    newButton.appendChild(icon);
    newListItem.appendChild(newButton);
    newButtonList.appendChild(newListItem);
}
// Add new button list to the page
metrcPanel.appendChild(newButtonList);
