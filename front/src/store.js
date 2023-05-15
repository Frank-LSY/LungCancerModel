import { createStore } from 'vuex';

export default createStore({
    state: {
        num: -1, //第几题
        name: "拖拉机没有司机", //姓名
        phone: "", //电话
        questions: [], //题目
        answers: {}, //答案
        height: "", //身高
        weight: "", //体重
        bmi: "" //bmi
    },
    getters: {
        getNum: (state) => {
            return state.num
        },
        getName: (state) => {
            return state.name
        },
        getPhone: (state) => {
            return state.phone
        },
        getQuestions: (state) => {
            return state.questions
        },
        getAnswers: (state) => {
            return state.answers
        },
        getHeight: (state) => {
            return state.height
        },
        getWeight: (state) => {
            return state.weight
        },
        getBmi: (state) =>{
            return state.bmi
        }
    },
    mutations: {
        changeNum: (state,value) => {
            return state.num = value
        },
        changeName: (state, value) => {
            return state.name = value
        },
        changePhone: (state, value) => {
            return state.phone = value
        },
        changeQuestions: (state, value) => {
            return state.questions = value
        },
        changeAnswers: (state, value) => {
            return state.answers[value.name] = value.val
        },
        deleteAnswers: (state,value) => {
            return delete state.answers[value]
        },
        changeHeight: (state,value) => {
            return state.height = value
        },
        changeWeight: (state,value) => {
            return state.weight = value
        },
        changeBmi: (state,value)=> {
            return state.bmi = value
        }
    },
    actions: {

    }
})