<template>
    <div class=body>
        <button type=submit class=langCntButton>Language Count: </button>
        <button type=submit class=follCntButton >Follower Count: {{ this.$octokit.users.getByUsername({ username: this.currentUser}).followers}} </button>
        <p> Languages Mastered  vs       Follower Count </p>
    </div>
</template>
<script>
export default {
//   name: 'LangFollfor1user',
  data: function(){
        return {
            count: Object,
            
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
      getLanguages() {
          let promises=[];
           this.$octokit.repos.listForUser({ username: this.userName}) //list all repos first 
           .then(res =>{ //where res is obj of repos
                let userRepos = res.data.map(e => e.name); //make userRepos=array of repo names
                //iterate through each e repo in userRepos and for each e list langauges and put in lang array
                userRepos.forEach(e => {promises.push(this.$octokit.repos.listLanguages({ owner: this.userName,repo: e}))
                })
                //return this.promises.data.length
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
.langCntButton:hover{
    
  background-color:whitesmoke;
  /* color:black; */

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
  /* color:black; */
}
</style>