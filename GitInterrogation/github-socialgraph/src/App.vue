<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">

    <div>
      <p> {{username}} </p>
      <input type="search" v-model="username">
      <button v-on:click="findUser()">search</button>
    </div>
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'app',
  data: function() {
    return {
     username:""
    }
  },
  methods: {
    findUser() {
      this.$octokit.users.getByUsername({
        username: this.username
      }).then(function(response){
        //eslint-disable-next-line
        console.log(response)
      }).catch(function(err) {
        //eslint-disable-next-line
        console.log(err)
      }) //function(response) {}
      return
    }
  }
  
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
