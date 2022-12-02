<!-- darkmode: #24292e grey -->
<!-- whitemode: #0366d6 blue  -->
<!-- v-if="$q.screen.gt.xs" -->
<!-- v-if="$q.screen.gt.xs" -->
<!-- BC002D -->
<template>
  <q-layout view="hHh Lpr lFf" class="bg-grey-1">
    <q-header bordered
      :class="['sticky column', page === 'home' ? 'bg-white text-black shadow-2' : 'bg-red-10 text-white']"
      :style="{ backgroundColor: '' }" height-hint="61.59">
      <q-toolbar class="q-px-md q-gutter-sm q-py-xs col" fixed>
        <q-avatar @click="this.$router.push({path: '/'})">
        <img
          src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Coat_of_Arms_of_Joseon_Korea.svg/160px-Coat_of_Arms_of_Joseon_Korea.svg.png"
          width="50" /></q-avatar>
        <q-btn v-if="page == 'home'" class="tex-subtitle" flat @click="this.$router.push({path: '/' + dynasty_headline.name})">{{dynasty_headline != "" ? "Dynasty of the day: " + dynasty_headline.name + " " + "(House of" + " " + dynasty_headline.house + ")": "History Timeline"}}</q-btn>

        <q-btn v-if="page == 'timeline'" class="tex-subtitle" flat>{{dynasty_headline != "" ? dynasty_headline.name + " " + "(House of" + " " + dynasty_headline.house + ")": "History Timeline"}}</q-btn>

        <div class="col row">
          <q-select v-if="$q.screen.gt.sm && page !== 'home'" ref="search" dark dense standout use-input hide-selected
            class="" color="white" :stack-label="false" label="Search a dynasty..." v-model="text"
            :options="filteredOptions" @filter="filter" :style="{ width: '300px' }">

            <template v-slot:append>
              <img src="https://cdn.quasar.dev/img/layout-gallery/img-github-search-key-slash.svg">
            </template>

            <template v-slot:no-option>
              <q-item>
                <q-item-section>
                  <div class="text-center">
                    <q-spinner-pie color="grey-5" size="24px" />
                  </div>
                </q-item-section>
              </q-item>
            </template>

            <template v-slot:option="scope">
              <q-item v-bind="scope.itemProps" class="" 
              @click="() => {
                this.currentPage.dynasty = text.label
                this.$nextTick();
                this.$router.push({ path: '/' + text.label })
              }"
            >
                <q-item-section side>
                  <q-icon name="collections_bookmark" />
                </q-item-section>
                <q-item-section>
                  <q-item-label v-html="scope.opt.label" />
                </q-item-section>
              </q-item>
            </template>
          </q-select>
        </div>

        <q-btn v-if="$q.screen.lt.md && page !== 'home'" class="q-pa-sm" size="12px" flat
          @click="phone_search = !phone_search">
          <q-icon class="" name="search" />
        </q-btn>
        <q-space v-if="$q.screen.gt.xs" />

        <a v-if="!$q.screen.lt.md" href="https://github.com/teddidodo" :style="{textDecoration: 'none'}" target="_blank">
        <q-btn 
         dense flat :class="page === 'home' ? 'text-black' : 'text-white'">
          @Created by Thanh Do
        </q-btn></a>
      </q-toolbar>
      <q-toolbar v-if="$q.screen.lt.md && phone_search && page !== 'home'" class="">
        <q-select ref="search" dark dense standout use-input hide-selected class="text-black full-width" color="black"
          :stack-label="false" label="Search a dynasty..." v-model="text" :options="filteredOptions" @filter="filter">

          <template v-slot:append>
            <img src="https://cdn.quasar.dev/img/layout-gallery/img-github-search-key-slash.svg">
          </template>

          <template v-slot:no-option>
          <q-item>
            <q-item-section>
              <div class="text-center">
                <q-spinner-pie color="grey-5" size="24px" />
              </div>
            </q-item-section>
          </q-item>
        </template>

          <template v-slot:option="scope">
            <q-item v-bind="scope.itemProps" class="" @click="() => {
            this.currentPage.dynasty = text.label
            this.$nextTick();
            this.$router.push({ path: '/' + text.label })

          }">
              <q-item-section side>
              <q-icon name="collections_bookmark" />
            </q-item-section>
            <q-item-section>
              <q-item-label v-html="scope.opt.label" />
            </q-item-section>
              
            </q-item>
          </template>
        </q-select>
      </q-toolbar>
    </q-header>
    <q-page-container :class="page === 'timeline' ? 'bg-image' : 'bg-home'">
      <router-view />
      <q-footer class="transparent">2022</q-footer>
    </q-page-container>


  </q-layout>
