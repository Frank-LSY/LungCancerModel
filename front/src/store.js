import { createStore } from 'vuex';

export default createStore({
    state: {
        num: -1, //第几题
        name: "test", //姓名
        phone: 1, //电话
        userid: "", //用户id
        pollid: "", //问卷id
        questions: [], //题目
        answers: {}, //答案
        height: "", //身高
        weight: "", //体重
        bmi: "", //bmi
        prob: "", //概率
        smoke: "", //吸烟
        detail: {
            showDialog:false,
            details: []
        } //详细信息
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
        getUserid: (state) => {
            return state.userid
        },
        getPollid: (state) => {
            return state.pollid
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
        getBmi: (state) => {
            return state.bmi
        },
        getProb: (state) => {
            return state.prob
        },
        getSmoke: (state) => {
            return state.smoke
        },
        getDetail: (state) => {
            return state.detail
        }
    },
    mutations: {
        changeNum: (state, value) => {
            return state.num = value
        },
        changeName: (state, value) => {
            return state.name = value
        },
        changePhone: (state, value) => {
            return state.phone = value
        },
        changeUserid: (state, value) => {
            return state.userid = value
        },
        changePollid: (state, value) => {
            return state.pollid = value
        },
        changeQuestions: (state, value) => {
            return state.questions = value
        },
        changeAnswer: (state, value) => {
            return state.answers = value
        },
        changeAnswers: (state, value) => {
            return state.answers[value.name] = value.val
        },
        deleteAnswers: (state, value) => {
            return delete state.answers[value]
        },
        changeHeight: (state, value) => {
            return state.height = value
        },
        changeWeight: (state, value) => {
            return state.weight = value
        },
        changeBmi: (state, value) => {
            return state.bmi = value
        },
        changeProb: (state, value) => {
            return state.prob = value
        },
        changeSmoke: (state, value) => {
            return state.smoke = value
        },
        changeDetail: (state, value) => {
            return state.detail = value
        }
    },
    actions: {

    }
})