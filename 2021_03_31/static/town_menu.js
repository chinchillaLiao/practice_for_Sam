import map from './ol_main.js';

var response_town_list;
var response_town_polygon;

var html_select = '<select id="select_town" style="width:200px;" value="-1" ><option label="請選擇鄉鎮"></option>'
let xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function(){
	if (this.readyState == 4 && this.status == 200) {
		response_town_list = JSON.parse(this.responseText);           
		
		Object.getOwnPropertyNames(response_town_list).map(function(x){
			html_select = html_select + "<optgroup label= '"+x+"'>"
			Object.getOwnPropertyNames(response_town_list[x]).map(function(y){
				html_select = html_select + "<option value= '"+response_town_list[x][y]+"'>" + y + "</option>"
			})
			html_select = html_select + "</optgroup>"
		})				
		html_select = html_select + '</select>';
		$("#area_list").append(html_select);
		
		$("#select_town").on('change',function() {
			var value = $(this).val();
			let xhttp = new XMLHttpRequest();
			xhttp.onreadystatechange = function(){
				if (this.readyState == 4 && this.status == 200) {
					response_town_polygon = JSON.parse(this.responseText);
					var feature = new ol.format.GeoJSON().readFeature(response_town_polygon);
					feature.getGeometry().transform('EPSG:4326', 'EPSG:3857')
					#console.log(map.getLayers())
					var vectorSource = map.getLayers().array_[1].getSource()
					vectorSource.clear();
					vectorSource.addFeature(feature);
					#console.log(vectorSource)

					
				}else if(this.readyState==4 && this.status == 500){
					alert("查詢錯誤");
				}
			};
			xhttp.open("GET","http://127.0.0.1:5000/feature/town/"+value , true);    
			xhttp.send();
		});
		
	}else if(this.readyState==4 && this.status == 500){
		alert("查詢錯誤");
	}
};
xhttp.open("GET","http://127.0.0.1:5000/menu/town", true);    
xhttp.send();




$("#menu_town").click(function() {
		$("#search_div").css("visibility","visible");
});
$("#menu_town_close").click(function() {
		$("#search_div").css("visibility","hidden");
});
