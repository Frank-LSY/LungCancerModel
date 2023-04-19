import { createStore } from 'vuex';

export default createStore({
    state: {
        name: "",
        phone: ""
    },
    getters: {
        getName: (state) => {
            return state.name
        },
        getPhone: (state) => {
            return state.phone
        }
    },
    mutations: {
        changeName: (state, value) => {
            return state.name = value
        },
        changePhone: (state, value) => {
            return state.phone = value
        }
    },
    actions: {

    }
})