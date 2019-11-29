<template>
<div id="app">
      <p class="heading">Social Graph</p>
      <p class="subheading">Welcome, click to enter.</p>
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
  background-color: white;
}
.body{
  background-color :white;
}

.heading{
  color: rgb(46, 44, 44);;
  font-family: Garamond, Baskerville, "Baskerville Old Face", "Hoefler Text", "Times New Roman", serif;
  font-size: 120px;
  width:auto;
  background-color:white;
  position: static;
  text-align: center;
  top: 100px;
  
  
  
}
.subheading{
  font-family: "Gill Sans", "Gill Sans MT", Calibri, sans-serif;
  color: rgb(100, 99, 99);
  background-color: white;
  position: static;
  left: 30px;
  text-align: center;
  font-size: 40px;
  

}

</style>