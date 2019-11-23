import Vue from 'vue'
import Router from 'vue-router'

import Index from '@/components/Index'
import Login from '@/views/Login'
import Logout from '@/views/Logout'
import ListChampionships from '@/components/Books/List'
import EditBook from '@/components/Books/Edit'
import Experiments from '@/components/Experiments'
import Inicial from '@/components/Inicial'
import Origem from '@/components/Origem'
import Copas from '@/components/Copas'
import Brasileirao2018 from '@/components/Brasileirao2018'
import Brasileirao2008 from '@/components/Brasileirao2008'
import Regulamento from '@/components/Regulamento'
import Teste from '@/components/Teste'
Vue.use(Router)

export default new Router({
    mode: 'history',
    hash: false,
    routes: [{
            path: '/',
            name: 'Index',
            component: Index
        },
        {
            path: '/login',
            name: 'Login',
            component: Login
        },
        {
            path: '/logout',
            name: 'Logout',
            component: Logout
        },
        {
            path: '/championships',
            name: 'ListChampionships',
            component: ListChampionships
        },
        {
            path: '/books/edit/:id',
            name: 'EditBook',
            component: EditBook
        },
        {
            path: '/experiments',
            name: 'Experiments',
            component: Experiments
        },
        {
            path: '/inicial',
            name: 'Inicial',
            component: Inicial
        },
        {
            path: '/origem',
            name: 'Origem',
            component: Origem
        },
        {
            path: '/copa',
            name: 'Copas',
            component: Copas
        },
        {
            path: '/brasileirao2018',
            name: 'Brasileirao2018',
            component: Brasileirao2018
        },
        {
            path: '/brasileirao2008',
            name: 'Brasileirao2008',
            component: Brasileirao2008
        },
        {
            path: '/regulamento',
            name: 'Regulamento',
            component: Regulamento
        },
        {
            path: '/teste',
            name: 'Teste',
            component: Teste
        }
    ]
})