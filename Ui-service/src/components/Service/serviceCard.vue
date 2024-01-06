<template>
  <div class="service-card">
    <img :src="decodeImage(service.image)" alt="Service Image" />
    <div class="NamePrice">
      <h2 class="name">{{ service.name }}</h2>
      <p class="price">${{ service.price }}</p>
    </div>
    <p class="description">{{ service.description }}</p>
  </div>
</template>

<script>
import { services } from '@/api/serviceApi'

export default {
  props: {
    service: {
      type: Object,
      required: true
    }
  },
  methods: {
    decodeImage(base64Data) {
      if (base64Data) {
        return 'data:image/png;base64,' + base64Data;
      }
      return null;
    },
    async handleDelete() {
      const confirmation = window.confirm('Do you really want to delete?')
      if (confirmation) {
        try {
          await services.deleteService(this.service._id)
          console.log('service deleted')
          this.$emit('service-deleted', this.service._id)
        } catch (error) {
          console.error('Error fetching services:', error)
        }
      }
    },
    async handleEdit() {
      this.$emit('edit-service', this.service)
    }
  }
}
</script>

<style scoped>
.service-card {
  display: flex;
  flex-direction: column;
  background-color: rgb(255, 255, 255);
  max-width: 300px;
  width: 100%;
  min-height: fill;
  height: 450px;
  box-shadow: 0px 4px 50px 0px rgba(0, 0, 0, 0.07);
  backdrop-filter: blur(10px);
  border-top-left-radius: 30px; 
  border-top-right-radius: 30px; 
}

.service-card img {
  max-width: fill;
  max-height: 25rem;
}

.name {
  font-size: max(1.0rem, 17px);
  font-weight: 650;
  color: rgba(73, 135, 161, 1)
}

.NamePrice {
  margin-top: 5%;
  margin-left: 8%;
  margin-right: 8%;
  display: flex;
  align-items: baseline;
  justify-content: space-between;
}

.price {
  color: rgba(73, 135, 161, 1); 
  font-size: max(0.9vw, 12px);
  letter-spacing: 0em;
  font-weight: 650;
}

.description {
  display: flex;
  justify-content: center;
  color: rgba(136, 135, 143, 1);
  font-weight: 400;
  font-size: max(0.8vw, 13px);
  padding-top: 5%;
  padding-bottom: 5%;
  padding-left: 5%;
  padding-right: 5%;
}


.booking {
  height: 50px;
  width: 180px;
  max-width: 180px;
  max-height: 50px;
  background: rgba(73, 135, 161, 1);
  color: rgba(255, 255, 255, 1);
  border: none;
}

.booking:hover {
  background: rgb(255, 162, 0);
}

.delete-button {
  position: absolute;
  border-radius: 20px;
  padding: 8px;
  cursor: pointer;
  font-size: 23px;
}

.delete-button i {
  color: rgb(255, 136, 0);
  transition: color 0.3s ease-in-out;
}

.delete-button:hover i {
  color: red;
  font-size: 30px;
}

@media (max-width: 768px) {
  .service-card {
    width: min(100%, 8rem);
    height: fill;
  }

  .service-card img {
    width: fill;
    height: fill;
  }

  .booking {
    max-width: 3rem;
    max-height: 2rem;
    font-size: 0.7rem;
  }

  .description {
    font-size: min(1.8vw, 11px);
    line-height: min(2vw, 8px);
  }
}
</style>