</template>

<script>

import { ref } from 'vue'
import { fabGithub } from '@quasar/extras/fontawesome-v6'
import { storeToRefs } from "pinia";
import { usePage } from "../store/usePage";

import king from '../assets/king.png'

const stringOptions = [
  "Japan", "Sui", "Tang", "Song", "Ming", "Qing", "Joseon", "Goryeo", "Han"
]

export default {
  name: 'MyLayout',
  methods: {
  },

  setup() {
    const text = ref('')
    const mode = ref(true)

    const phone_search = ref(false)
    const options = ref(null)
    const filteredOptions = ref([])
    const search = ref(null) // $refs.search
    const currentPage = usePage();
    let { page, dynasty_headline } = storeToRefs(currentPage);

    function filter(val, update) {
      if (options.value === null) {
        // load data
        setTimeout(() => {
          options.value = stringOptions
          search.value.filter('')
        }, 2000)
        update()
        return
      }

      if (val === '') {
        update(() => {
          filteredOptions.value = [{label: "Song"}, {label: "Japan"}, {label: "Ming"}, {label: "Joseon"}]
        })
        return
      }

      update(() => {
        filteredOptions.value = [
          {
            label: val,
            type: 'In this repository'
          },
          {
            label: val,
            type: 'All GitHub'
          },
          ...options.value
            .filter(op => op.toLowerCase().includes(val.toLowerCase()))
            .map(op => ({ label: op }))
        ]
      })
    }

    return {
      fabGithub,
      text,
      options,
      filteredOptions,
      search,
      filter,
      mode,
      king,
      phone_search,
      page,
      dynasty_headline,
      currentPage
    }
  }
}
</script>

<style lang="sass">
.GL
  &__select-GL__menu-link
    .default-type
      visibility: hidden

    &:hover
      background: #0366d6
      color: white
      .q-item__section--side
        color: white
      .default-type
        visibility: visible

  &__toolbar-link
    a
      color: white
      text-decoration: none
      &:hover
        opacity: 0.7

  &__menu-link:hover
    background: #0366d6
    color: white

  &__menu-link-signed-in,
  &__menu-link-status
    &:hover
      & > div
        background: white !important

  &__menu-link-status
    color: $blue-grey-6
    &:hover
      color: $light-blue-9

  &__toolbar-select.q-field--focused
    width: 450px !important
    .q-field__append
      display: none

.bg-image
  background: linear-gradient( rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5) ), url(https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Flag_of_the_Japanese_Emperor.svg/2560px-Flag_of_the_Japanese_Emperor.svg.png)
  background-repeat: no-repeat
  background-size: 100% 100%
  background-attachment: fixed



.bg-home
  background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url(https://upload.wikimedia.org/wikipedia/commons/d/d7/Korea-Gyeongju-Bulguksa-33.jpg)  
  background-repeat: no-repeat
  background-size: 100% 100%
  background-attachment: fixed
  height: 100vh


.sticky
  position: sticky
  background-attachment: scroll
  left: 0
  top: 0

</style>

<!-- https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Imperial_Seal_of_Japan.svg/1920px-Imperial_Seal_of_Japan.svg.png -->
<!-- https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Sekigahara_Kassen_By%C5%8Dbu-zu_%28Gifu_History_Museum%29.jpg/1200px-Sekigahara_Kassen_By%C5%8Dbu-zu_%28Gifu_History_Museum%29.jpg -->
<!-- https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Flag_of_the_Japanese_Emperor.svg/2560px-Flag_of_the_Japanese_Emperor.svg.png -->