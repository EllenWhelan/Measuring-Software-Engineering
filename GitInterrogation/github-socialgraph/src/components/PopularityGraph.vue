<template>
<div class=body>
    <h5>Popularity based on Following Count</h5>
    <div id="pop_chart"></div>
    </div>
</template>

<script>
 const d3 = require("d3")
export default {
data: function(){
        return {
            count: [], //array of languages
            graphData: [], // array of objects [{x1,y1}, {x2,y2}...{xn,yn}]
            
        }
        
    },
  props:{
      userName: String
  },
  watch: {
        userName: function() {
            this.getGraphData()
            
        }
    },
    created: function() {
        this.getGraphData()
        
    },
 
  methods: {
  
       getGraphData(){
       
          this.graphData=[]
          //takes user and attempts to get list of followers of that user 
          this.$octokit.users.listFollowersForUser({ username: this.userName})  
           .then(res =>{
               let followers = res.data.map(e => e.login); //map returned data to array of followers logins
                //creates temp array with [follower.followercount, follower.langCount] then pushes tempArray to graphdata
                let tempObj =Object();
                let tempUser= Object();
                //iterates through all users followers
                for (let i=0; i<followers.length; i+=1){
                    //gets user data of each follower[i] and initialises temp user
                    this.$octokit.users.getByUsername({ username: followers[i]})
                    .then(res =>{tempUser=res.data});
                    
                    //lists all repos of that follower
                    this.$octokit.repos.listForUser({username: followers[i]}.
                    then(res =>{
                        //maps user repos by their language to new array userRepos
                        let userRepos = res.data.map(e => e.language); 
                        this.count=[];
                        for( let i=0; i<userRepos.length; i+=1){
                            if(userRepos[i] in this.count ==false) this.count.push(userRepos[i]);
                                        
                         }
                         //create temporary object of followers name, their follow count and their language count
                        tempObj={name: tempUser.login, followCount:tempUser.followers, languageCount:this.count.length}; 
                        this.graphData.push(tempObj); //push this object to array graphData 
                    })
                    );   
                    
                }
                    
           
           this.createPOPScatter()
            
           })
      
    },
      

        
    createPOPScatter(){
    
        if(data!=null){
            var data = this.graphData
        }
        else{ //used for debugging purposes
            data= [{name: 'Ellen',followCount:4, languageCount:5}, {name:'John', followCount:3, languageCount:7}]
        }
        //eslint-disable-next-line
        console.log(data)
        let height=250
        let width=250

let svg = d3.select("body")
            .append("svg")
            .attr("width", width)
            .attr("height", height)

svg.selectAll("circle")
   .data(data).enter()
   .append("circle")
   .attr("cx", function(d) {return d.followCount})
   .attr("cy", function(d) {return d.languageCount})
   .attr("fill", function(d) {
     return "rgb("+d.followCount+","+d.languageCount+",0)"
   })

svg.selectAll("text")
  .data(data).enter()
  .append("text")
  .attr("x", function(d) {return d.followCount+10})
  .attr("y", function(d) {return d.languageCount+4})
  .attr("font-size", "10px")

        //Add X axis
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

    
    },
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
