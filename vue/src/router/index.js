import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'

import User from '@/components/users/User'

Vue.use(Router)

export default new Router({
    mode: 'history',
    routes: [
        {
            path: '/',
            name: 'user',
            component: User
        },
    ]
})
