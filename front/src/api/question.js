/* eslint-disable */
import { get, post, form } from '../assets/js/request.js'



//默认导出的是一个对象
export default {
    // 获取所有问题
    getAllQuestions: query => get('/polls/question/getAllQuestions', query),
    // 获取问题id
    getQuestionHandle: query => get('/polls/question/getQuestionHandle', query),
    // 获取某一个问题
    getOneQuestion: query => get('/polls/question/getOneQuestion', query),
}
