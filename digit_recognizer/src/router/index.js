import { createRouter, createWebHistory } from 'vue-router'
import IndexView from '../views/IndexView.vue'
import DigitView from '../views/DigitView.vue'

const routes = [

  {path:'/',name:'index',component:IndexView},
  {path:'/PredictDigit/:digit',name:'PredictDigit',component:DigitView},

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
