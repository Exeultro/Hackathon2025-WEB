import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/Home.vue'

const routes = [
  
  {
    path: '/',
    name: 'Home',
    component: HomePage
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('../views/About.vue')
  },
  {
    path: '/careers', 
    name: 'Careers',
    component: () => import('../views/Careers.vue')
  },
  {
    path: '/team',
    name: 'Team', 
    component: () => import('../views/Team.vue')
  },
  {
    path: '/simulator',
    name: 'Simulator',
    component: () => import('../views/Simulator.vue')
  },
  {
    path: '/news',
    name: 'News',
    component: () => import('../views/News.vue')
  },
  {
    path: '/news/:id',
    name: 'NewsArticle',
    component: () => import('../views/NewsArticle.vue'),
    props: true
  },
  {
    path: '/career-paths',
    name: 'CareerPaths',
    component: () => import('../views/CareerPaths.vue')
  },
  {
    path: '/career-paths/:id',
    name: 'CareerPathItem',
    component: () => import('../views/CareerPathItem.vue'),
    props: true
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router