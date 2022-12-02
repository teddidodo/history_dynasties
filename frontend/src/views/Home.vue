<!-- https://www.educative.io/answers/how-to-use-postgresql-database-in-fastapi -->
<template>
  <div class="text-white absolute-center">
    <div class="q-mb-md" :style="{ marginLeft: '12%', marginRight: '12%' }">

      <div :class="['text-bold q-pb-md', $q.screen.lt.md ? 'text-center text-subtitle1' : 'text-h3']">
        Time travel to dynasties around the world!
      </div>

      <q-select ref="search" standout use-input hide-selected class="bg-yellow" :stack-label="false"
        placeholder="Search a dynasty..." v-model="text" :options="filteredOptions" @filter="filter"
        :style="{ width: '100%' }">

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
    </div>
    {{ text }}
  </div>
</template>

<style>

</style>

<script>
import { ref, computed } from 'vue'
import { fabGithub } from '@quasar/extras/fontawesome-v6'
const stringOptions = [
  "Japan", "Sui", "Tang", "Song", "Ming", "Qing", "Joseon", "Goryeo", "Han"
]
export default {
  name: "Home",

  setup() {
    const text = ref('')
    const mode = ref(true)
    const options = ref(null)
    const filteredOptions = ref([])
    const search = ref(null) // $refs.search

    const myListRef = ref(null)
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
            label: val
          },
          ...options.value
            .filter(op => op.toLowerCase().includes(val.toLowerCase()))
            .map(op => ({ label: op }))
        ]
      })
    }

    return {
      myListRef,
      listEl: computed(() => myListRef.value ? myListRef.value.$el : null),
      fabGithub,
      text,
      options,
      filteredOptions,
      search,
      filter,
      mode
    }
  }
}
</script>



<style lang="sass" scoped>
.example-item
  height: 290px
  width: 250px
</style>