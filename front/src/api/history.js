import { get, post, form } from "@/assets/js/request";

//默认导出的是一个对象
export default {
    // 获取用户历史
    listHistory: query => get('/polls/history/listHistory', query),
    // 插入用户历史
    addHistory: query => post('/polls/history/addHistory/', query),
}