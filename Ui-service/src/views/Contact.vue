<!--
* The "ContactUs" component is responsible for displaying the contact information.
-->
<template>
    <div class="container">
        <contactPhoto class="photo"/>
        <messageBoxNonUser class="message"/>
        <!--<messageBox v-if="isLoggedIn" class="message"/>-->
    </div>
</template>

<script>
import contactPhoto from '@/components/Contact/contactInfo.vue'
import messageBoxNonUser from '@/components/Contact/messageBoxNonUser.vue'
//import messageBox from '@/components/Contact/messageBox.vue'
//import { mapState } from 'vuex'

export default {
  name: 'Contact',
  //computed: {
    //...mapState(['isLoggedIn', 'role'])
  //},
  components: {
    contactPhoto,
    messageBoxNonUser
    //messageBox
  }
}
</script>

<style scoped>
.container {
  padding-top: 200px;
  display: flex;
  flex-direction: row;
  margin-bottom: 100px;
  padding-left: 2%;
}

.message{
  margin-top: 20px;
  padding-left: 1rem;
}

@media (max-width: 768px) {
  .container {
    padding-top: 8rem;
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    margin-bottom: 100px;
  }
}
</style>
