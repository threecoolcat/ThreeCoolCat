import Vue from 'vue'
import Vuex from 'vuex'
import { constantRoutes } from '@/router'
Vue.use(Vuex)
const store = new Vuex.Store({
  state: {
    permissioned_routes: constantRoutes
  },
  getters: {
    permissioned_routes: (state) => {
      return state.permissioned_routes
    },

  },
  mutations: {
    
  },
  actions: {
  },
  modules: {
    //
  }
})

export default store
