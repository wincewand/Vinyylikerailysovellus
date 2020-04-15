import Vue from 'vue'
import Router from 'vue-router'
import Overview from '@/components/Overview'
import Add from '@/components/Add'
import Edit from '@/components/Edit'
import Login from '@/components/Login'

Vue.use(Router)

const router = new Router({
  routes: [
        {
      path: '/',
      name: 'Login',
      component: Login
    },
    {
      path: '/Overview',
      name: 'Overview',
      component: Overview,
      props: (route) => ({ status: route.query.status }),
    },
    {
      path: '/Add',
      name: 'Add',
      component: Add
    },
    {
      path: '/Edit',
      name: 'Edit',
      component: Edit,
      props: (route) => ({ id: route.query.id })
    },
  ],
  
})
router.beforeEach((to, from, next)  => {
  if (to.name !== 'Login' && !$cookies.get("user")) next({ name: 'Login' })
  else next()
})

export default router