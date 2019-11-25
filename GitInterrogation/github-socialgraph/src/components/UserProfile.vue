
<template>
<div class=prof>
<p class=heading>User Profile</p>  
  <div class=card> 
         <img v-bind:src="userData.avatar_url" alt="https://upload.wikimedia.org/wikipedia/commons/7/72/Default-welcomer.png" class="image">
        <h5 >{{userData.name}}</h5>
        <p >Followers: {{userData.followers}}</p>
        <p v-if="userData.company" >Company: {{userData.company}}</p>
        <p>Bio: {{userData.bio}}</p>
      
  </div>
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
.heading{
  color: rgb(46, 44, 44);
  font-family: Garamond, Baskerville, "Baskerville Old Face", "Hoefler Text", "Times New Roman", serif;
  font-size: 80px;
  width:auto;
  background-color:white;
  position: static;
  text-align: center;
  padding-bottom: 10%;
  
  
  
}
.card{
  color: rgb(46, 44, 44);;
  font-family: Garamond, Baskerville, "Baskerville Old Face", "Hoefler Text", "Times New Roman", serif;
  font-size: 20px;
  height:100%;
  width: auto;
  background-color:white;
  position: static;
  text-align: center;
  padding-bottom: 10%;
  border:3px solid rgb(153, 204, 255);
  height:100%;
  position: relative;
}
.image{
  height:40%;
}

</style>
