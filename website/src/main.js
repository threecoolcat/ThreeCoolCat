// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import store from './store'
import App from './App'
import axios from 'axios'

import Element from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import '@/assets/style/css/element_ui.less'
Vue.use(Element, {
  size: 'small', // set element-ui default size
})
Vue.prototype.$http = axios

Vue.config.productionTip = false
import router from './router'
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router, //vue-router
  store, // vuex
  render: h => h(App)
})


