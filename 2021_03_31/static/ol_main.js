// 地圖物件




var map = new ol.Map({
  target: 'js-map',
  pixelRatio: 2,
  view: new ol.View({
    center: ol.proj.fromLonLat([120.3043, 22.6206]),
    zoom: 10,
  }),
});

// 底圖: 國土繪測中心
var layer_nlsc = new ol.layer.Tile({
  source: new ol.source.XYZ({
	// you can find more free tile-servers from https://wiki.openstreetmap.org/wiki/Tile_servers
	url:"https://c.tile.openstreetmap.org/{z}/{x}/{y}.png",
  }),
});

// 控制物件: 滑鼠經緯度
var mousePositionControl = new ol.control.MousePosition({
  coordinateFormat: ol.coordinate.createStringXY(4),
  projection: 'EPSG:4326',
  //comment the following two lines to have the mouse position
  //be placed within the map.
  className: 'custom-mouse-position',
  target: document.getElementById('mouse-position'),
  // &nbsp 是HTML空格的意思
  undefinedHTML: '&nbsp;',
});


map.addLayer(layer_nlsc);
map.addControl(mousePositionControl);


var style_Polygon = new ol.style.Style({
    stroke: new ol.style.Stroke({
      color: 'blue',
      lineDash: [4],
      width: 3,
    }),
    fill: new ol.style.Fill({
      color: 'rgba(0, 0, 255, 0.1)',
    }),
  });
  
vectorSource = new ol.source.Vector();

vectorLayer = new ol.layer.Vector({
	source:vectorSource,
	style:style_Polygon
})

map.addLayer(vectorLayer);

map.on('rendercomplete',function(e) {
  var zoomLevel = map.getView().getZoom();
  document.getElementById('zoomlv').innerHTML = zoomLevel;
})










