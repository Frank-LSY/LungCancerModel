import {
    createRouter,
    createWebHashHistory,
} from 'vue-router'

const routes = [
    // 路由的默认路径
    {
        path: '/',
        redirect: "/home",
        meta: {
            title: '肺癌风险预测问卷'
        }
    },
    {
        path: '/home',
        component: () => import('@/Structure.vue'),
        redirect: "/check",
        name: '主页',
        meta: {
            isLogin: false,
            title: '肺癌风险预测问卷',
            index: 1
        },
        children: [
            {
                path: '/check',
                component: () => import('@components/Check.vue'),
                name: '检查',
                meta: {
                    isLogin: false,
                    title: '肺癌风险预测问卷',
                    index: 1
                },
            },
            {
                path: '/questions',
                component: () => import('@components/Questions.vue'),
                name: '问卷',
                meta: {
                    isLogin: false,
                    title: '问卷内容',
                    index: 2
                },
            }
        ]
    },

    // {
    //     // 一切没的页面导向404
    //     path: '/:catchAll(.*)',
    //     redirect: '/404',
    // },

]

// 创建路由对象
const router = createRouter({
    history: createWebHashHistory(),
    base: '/lungCancer/',
    routes
})
export default router;

