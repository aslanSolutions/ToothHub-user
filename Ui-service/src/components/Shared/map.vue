<template>
  <div class="map-container">
    <l-map v-if="isValidLatLng(center)" style="height: 100vh; width: 100vw;" :zoom="zoom" :center="center">
      <l-tile-layer :url="url"></l-tile-layer>
      <l-marker v-for="clinic in clinics" :key="clinic._id"
        :lat-lng="{ lat: clinic.location.latitude, lng: clinic.location.longitude }" @click="onClinicClick(clinic)">
        <l-popup>
          <div class="popup-content">
            <h3>{{ clinic.name }}</h3>
            <p>{{ clinic.address }}</p>
            <button v-if="isPatientDashboardRoute" @click="chooseClinic(clinic)">
              {{ clinicChosen === clinic ? 'Chose' : 'Choose' }}
            </button>
          </div>
        </l-popup>
      </l-marker>
    </l-map>
  </div>
</template>

<script>
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
  data() {
    return {
      clinics: [],
      center: [57.7089, 11.9746],
      zoom: 70,
      selectedClinic: null,
      clinicChosen: null,
      isPatientDashboardRoute: false,
      url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
    };
  },
  methods: {
    isValidLatLng(location) {
      if (!location || location.length !== 2) {
        return false;
      }

      const [latitude, longitude] = location;

      if (typeof latitude !== 'number' || typeof longitude !== 'number' || isNaN(latitude) || isNaN(longitude)) {
        return false;
      }

      return true;
    },

    async getAllClinics() {
      try {
        const response = await axios.get(BASE_URL);
        return response.data;
      } catch (error) {
        console.error('Error fetching clinics:', error);
        throw error;
      }
    },

    async onMounted() {
      try {
        const data = await this.getAllClinics();
        this.clinics = data;
      } catch (error) {
        console.error('Error:', error);
      }
    },

    onRouteChange() {
      this.isPatientDashboardRoute = this.$route.name === 'Patient-Dashboard';
    },

    onClinicClick(clinic) {
      if (this.isPatientDashboardRoute) {
        this.selectedClinic = clinic;
      } else {
        console.log(`Clicked on clinic: ${clinic.name}`);
      }
    },
    chooseClinic(clinic) {
      this.clinicChosen = clinic;
      this.$emit('clinic-selected', this.clinicChosen.name);
    },
  },
  watch: {
    '$route.name': 'onRouteChange',
  },
  created() {
    this.onMounted();
    this.onRouteChange();
    setInterval(this.onMounted, 30000);
  },
};
</script>

<style scoped>
.map-container {
  display: flex;
  justify-content: center;
  margin-top: 5%;
  height: 50vh;
}

button {
  background: rgb(96, 187, 205);
  border: 2px solid;
  border-radius: 8px;
  font-size: 10px;
  color: #00000098;
  cursor: pointer;
  transition: color 0.3s;
  padding: 0.5rem 1rem;
}</style>
