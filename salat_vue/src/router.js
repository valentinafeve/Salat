import Vue from 'vue'
import VueRouter from 'vue-router'
import Information from './views/Information.vue'
import Loader from './views/Loader.vue'
import Login from './views/Login.vue'

Vue.use(VueRouter)

const routes = [
  { path: '/', component : Login},
  { path: '/information', component: Information },
  { path: '/loader', component: Loader },
]

const  router  =  new  VueRouter({
  routes
})

export default router;
