import { post, form } from "@/assets/js/request";

//默认导出的是一个对象
export default {
    // 计算癌症概率
    calcProbability: query => post('/polls/result/calcProbability', query)

}