import Vue from 'vue'
import VueRouter from 'vue-router'
import SharkComponent from '../components/Shark.vue'
import GamesComponent from '../components/Games.vue'
Vue.use(VueRouter)

const routes = [
 
  {
    path: '/shark',
    name : 'Shark',
    component: SharkComponent
  },
  {
    path: '/games',
    name : 'Games',
    component: GamesComponent
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
