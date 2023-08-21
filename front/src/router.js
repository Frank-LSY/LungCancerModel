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
                path: '/history',
                component: () => import('@components/History.vue'),
                name: '历史',
                meta: {
                    isLogin: false,
                    title: '用户记录',
                    index: 2
                },
            },
            {
                path: '/questions',
                component: () => import('@components/QuestionOnePage.vue'),
                name: '问卷',
                meta: {
                    isLogin: false,
                    title: '问卷内容',
                    index: 3
                },
            },
            {
                path: '/result',
                component: () => import('@components/Result.vue'),
                name: '结果',
                meta: {
                    isLogin: false,
                    title: '问卷结果',
                    index: 4
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

