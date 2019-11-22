
<template>
  <div>      
         <h5>{{userData.name}}</h5>
        <p>Followers: {{userData.followers}}</p>
        <p v-if="userData.company" >Company: {{userData.company}}</p>
        <p>Bio: {{userData.bio}}</p>
      
  </div>
</template>

<script>
export default {
  data: function() {
      return{
      }
  },
  props:{
      userData: Object
  },
  methods: {
  
  }
}
</script>

<style>
</style>
