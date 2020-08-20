import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)
export default new Vuex.Store({
  // strict: true,
  state: {
    // save data
    templates: [],
    resources: [],
    selected_template_id: null,
  },
  getters: {
    getTemplates: (state) => {
      return state.templates
    },
    getTemplateById: (state) => (id) => {
      return state.templates.find(template => template.id === id)
    },
    getResources: (state) => {
      return state.resources
    },

  },
  mutations: {
    // update state's data
    // synchronize operation
    UpdateResources(state, resources) {
      state.resources = resources
    },

    updateTemplates(state, templates) {
      state.templates = templates
    },
    selectTemplate(state, tid) {
      state.selected_template_id = tid
    }

  },
  actions: {
    //call api and commit to mutation
    // asynchronize operation
    // cannot update state directly
    getHtmlTemplates(context) {
      axios.get('http://localhost:8000/api/v1/translation/templates')
        .then((resp) => {
          let templates = resp.data.results
          context.commit("updateTemplates", templates)
        }).catch((error) => {
          console.log(error);
        })
    },
    getResources(context, tid) {
      if (!tid || tid === 'null') {
        context.commit('UpdateResources', null)
        return
      }

      axios.get('http://localhost:8000/api/v1/translation/resources', {
        params: {
          tid: tid
        },
      }).then(function (resp) {
        context.commit('UpdateResources', resp.data.results)
      }).catch(function (error) {
        console.log(error);
      })

    },
  },
  modules: {}
})