import Vue from 'vue'
import Router from 'vue-router'

import Index from '@/components/Index'
import Login from '@/views/Login'
import Logout from '@/views/Logout'
import EditionC from '@/components/Championships/EditionC'
import ListChampionships from '@/components/Championships/List'
import EditChampionship from '@/components/Championships/Edit'
import Origem from '@/components/Origem'
import Copas from '@/components/Copas'
import Brasileirao2019 from '@/components/Brasileirao2019'
import Brasileirao2018 from '@/components/Brasileirao2018'
import Brasileirao2008 from '@/components/Brasileirao2008'
import Regulamento from '@/components/Regulamento'
import Teste from '@/components/Teste'
import Teams from '@/components/Teams/List'
import EditTeam from '@/components/Teams/Edit'

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
            path: '/editionc',
            name: 'EditionC',
            component: EditionC
        },
        {
            path: '/championships',
            name: 'ListChampionships',
            component: ListChampionships
        },
        {
            path: '/championships/edit/:id',
            name: 'EditChampionship',
            component: EditChampionship
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
            path: '/brasileirao2019',
            name: 'Brasileirao2019',
            component: Brasileirao2019
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
            path: '/teams',
            name: 'Teams',
            component: Teams
        },
        {
            path: '/teams/edit/:id',
            name: 'EditTeam',
            component: EditTeam
        },
        {
            path: '/teste',
            name: 'Teste',
            component: Teste
        }
    ]
})