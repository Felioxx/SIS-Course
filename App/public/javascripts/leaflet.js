// Map with NRW bounds
var map = L.map("map").setView([51.51588878700843, 7.475327389339492], 7);

mapLink = '<a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>';
var osm = L.tileLayer("http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  attribution: "&copy; " + mapLink + " Contributors",
  maxZoom: 18,
}).addTo(map);

var baseMaps = {
  OpenStreetMap: osm,
};

var layerControl = L.control.layers(baseMaps).addTo(map);
let geoJsonLayerGroup = L.layerGroup().addTo(map);
