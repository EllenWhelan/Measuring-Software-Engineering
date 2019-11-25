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