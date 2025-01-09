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
let fsGeoJsonLayerGroup = L.featureGroup().addTo(map);
let adGeoJsonLayerGroup = L.featureGroup().addTo(map);
let districtGeoJsonLayerGroup = L.featureGroup().addTo(map);
let cityGeoJsonLayerGroup = L.featureGroup().addTo(map);

var legend = L.control({ position: "bottomleft" });
legend.onAdd = function (map) {
  var div = L.DomUtil.create("div", "info legend");
  (labels = ["<strong>Federal Levels</strong>"]),
    (categories = [
      "City",
      "District",
      "Administrative district",
      "Federal state",
    ]);

  for (var i = 0; i < categories.length; i++) {
    div.innerHTML += labels.push(
      '<i class="bi bi-circle-fill" style="color:' +
        getColor(categories[i]) +
        '" ></i> ' +
        (categories[i] ? categories[i] : "+")
    );
  }
  div.style.backgroundColor = "rgba(255, 255, 255, 0.7)";
  div.innerHTML = labels.join("<br>");
  return div;
};

legend.addTo(map);

function getColor(d) {
  return d === "City"
    ? "#3A27D0"
    : d === "District"
    ? "#f04b23"
    : d === "Administrative district"
    ? "#ffcc00"
    : d === "Federal state"
    ? "#469F4E"
    : "#ff7f00";
}
