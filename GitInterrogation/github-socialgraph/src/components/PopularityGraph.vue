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
//       getLanguages(user) {
//           let promises=[];
//            this.$octokit.repos.listForUser({ username: user.userName}) //list all repos first 
//            .then(res =>{ //where res is obj of repos
//                 let userRepos = res.data.map(e => e.name); //make userRepos=array of repo names
//                 //iterate through each e repo in userRepos and for each e list langauges and put in lang array
//                 userRepos.forEach(e => {promises.push(this.$octokit.repos.listLanguages({ owner: this.userName,repo: e}))
//                 })
//                 //return this.promises.data.length
//                 Promise.all(promises).then(repoStats => {
//                     this.count = Object()
//                     repoStats.map(e =>    
//                             e.data
//                     ).filter(e => 
//                         Object.keys(e).length
//                     ).forEach(e => {
//                         for(let i of Object.keys(e)){
//                             if(i in this.count){
//                                 this.count[i] += e[i]
//                             }else{
//                                 this.count[i] = e[i]
//                             }
//                         }
//                     })
                
//                     //this is causing major problems 
//                 })
//             })
//       },


      


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