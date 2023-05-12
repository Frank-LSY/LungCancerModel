/* eslint-disable */
import { get, post, form } from '../assets/js/request.js'



//默认导出的是一个对象
export default {
    getAllQuestions: query => get('/polls/question/getAllQuestions', query),
}
