<template>
  <div class=langCard>
      <h5 class=headingSect>
              Language Breakdown
          </h5>
      <div >
          <div id="language_pichart" ></div>
      </div>
  </div>
</template>

<script>
const d3 = require("d3")
export default {
    name: "LanguagePi",
    data: function(){
        return {
            languagePercentages: null,
            
        }
    },
    props: {
        userName: String 
    },
    watch: {
        userName: function() {
            this.getLanguagePercentages()
        }
    },
    created: function() {
        this.getLanguagePercentages()
    },
     
    methods: {
        getLanguagePercentages() {
            let promises = [];
            this.$octokit.repos.listForUser({
                username: this.userName
            }).then(res => {
                let userRepos = res.data.map(e => e.name);
                userRepos.forEach(e => {
                    promises.push(this.$octokit.repos.listLanguages({
                        owner: this.userName,
                        repo: e
                    }))
                })
                Promise.all(promises).then(repoStats => {
                    this.languagePercentages = Object()
                    repoStats.map(e =>    
                            e.data
                    ).filter(e => 
                        Object.keys(e).length
                    ).forEach(e => {
                        for(let i of Object.keys(e)){
                            if(i in this.languagePercentages){
                                this.languagePercentages[i] += e[i]
                            }else{
                                this.languagePercentages[i] = e[i]
                            }
                        }
                    })
                   
                    this.makePiChart()
                })
            })
        },
        makePiChart() {
            let piChart = d3.select("#pie-graph")
            if(piChart){
                piChart.remove()
            }
            let width = window.innerHeight/0.5
            let height = window.innerHeight/1.7
            let margin = 10
            let radius = Math.min(width, height) / 2 - margin
            let svg = d3.select("#language_pichart")
                        .append("svg")
                          .attr("width", width)
                          .attr("height", height)
                        .attr("id", "pie-graph")
                        .append("g")
                          .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");
            let data = this.languagePercentages
            let color = d3.scaleOrdinal().domain(data).range(d3.schemeSet2)
            
            
            let pi = d3.pie()
                        .sort(null)
                        .value(function(d) {return d.value;})
            
        
            
            svg
                .selectAll('allSlices')
                .data(pi(d3.entries(data)))
                .enter()
                .append('path')
                .attr('d', d3.arc().innerRadius(radius * 0.025).outerRadius(radius * 0.8))
                .attr('fill', function(d){ return(color(d.data.key)) })
                .attr("stroke", "white")
                .style("stroke-width", "2px")
                .style("opacity", 0.65)
            
            svg.selectAll("circleKeys")
                .data(Object.keys(data))
                .enter()
                .append("circle")
                .attr("cx", function(d,i){return -200 + i*100})
                .attr("cy", 175)
                .attr("r", 5)
                .style("fill", function(d){return color(d)})
            svg.selectAll("labels")
               .data(Object.keys(data))
               .enter()
               .append("text")
               .attr("x", function(d,i){return -210 + i*100})
               .attr("y", 180)
               .style("fill", function(d){return color(d)})
               .text(function(d){return d})
               .attr("text-anchor", "end")
               .style("alignment-baseline", "alphabetic")    
        }
    }
}

</script>

<style>
.langCard{
    margin-top: 10px;
    margin-bottom: 10px;
    border:2px solid rgb(153, 204, 255);
    text-align: center;
    font-size: 20px;
    font-style:normal;
    color: rgb(46, 44, 44);
    font-family:Garamond, Baskerville, "Baskerville Old Face", "Hoefler Text", "Times New Roman", serif;
}

.headingSect{
  color: rgb(46, 44, 44);;
  font-family: Garamond, Baskerville, "Baskerville Old Face", "Hoefler Text", "Times New Roman", serif;
  font-size: 20px;
  font-style:normal;
  font-weight:100;
}
</style>
