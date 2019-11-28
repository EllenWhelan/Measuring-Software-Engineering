<template>
    <div class=body>
        <!-- Language BUtton gets num of lang from length of array of enumerable items in count object -->
        <button type=submit class=langCntButton>Language Count:{{Object.keys(this.count).length}} </button>
        <button type=submit class=follCntButton >Follower Count: {{ userData.followers}} </button>
        <p> Languages Mastered  vs       Follower Count </p>
    </div>
</template>

<script>
export default {
  data: function(){
        return {
            count: Object,
            userData: null,
        }
    },
  props:{
      userName: String
  },
  watch: {
        userName: function() {
            this.getLanguages()
        }
    },
    created: function() {
        this.getLanguages()
    },
  methods: {
      //method to find a user and return user data given a user login
      findUser: function() {
      if(this.userName != ""){
        this.$octokit.users.getByUsername({
          username: this.userName
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
      //this method is working
       getLanguages() {
          this.findUser()
          let promises=[];
          //let count=[];
           this.$octokit.repos.listForUser({ username: this.userName}) //list all repos first 
           .then(res =>{ //where res is obj of repos
                let userRepos = res.data.map(e => e.name); //make userRepos=array of repo names
                //iterate through each e repo in userRepos and for each e list langauges and put in lang array
                userRepos.forEach(e => {promises.push(this.$octokit.repos.listLanguages({ owner: this.userName,repo: e}))
                })
                 Promise.all(promises).then(repoStats => {
                    this.count = Object()
                    repoStats.map(e =>    
                            e.data
                    ).filter(e => 
                        Object.keys(e).length
                    ).forEach(e => {
                        for(let i of Object.keys(e)){
                            if(i in this.count){
                                this.count[i] += e[i]
                            }else{
                                this.count[i] = e[i]
                            }
                        }
                    })
                   
                   
                })
            })
      },

   
  }
  
}
</script>

<style >

.body{
    border: 2px solid ;
    position: static;
}

.langCntButton{
    width:200px;
    height: 200px; 
    margin:1%;
    padding-left:0%;
    position:relative;
    color: rgb(61, 59, 59);
  text-align: center;
  text-anchor: end;
  transition: all 0.2s;
  background-color:rgb(61, 59, 59);
    
}
/* on hovering over button the text will appear  */
.langCntButton:hover{
  background-color:whitesmoke;
}

.follCntButton{
    width:200px;
    height: 200px;
    margin:1%;
    padding-left:0%;
    position:relative;
    color: rgb(61, 59, 59);
  text-align: center;
  text-anchor: end;
  transition: all 0.2s;
  background-color:rgb(61, 59, 59);   
}

.follCntButton:hover{ 
  background-color:whitesmoke;
}
</style>