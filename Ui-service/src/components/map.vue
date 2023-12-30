<template>
  <div class="map-container">
    <l-map style="height: 100vh; width: 100vw;" :zoom="zoom" :center="center">
      <l-tile-layer :url="url"></l-tile-layer>
      <l-marker v-for="clinic in clinics" :key="clinic._id"
        :lat-lng="{ lat: clinic.location.latitude, lng: clinic.location.longitude }" @click="onClinicClick(clinic)">
        <l-popup>
          <div class="popup-content">
            <h3>{{ clinic.name }}</h3>
            <p>{{ clinic.address }}</p>
          </div>
        </l-popup>
      </l-marker>
    </l-map>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { LMap, LTileLayer, LMarker, LPopup } from 'vue3-leaflet';
import 'leaflet/dist/leaflet.css';

const BASE_URL = 'http://localhost:5000/clinics/';

export default {
  components: {
    LMap,
    LTileLayer,
    LMarker,
    LPopup
  },
  setup() {
    const clinics = ref([]);
    const center = ref([57.7089, 11.9746]);
    const zoom = ref(13);
    const selectedClinic = ref(null);

    onMounted(async () => {
      try {
        const data = await getAllClinics();
        clinics.value = data;
        console.log("Clinics: ", clinics.value);
        getUserLocation();
      } catch (error) {
        console.error('Error:', error);
      }
    });

    async function getAllClinics() {
      try {
        const response = await axios.get(BASE_URL);
        console.log("Data: ", response.data)
        return response.data;
      } catch (error) {
        console.error('Error fetching clinics:', error);
        throw error;
      }
    }

    function getUserLocation() {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
          (position) => {
            center.value = [position.coords.latitude, position.coords.longitude];
          },
          () => {
            console.error('Permission denied or error retrieving location');
          }
        );
      } else {
        console.error('Geolocation is not supported by this browser.');
        // Handle error or set a default center
      }
    }
    function onClinicClick(clinic) {
      selectedClinic.value = clinic;
    }

    return {
      clinics,
      center,
      zoom,
      url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
      selectedClinic,
      onClinicClick
    };
  }
};
</script>

<style scoped>
.map-container {
  display: flex;
  justify-content: center;
  margin-top: 5%;
  height: 50vh;
}
</style>
