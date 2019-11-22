<template>
<div id="app">
      <p class="heading">Social Graph</p>
      <p class="subheading">Welcome</p>
      
</div>
</template>

<script>
export default {
  name: 'WelcomePage',
  props: {
    msg: String
  }
}
</script>

<style>
#app{
  height: 100%;
  background-color: black;
}
.body{
  background-color :black;
}

.heading{
  color: whitesmoke;
  font-family: Garamond, Baskerville, "Baskerville Old Face", "Hoefler Text", "Times New Roman", serif;
  font-size: 120px;
  width:auto;
  background-color:black;
  
}
.subheading{
  font-family: "Gill Sans", "Gill Sans MT", Calibri, sans-serif;
  color: whitesmoke;
  background-color: black;

}

</style>