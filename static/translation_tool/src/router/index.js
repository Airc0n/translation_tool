import Vue from 'vue'
import VueRouter from 'vue-router'
import HtmlGenerator from '../views/HtmlGenerator.vue'


Vue.use(VueRouter)

const routes = [{
    path: '/',
    redirect: {
      name: 'HtmlGenerator'
    }
  },
  {
    path: '/html-generator',
    name: 'HtmlGenerator',
    component: HtmlGenerator
  },
  {
    path: '/resources-manage',
    name: 'ResourcesManage',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import( /* webpackChunkName: "about" */ '../views/ResourcesManage.vue')
  }
]

const router = new VueRouter({
  routes
})

export default router