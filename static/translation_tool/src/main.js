import '@babel/polyfill'
import 'mutationobserver-shim'
import 'bootstrap'; // Import js file
import 'bootstrap/dist/css/bootstrap.min.css'; // Import css file

import Vue from 'vue'
import './plugins/axios'
import store from './store'
import App from './App.vue'
import router from './router'
import Notifications from 'vue-notification'
Vue.config.productionTip = false
Vue.use(Notifications)

new Vue({
  store,
  router,

  render: h => h(App)
}).$mount('#app')