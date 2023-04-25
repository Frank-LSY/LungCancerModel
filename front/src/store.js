import { createStore } from 'vuex';

export default createStore({
    state: {
        name: "",
        phone: "",
        answers: {},
        height: "",
        weight: ""
    },
    getters: {
        getName: (state) => {
            return state.name
        },
        getPhone: (state) => {
            return state.phone
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
    },
    mutations: {
        changeName: (state, value) => {
            return state.name = value
        },
        changePhone: (state, value) => {
            return state.phone = value
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
        }
    },
    actions: {

    }
})