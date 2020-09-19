// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
// import Vuex from 'vuex'
import 'babel-polyfill';
import Es6Promise from 'es6-promise';
require('es6-promise').polyfill();
Es6Promise.polyfill();
import store from './store'
import App from './App'

import './login.js'
import axios from 'axios'
import i18n from './lang' // internationalization

import eChart from './components/echart/chart.vue'
Vue.component('e-chart', eChart);
import liquidfill from 'echarts-liquidfill'
Vue.use(liquidfill)

import 'swiper/dist/css/swiper.css';

// 引入loadscript
import LoadScript from 'vue-load-script'
Vue.use(LoadScript)

import Element from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import './assets/style/css/element_ui.less'
Vue.use(Element, {
  size: 'small', // set element-ui default size
  i18n: (key, value) => i18n.t(key, value)
})

var VueCookie = require('vue-cookie')
Vue.use(VueCookie)

Vue.prototype.$http = axios
Vue.prototype.$dayjs = require('dayjs')
// Vue.use(Vuex)

Vue.config.productionTip = false
import router from './router'
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router, //vue-router
  store, // vuex
  render: h => h(App)
})


