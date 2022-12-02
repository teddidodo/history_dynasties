import { defineStore } from 'pinia';
export const usePage = defineStore({
    id: 'page',
    state: () => ({
        page: '',
        dynasty_headline: '',
        dynasty: ''
    }),
    getters: {},
    actions: {}
})
