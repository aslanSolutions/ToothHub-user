import axios from 'axios'

const BASE_URL = 'http://localhost:5000/services'

export const services = {
  getAllServices() {
    return axios.get(`${BASE_URL}`)
  },

  getService(userId) {
    return axios.get(`${BASE_URL}/${userId}`)
  },

  createService(userData) {
    return axios.post(`${BASE_URL}`, userData)
  },

  updateService(userId, userData) {
    return axios.put(`${BASE_URL}/${userId}`, userData)
  },

  deleteService(userId) {
    return axios.delete(`${BASE_URL}/${userId}`)
  }
}
