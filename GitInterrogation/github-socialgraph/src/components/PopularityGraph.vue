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
           //return graphData;
    },

     createPopGraph(){
          let popChart= d3.select("#my_dataviz")

        let margin = {top: 10, right: 30, bottom: 30, left: 60};
        let  width = 460 - margin.left - margin.right;
        let  height = 400 - margin.top - margin.bottom;

        // append the svg object to the body of the page
        svg = d3.select("#pop_chart")
        .append("svg")
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
        .append("g")
            .attr("transform",
                "translate(" + margin.left + "," + margin.top + ")");

        let data = getGraphData(); //this fucntion combines data of language count of a user and that users follower  into an object
        let color= d3.scaleOrdinal().domain(data).range(d3.schemeSet2)

        // Add X axis
        let x = d3.scaleLinear()
            .domain(data)
            .range([ 0, width ]);
        svg.append("g")
            .attr("transform", "translate(0," + height + ")")
            .call(d3.axisBottom(x));

        // Add Y axis
        var y = d3.scaleLinear()
            .domain(data)
            .range([ height, 0]);
        svg.append("g")
            .call(d3.axisLeft(y));

        // Add dots
        svg.append('g')
            .selectAll("dot")
            .data(data)
            .enter()
            .append("circle")
            .attr("cx", function (d) { return x(d.followerCount); } )
            .attr("cy", function (d) { return y(d.langaugeCount); } )
            .attr("r", 1.5)
            .style("fill", "#69b3a2")

    
        }


}
    
           
  
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