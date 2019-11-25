
<template>
<div class=prof>
  <div class=card> 
        <h5 class=header v-if="userData.name" >{{userData.name}}</h5>
        <h5 class=header v-if="!userData.name">{{userData.login}}</h5>
        <img v-bind:src="userData.avatar_url" alt="https://upload.wikimedia.org/wikipedia/commons/7/72/Default-welcomer.png" class="image">
        <p> Username: {{userData.login}}</p>
        <p > Followers: {{userData.followers}}</p>
        <p> Following: {{userData.following}}</p>
        <p> {{userData.type}}</p>
        <p v-if="userData.company" > Company: {{userData.company}}</p>
        <p v-if="!userData.company"> Company: Unknown </p>
        <p v-if="userData.Bio"> Bio: {{userData.bio}}</p>
        <p v-if="!userData.bio"> Bio: Unknown</p>
      
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

.card{
  color: rgb(46, 44, 44);;
  font-family: Garamond, Baskerville, "Baskerville Old Face", "Hoefler Text", "Times New Roman", serif;
  font-size: 20px;
  height:100%;
  width: auto;
  background-color:white;
  position: static;
  text-align:center;
  padding-bottom: 10%;
  border:2px solid rgb(153, 204, 255);
  height:100%;
  position: relative;
}
.image{
  height:40%;
  margin-left:0%;
  border: 2px solid rgb(153, 204, 255);
  border-radius: 50%;
  text-align: center;
}
.header{

  text-align: center;
}

</style>
