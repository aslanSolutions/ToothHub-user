<template>
  <div class="container">
    <headerPhoto class="headerPhoto" />
    <textSection :text="textContent" />
    <div v-if="isLogged">
      <button v-if="isLoggedIn && (role === 'Admin')" class="btn btn-primary" @click="openEditModal">Edit Text</button>
      <div class="modal fade" id="editModal" tabindex="-1" role="dialog" aria-labelledby="editModalLabel"
        aria-hidden="true">
        <div class="modal-dialog" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="editModalLabel">Edit Text</h5>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body">
              <textarea v-model="textContent" class="form-control" rows="10" ></textarea>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
              <button @click="saveEditedText" class="btn btn-primary">Save changes</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import headerPhoto from '@/components/About/headerPhoto.vue'
import textSection from '@/components/About/textSection.vue'
//import { mapState } from 'vuex'
import { about } from '@/api/aboutApi'

export default {
  name: 'About',
  components: {
    headerPhoto,
    textSection,
  },
  //computed: {
    //...mapState(['isLoggedIn', 'role'])
  //},
  //created() {
    //this.getAboutUs()
  //},
  data() {
    return {
      textContent: "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum. It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).",
      editedText: '',
      isLogged: false
    }
  },
  methods: {
    openEditModal() {
      this.editedText = this.textContent
      /* global $ */
      $('#editModal').modal('show')
    },
    async saveEditedText() {
      const newText = {
        text: this.textContent
      }
      await about.updateAbout(newText)
      this.getAboutUs()
      $('#editModal').modal('hide')
    },
    async getAboutUs() {
      const textObject = await about.getAbout()
      this.textContent = textObject.data.text
    }
  }
}
</script>

<style>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 75px;
  padding-bottom: 80px;
}

.textSection {
  width: auto;
}
</style>