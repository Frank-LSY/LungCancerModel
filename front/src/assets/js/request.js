// get/post请求封装

import axios from 'axios'
import qs from 'qs'
import store from '@/store'
import router from '@/router'
import https from 'https-browserify'
// import common from './common'
import { infoMessage,errorMessage } from './common'
//响应拦截器
axios.interceptors.response.use(
    function (response) {
        // console.log(response)
        const res = response.data
        if (res && res.code !== 200) {
            res
        }
        return response

    },
    function (error) {
        return Promise.reject(error)
    }
)

//请求拦截器 
axios.interceptors.request.use(
    function (config) {
        //...
        return config
    },
    function (error) {
        return Promise.reject(error)
    }
)

// const httpsAgent = new https.Agent({
//     rejectUnauthorized: false,
// })

// axios.defaults.httpsAgent = httpsAgent

/*
 * 封装请求方法
 */
const request = function (query) {
    return axios
        .request(query)
        .then((res) => {
            // console.log(res)
            if (res.status === 500) { //判断是否和后端连上了
                errorMessage('与后端数据连接断开!')
            } else if (res.status === 200) { //如果和后端连上了
                
                if (res.data.code === 200) { //如果后端说请求正确，直接返回
                    return Promise.resolve(res.data)
                } else if (res.data.code === 401 ||
                    res.data.code === 502) { //如果后端觉得权限不足
                    return Promise.reject(res.data)
                } else if (res.data.code === 1003 ||
                    res.data.code === 1002) { //如果后端说登录被踢了或掉线了
                    // console.log('未登录！')
                    infoMessage('未登录！')
                    // localStorage.removeItem("flag");
                    // localStorage.removeItem("userId");
                    // localStorage.removeItem("userName");
                    // localStorage.removeItem("roleId");
                    // localStorage.removeItem("authList");
                    // store.dispatch("setLoginStatus", false);
                    // router.push({
                    //     path: "/dcsp-front",
                    // });
                    return Promise.reject(res.data)
                } else { //其他全给拒掉
                    // console.log(res)
                    return Promise.reject(res.data)
                }
            }

        })
        //对错误进行处理
        .catch((e) => {
            return Promise.reject(e.message)
        })
}

//post请求  ----> json格式的post请求 
const post = function (url, params) {
    const query = {
        url: url,
        method: 'post',
        withCredentials: true, //跨域允许携带cookie
        timeout: 30000,
        data: params,
        headers: { 'Content-Type': 'application/json', 'request-ajax': true },
    }
    return request(query)
}

//Get请求
const get = function (url, params) {
    const query = {
        url: url,
        method: 'get',
        withCredentials: true,
        timeout: 30000,
        params: params,
        headers: { 'request-ajax': true },
    }
    return request(query)
}

//post 请求（用于后端是post，但不是通过对象接收参数的情况）
const form = function (url, params) {
    const query = {
        url: url,
        method: 'post',
        withCredentials: true,
        timeout: 30000,
        data: params,
        transformRequest: [
            function (data) {
                return qs.stringify(data);
            }
        ],
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'request-ajax': true,
        },
    }
    return request(query)
}

// delete 请求
const delitt = function (url, params) {
    const query = {
        url: url,
        method: 'delete',
        withCredentials: true,
        timeout: 30000,
        params: params,
        headers: { 'request-ajax': true },
    }
    return request(query)
}

export { get, post, form, delitt }