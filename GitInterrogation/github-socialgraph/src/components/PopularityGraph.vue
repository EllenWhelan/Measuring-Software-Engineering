<template>
<div class=body>
    <h5>Popularity based on Following Count</h5>
    <div id="pop_chart"></div>
    </div>
</template>

<script>
export default {
data: function(){
        return {
            count: Object,
            graphData: Object,
            
        }
    },
  props:{
      userName: String
  },
 
  methods: {
      getLanguages(user) {
          let promises=[];
           this.$octokit.repos.listForUser({ username: user.userName}) //list all repos first 
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
                            this.count[i]=e[i];
                            // if(i in this.count){
                            //     this.count[i] += e[i]
                            // }else{
                            //     this.count[i] = e[i]
                            // }
                        }
                    })
                
                    //this is causing major problems 
                })
            })
      },

    getGraphData(){
       
          graphData=Object()
          //takes user and attempts to get list of followers of that user 
          this.$octokit.users.listFollowersForUser({ username: this.userName}) //list all followers of user first 
           .then(res =>{
               let followers = res.data.map(e => e.name); //map returned data to array
                //iterate through each e follower in followers and for each e list langauges they have and put in graph data
                followers.forEach(e => {graphData.push(getLanguages(e))})
                //also add follower data
                followers.forEach(e=> {graphData.push(e.followers)})
           }
    }
},
    
           
  
}
  


</script>

<style>
.body{
    margin-top: 10px;
    margin-bottom: 10px;
    border:2px solid rgb(153, 204, 255);
    text-align: center;
    font-size: 20px;
    font-style:normal;
    color: rgb(46, 44, 44);
    font-family:Garamond, Baskerville, "Baskerville Old Face", "Hoefler Text", "Times New Roman", serif;
}
</style>