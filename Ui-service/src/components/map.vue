<template>
    <div>
      <MglMap
        :accessToken="mapboxAccessToken"
        :mapStyle="mapStyle"
        :center="center"
        :zoom="zoom"
        style="height: 400px; width: 100%;"
      >
        <MglMarker
          v-for="clinic in clinics"
          :key="clinic.id"
          :lngLat="[clinic.longitude, clinic.latitude]"
        >
          <div>{{ clinic.name }}</div>
        </MglMarker>
      </MglMap>
    </div>
  </template>
  
  <script>
  import { ref, onMounted } from 'vue';
  import axios from 'axios';
  import { MglMap, MglMarker } from 'vue-mapbox';
  
  const BASE_URL = 'http://localhost:5000/clinics/';
  
  export default {
    components: {
      MglMap,
      MglMarker,
    },
    setup() {
      const clinics = ref([]);
  
      onMounted(async () => {
        try {
          clinics.value = await getAllClinics();
        } catch (error) {
          console.error('Error:', error);
        }
      });
  
      return { clinics };
    },
    methods: {
      getAllClinics: async () => {
        try {
          const response = await axios.get(BASE_URL);
          return response.data;
        } catch (error) {
          console.error('Error fetching clinics:', error);
          throw error;
        }
      },
    },
    data() {
      return {
        mapboxAccessToken: 'pk.eyJ1IjoiZ3VjY2licmFnYSIsImEiOiJjbHFtamY1M28yajI3Mml0a3BpMjF2a3BhIn0.0WPtfrTGre_3Y-NYQQfw3A', 
        mapStyle: 'mapbox://styles/mapbox/streets-v11',
        center: [57.7, 11.9],
        zoom: 9,
      };
    },
  };
  </script>
  
  <style>
  </style>
  