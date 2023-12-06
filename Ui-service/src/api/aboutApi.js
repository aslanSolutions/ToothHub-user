import axios from 'axios'

const BASE_URL = 'http://localhost:5000/abouts/652d834f4e05702075eabc4f'

export const about = {
  updateAbout(userData) {
    return axios.put(BASE_URL, userData)
  },
  getAbout(userData) {
    return axios.put(BASE_URL, userData)
  }
}
