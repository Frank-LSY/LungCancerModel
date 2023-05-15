/* eslint-disable */
import { get } from '../assets/js/request.js'



//默认导出的是一个对象
export default {
    // 查询有用户是否存在
    checkUser: query => get('/polls/user/checkUser', query),
    // 创建用户
    createUser: query => get('/polls/user/createUser', query)
}
