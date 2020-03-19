import Vue from 'vue'
import Router from 'vue-router'
import Overview from '@/components/Overview'
import Add from '@/components/Add'
import Edit from '@/components/Edit'
import Login from '@/components/Login'

Vue.use(Router)

export default new Router({
  routes: [
        {
      path: '/',
      name: 'Login',
      component: Login
    },
    {
      path: '/Overview',
      name: 'Overview',
      component: Overview
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
  ]
})
