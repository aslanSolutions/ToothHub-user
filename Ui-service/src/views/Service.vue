<!-- * The "Service" component represents a view that displays a collection of services. It allows patient to choose a service and booke it and allows dentists to add, edit, and delete services.
* This component includes child components for displaying individual service cards and service management forms. -->
<template>
  <div :class="{ 'container': true, 'blur-background': showModel }">
    <headerPhoto />
    <div class="serviceCard">
      <div v-if="isLoading" class="loading-circle">
        <i class="fas fa-spinner fa-spin"></i> Loading...
      </div>
      <serviceCard
      v-for="service in services"
      :key="service._id" :service="service"
      @service-deleted="handleServiceDeleted"
      @edit-service="handleEditService"
      />
      <!-- * <div class="holder" v-if="isLoggedIn && (role === 'Admin')">
        <button class="rectangle-button" @click="showFormModel">
          <i class="fas fa-plus"></i>
        </button>
      </div>
      -->
    </div>
    <serviceForm :showModel="showModel" @close-modal="closeModal" @fetch-services="fetchServices"/>
    <serviceUpdate :showEdit="showEdit" :currentService="editingService" @close-modal="closeModal" @fetch-services="fetchServices" />
  </div>
</template>

<script>
import { services } from '@/api/serviceApi'
import serviceCard from '@/components/Service/serviceCard.vue'
import headerPhoto from '@/components/Service/headerPhoto.vue'
import serviceForm from '@/components/Service/serviceForm.vue'
import serviceUpdate from '@/components/Service/serviceUpdate.vue'
import '@fortawesome/fontawesome-free/css/all.css';
// import { mapState } from 'vuex'

export default {
  name: 'Service',
  components: {
    serviceCard,
    headerPhoto,
    serviceForm,
    serviceUpdate
  },
  //computed: {
    //...mapState(['isLoggedIn', 'role'])
  //},
  data() {
    return {
      services: [],
      showModel: false,
      showEdit: false,
      editingService: null,
      form: null,
      isLoading: true
    }
  },

  async created() {
    await this.fetchServices()
  },

  methods: {
    async handleServiceDeleted(serviceId) {
      this.services = this.services.filter(service => service._id !== serviceId)
    },
    async fetchServices() {
      try {
        const response = await services.getAllServices()
        this.services = response.data
        console.log(response)
        this.isLoading = false
      } catch (error) {
        console.error('Error fetching services:', error)
      }
    },
    showFormModel() {
      this.showModel = true
    },
    closeModal() {
      this.showModel = false
      this.showEdit = false
    },
    handleEditService(service) {
      this.editingService = service
      this.showEdit = true
    }
  }
}
</script>

<style>

.container.blur-background .serviceCard{
  filter: blur(10px);
}

.serviceCard{
  padding-top: 50px;
  margin-left:10%;
  margin-right:10%;
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
  flex-flow: wrap;
  gap: 50px;
}

.container{
  padding-top: 170px;
  padding-bottom: 60px;
  display: flex;
  flex-direction: column;
}

.rectangle-button {
  width: 100px;
  height: 80px;
  background-color: #3498db;
  border: none;
  color: white;
  border-radius: 5px;
}

.holder {
  display: flex;
  justify-content: center;
  align-items: center;
  max-width: 300px;
  width: max(7rem, 350px);
  height: max(9rem, 350px);
  box-shadow: 0px 4px 50px 0px rgba(0, 0, 0, 0.07);
  backdrop-filter: blur(10px);
}
.loading-circle {
  z-index: 1;
  margin-bottom: 15%;
}

.loading-circle i {
  font-size: 150px;
  color: #3498db;
}
</style>
