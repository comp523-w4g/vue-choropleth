<template>
  <div id="app">
    <ChoroplethMap :data="ncCountyData" titleKey="county_name" idKey="county_id" :value="value" :extraValues="extraValues" geojsonIdKey="county_id" :geojson="ncGeojson" :center="center" :colorScale="colorScale" mapStyle="height: 500px;" :zoom="1" :mapOptions="mapOptions">
      <template scope="props">
        <InfoControl :item="props.currentItem" :unit="props.unit" title="Department" placeholder="Hover over a department"></InfoControl>
        <ReferenceChart title="Girls school enrolment" :colorScale="colorScale" :min="props.min" :max="props.max" position="topright"></ReferenceChart>
      </template>
    </ChoroplethMap>
  </div>
</template>

<script>
import { ChoroplethMap, InfoControl, ReferenceChart } from 'vue-choropleth'
// import { geojson } from './data/py-departments-geojson'
// import paraguayGeojson from './data/paraguay.json'
import ncCountyData from './data/ncCountyData'
import ncGeojson from './data/ncgeo.json'

export default {
  name: "app",
  components: { ChoroplethMap, InfoControl, ReferenceChart },
  data() {
    return {
      center: [-78.890317, 35.867830999999995],
      ncCountyData,
      ncGeojson,
      colorScale: ["e7d090", "e9ae7b", "de7062"],
      value: {
        key: "amount_w",
        metric: "% girls"
      },
      extraValues: [{
        key: "amount_m",
        metric: "% boys"
      }],
      mapOptions: {
        attributionControl: false
      }
    }
  }
}
</script>
<style>
@import "../node_modules/leaflet/dist/leaflet.css";
body {
  background-color: #e7d090;
  margin-left: 100px;
  margin-right: 100px;
}

#map {
  background-color: #eee;
}
</style>
