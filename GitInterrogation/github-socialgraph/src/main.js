import Vue from 'vue'
import App from './App.vue'
import Octokit from "@octokit/rest"
import BootstrapVue from 'bootstrap-vue'

require("dotenv").config()
//eslint-disable-next-line
console.log(process.env)
const octokit = Octokit({ //create ocotkit object
 
  auth: `token ${process.env.VUE_APP_GITHUB_TOKEN}`, //git auth token in .env file 
  userAgent: 'github vis'
})

Vue.config.productionTip = false
Vue.prototype.$octokit = octokit //made oktokit global this.
Vue.use(BootstrapVue)

new Vue({
  render: h => h(App),
}).$mount('#app')
