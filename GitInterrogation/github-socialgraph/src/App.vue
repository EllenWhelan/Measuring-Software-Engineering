<template>
  <div id="app" class="pt-1">
    <!-- Below this is welcome page and search stuff-->
      <WelcomePage v-if="!landed" v-on:click.native="landed=true"></WelcomePage>
    <div v-if="landed" class="navbar navbar-expand-lg navbar-light bg-light mb-2">
        <div class="form-inline ml-auto" v-if=pages[0].active>
          <p class=head> GitHub User Search</p>
          <form @submit.prevent>
            <input class="srch" type="search" placeholder="Enter a Username" v-model="currentUser" id="user_search">
            <button content="Return" class="btn" type="submit" id="search_button" v-on:click=";loadingUser = true;findUser(); changePage(pages[1])" >
              <span v-if="loadingUser" class="spinner-border spinner-border-sm mr-2" role="status" aria-hidden="true"></span>Search</button>
              </form>
        </div>
      </div>
      <!-- below this is graphs and profile stuff-->
     <div v-if="userData && pages[1].active">
        <div>
          <p class=headingProfile>User Profile</p>  
          <p> This project aims to explore the link between the laguages known by a GitHub user and that users popularity. 
            The following graphs compare languages of users and the amount of stars they have, as well as the amount of followers. </p>
          <UserProfile v-bind:userData="userData"></UserProfile>
          <LanguagePi v-bind:userName="userData.login"></LanguagePi>
          <p> This graph breaks down all the code in {{userData.login}}'s Repositories into languages. 
            It shows clearly the different languages {{userData.login}} is familar with and how much they use each language.</p>
            <LanguageFollowerFor1User v-bind:userName="userData.login"></LanguageFollowerFor1User>
            <PopularityGraph v-bind:userName="userData.login"></PopularityGraph>
        </div> 
        
      </div>
      <!-- This is button to return to search page -->
      <div v-if=pages[1].active>
        <button class=btn2 type="button" v-on:click="changePage(pages[0])"> Back To Search </button>
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
import LanguagePi from './components/LanguagePi.vue'
import LanguageFollowerFor1User from './components/LanguageFollowerFor1User'
import PopularityGraph from './components/PopularityGraph'
export default {
  name: 'app',
  components: {
    UserProfile,
    WelcomePage,
    LanguagePi,
    LanguageFollowerFor1User,
    PopularityGraph
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
  font-family: Garamond, Baskerville, "Baskerville Old Face", "Hoefler Text", "Times New Roman", serif;
  color: rgb(100, 99, 99);
  text-align: center;
  color: #2c3e50;
  margin-top: 20%; 
} 
.head{
  font-family: Garamond, Baskerville, "Baskerville Old Face", "Hoefler Text", "Times New Roman", serif;
  color: rgb(100, 99, 99);
  font-size: 40px;
  text-align: center;
  margin: 0%;
}
.btn{
  font-family: Garamond, Baskerville, "Baskerville Old Face", "Hoefler Text", "Times New Roman", serif;
  color: white;
  text-align: center;
  transition: all 0.2s;
  background-color:rgb(61, 59, 59);
  display: inline-block;
  padding:0.35em 1.2em;
  border:0.1em solid #FFFFFF;
  margin:0 0.3em 0.3em 0;
  border-radius:0 5px 5px 0;
  box-sizing: border-box;

}
.btn:hover{
  background-color:whitesmoke;
  color:black;
}
@media all and (max-width:30em){
  btn{
    display:block;
    margin:0.4em auto;
  }
}

.srch{
  border: 1px solid rgb(61, 59, 59);
  border-radius: 5px 0 0 5px;
  height: 25px;
  /* padding:0.35em 1.2em; */
}

.btn2{
  background: rgb(61, 59, 59);
  width: 180px;
  padding: 4px 0;
  margin-bottom:25%;
  margin-top:15%;
  position: static;
  left: 50%;
  top: 50%;
  border-radius: 5px 5px 5px 5px;
  border: 1px solid rgb(61, 59, 59);
  color: white;
  font-family: Garamond, Baskerville, "Baskerville Old Face", "Hoefler Text", "Times New Roman", serif;
  color: white;
  font-size: 15px;
  font-weight:10;


  
}
.headingProfile{
  color: rgb(46, 44, 44);
  font-family: Garamond, Baskerville, "Baskerville Old Face", "Hoefler Text", "Times New Roman", serif;
  font-size: 80px;
  background-color:white;
  position: static;
  text-align: center;
  padding-bottom: 0%;
 padding-top:0%;
 margin:0%;
  
  
}



</style> 
