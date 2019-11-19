import Vue from 'vue'
import App from './App.vue'
import Octokit from "@octokit/rest"

require("dotenv").config()

const octokit = Octokit({ //create ocotkit object
  auth: `token ${process.env.VUE_APP_GIT_TOKEN}`, //gen tkoen in .env file 
  userAgent: 'github vis'
})

Vue.config.productionTip = false
Vue.prototype.$octokit = octokit //made oktokit global this.


new Vue({
  render: h => h(App),
}).$mount('#app')
