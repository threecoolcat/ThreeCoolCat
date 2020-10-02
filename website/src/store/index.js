import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)
const store = new Vuex.Store({
  state: {
    activeSchoolId: window.localStorage.getItem('active-school') || 1, //默认学校Id = 1
    activeSchoolName: window.localStorage.getItem('active-school-name')
  },
  getters: {
    activeSchoolId: (state) => {
      return state.activeSchoolId
    },
    activeSchoolName: (state) => {
      return state.activeSchoolName
    }
  },
  mutations: {
    CHANGE_SCHOOL(state, schoolId) {
      state.activeSchoolId = schoolId
      window.localStorage.setItem('active-school', schoolId)
    }
  },
  actions: {
    changeSchool({commit}, schoolId) {
      commit('CHANGE_SCHOOL', schoolId)
    }
  },
  modules: {

  }
})

export default store
