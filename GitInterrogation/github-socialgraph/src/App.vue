<template>
  <div id="app" class="pt-1">
    <!-- Below this is welcome page and search stuff-->
      <WelcomePage v-if="!landed" v-on:click.native="landed=true"></WelcomePage>
    <div v-if="landed" class="navbar navbar-expand-lg navbar-light bg-light mb-2">
        <!-- <div class="btn-group btn-group-toggle" data-toggle="buttons">
          <label class="btn btn-secondary" v-bind:class="{active: page.active}" v-for="page in pages" v-bind:key="page.id">
              <input type="button" name="options" v-bind:id="'nav-button-'+page.id" autocomplete="off" v-on:click="changePage(page)"> {{page.name}}
          </label>
        </div> -->
        <div class="form-inline ml-auto" v-if=pages[0].active>
          <form @submit.prevent>
            <input class="form-control mr-sm-2" type="search" placeholder="Username" v-model="currentUser" id="user_search">
            <button class="btn my-2 my-sm-0" type="submit" id="search_button" v-on:click=";loadingUser = true;findUser(); changePage(pages[1])" :class="error ? 'btn-outline-danger' : 'btn-outline-primary'">
              <span v-if="loadingUser" class="spinner-border spinner-border-sm mr-2" role="status" aria-hidden="true"></span>Search</button>
              </form>
        </div>
      </div>
      <!-- below this is graphs and profile stuff-->
     <div class="d-flex flex-row pl-2" v-if="userData && pages[1].active">
        <div class="d-flex flex-column flex-wrap fade-in-left">
          <UserProfile v-bind:userData="userData"></UserProfile>
        </div>
      </div>
      <div v-if=pages[1].active>
        <button type="button" v-on:click="changePage(pages[0])"></button>
      </div> 
      <b-alert
      v-model="error"
      class="position-fixed fixed-bottom m-0 rounded-0"
      style="z-index: 2000;"
      variant="danger"
      dismissible
    >
      An error has occured! Your last gitApi request failed. Try a different username or maybe re-connect to the network.
    </b-alert>
        
  </div>
</template>

<script>
import WelcomePage from './components/WelcomPage.vue'
import UserProfile from './components/UserProfile.vue'
export default {
  name: 'app',
  components: {
    UserProfile,
    WelcomePage
  },
  data: function() {
    return {
       pages: [{name: "SearchPage", id: 0, active: true},
              {name: "DataPage", id: 1, active: false}
              ],
     currentUser:"",
     userData: null,
     loadingUser: false,
     error: false, 
     landed: false
    }
  },
  methods: {
    changePage: function(page){
      this.pages.forEach(p => {
        if(p.id == page.id){
          p.active = true
        }else{
          p.active = false
        }
      })
    },
   findUser: function() {
      if(this.currentUser != ""){
        this.$octokit.users.getByUsername({
          username: this.currentUser
        }).then((res) => {
          this.loadingUser = false
          this.error = false
          this.userData = res.data
        }).catch(err => {
          //eslint-disable-next-line
          console.log(err)
          this.loadingUser = false
          this.error = true
        })
      }
    },
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
