<template>
  <div class="modal-overlay" v-if="showModel">
    <div class="modal-content">
      <div class="form-container">
        <form @submit.prevent="handleSubmit">
          <div class="form-group">
            <label for="name">Name:</label>
            <input v-model="form.name" type="text" id="name" required />
          </div>

          <div class="form-group">
            <label for="price">Price:</label>
            <input v-model="form.price" type="number" id="price" required />
          </div>

          <div class="form-group">
            <label for="description">Description:</label>
            <textarea v-model="form.description" id="description" required></textarea>
          </div>

          <div class="form-group">
            <label for="image">Upload Image:</label>
            <input type="file" @change="handleImageUpload" accept="image/*" id="image" required />
          </div>
          <button type="submit">Save</button>
          <button class="close-button" @click="closeModal">Cancel</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import { services } from '@/api/serviceApi'

export default {
  props: ['showModel'],
  data() {
    return {
      form: {
        name: '',
        price: null,
        description: '',
        duration: null,
        image: null
      }
    }
  },
  methods: {
    handleImageUpload(event) {
      const file = event.target.files[0]
      this.form.image = file
    },
    handleSubmit() {
      const formData = new FormData()
      formData.append('name', this.form.name)
      formData.append('price', this.form.price)
      formData.append('description', this.form.description)
      formData.append('duration', this.form.duration)
      formData.append('image', this.form.image)

      services.createService(formData)
        .then(() => {
          this.$emit('close-modal')
          this.$emit('fetch-services')
        })
        .catch(error => {
          console.error('Error adding service:', error)
        })
    },
    closeModal() {
      this.$emit('close-modal')
    }
  }
}
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
}

.modal-content {
  background: white;
  padding: 20px;
  border-radius: 10px;
  max-width: 80%;
  margin-top: 60px;
}

.form-container {
  max-width: 400px;
  width: 100%;
}

.form-group {
  margin-bottom: 10px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
}

.form-group input,
.form-group textarea {
  width: calc(100% - 20px);
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 5px;
  resize: none;
}

button {
  padding: 10px 20px;
  background-color: #3498db;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #2980b9;
}

.close-button {
  margin-top: 10px;
  margin-left: 10px;
}
</style>
