<template>
  <div class="text-white q-mx-md">
    <q-drawer v-model="isLeftOpen" :width="300" :breakpoint="700" bordered class="bg-grey-3 text-grey">
      <q-scroll-area class="fit full-height">
        <q-list padding class="" :style="{ maxWidth: '350px' }">
          <q-item-label header>Table of Contents</q-item-label>

          <q-item v-for="(content_head, idx) in contents_heads" :key="content_head" tag="label" v-ripple>
            <a :href="'#' + idx" :style="{ textDecoration: 'none' }" class="text-black full-width">
              <q-item-label>{{ content_head }}</q-item-label>
            </a>
          </q-item>

        </q-list>
      </q-scroll-area>
    </q-drawer>
    <div class="q-mx-md" :style="{ opacity: opacity_value / 10 }">
      <div :class="[$q.screen.lt.md ? 'text-left' : 'text-center', 'text-h2 text-bold']">
        Dynasty of {{ dynasty.name }}
        <br>
        (House of {{ dynasty.house }})
      </div>
      <q-timeline :layout="layout" color="secondary" class="">
        <div v-for="(eventPeriod, idx) in events" :key="eventPeriod">
          <q-timeline-entry :id="idx" heading>{{ eventPeriod[0] }}

          </q-timeline-entry>
          <q-timeline-entry v-for="(event, idx) in eventPeriod[1]" :key="event.year" :title="event.description"
            :subtitle="event.year" :side="idx % 2 === 0 ? 'left' : 'right'" class="text-caption" />
        </div>
      </q-timeline>

      <q-page-sticky position="bottom-right" :offset="[18, 18]">
        <q-fab color="amber" text-color="black" icon="" class="float-right" @click="isLeftOpen = !isLeftOpen">
          <template v-slot:label="{ opened }">
            <div>
              {{!opened ? 'Contents' : 'Close'}}
            </div>
          </template>
        </q-fab>
      </q-page-sticky>
    </div>
  </div>
</template>

<style>

</style>

<script>
import { inject, ref, computed } from 'vue'
import { fabGithub } from '@quasar/extras/fontawesome-v6'
import { useQuasar } from 'quasar'
import HTTP from "../api/http_common";
import { usePage } from "../store/usePage";
const stringOptions = [
  'quasarframework/quasar',
  'quasarframework/quasar-awesome'
]
export default {
  name: "Timeline",
  components: {},
  methods: {
    async getDynasty() {
      try {
        const dynastyPromise = HTTP.get("/dynasties/" + this.currentPage.dynasty)
        const dynastyResult = await dynastyPromise;
        this.currentPage.dynasty_headline = dynastyResult.data
        this.dynasty = dynastyResult.data
      } catch (error) {
        console.log(error);
      }
    },
    async getTimeline() {
      try {
        const eventsDynastyPromise = HTTP.get("/events/" + this.currentPage.dynasty)
        const eventsResult = await eventsDynastyPromise;

        const data = eventsResult.data
        this.contents_heads = Object.keys(data).reverse()
        this.events = Object.entries(data).reverse()
        this.events = this.events.map((event) => {
          return [event[0], event[1].reverse()]
        })
      } catch (error) {
        console.log(error);
      }
    },
    delay(ms) {
      const startPoint = new Date().getTime();
      while (new Date().getTime() - startPoint <= ms) {
        /* wait */
      }
    }
  },
  mounted() {
    try {
      this.getDynasty()
      this.getTimeline()
    } catch (error) {
      console.log(error);
    }
  },

  setup() {
    const text = ref('')
    const inner_search = ref('')
    const isLeftOpen = ref(false) // boolean to check the left drawer
    const opacity_value = ref(9)
    const $q = useQuasar()
    const mode = ref(true)
    const options = ref(null)
    const filteredOptions = ref([])
    const search = ref(null) // $refs.search
    const currentPage = usePage();

    const dynasty = ref({})
    const events = ref([])
    const contents_heads = ref([])


    const myEl = ref(0);
    const constant = ref(400)
    const smoothScroll = inject("smoothScroll");
    const scrollToMyEl = () => {
      smoothScroll({
        scrollTo: myEl.value - constant.value,
        hash: "#sampleHash",
      });
    };
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
          filteredOptions.value = options.value.map(op => ({ label: op }))
        })
        return
      }

      update(() => {
        filteredOptions.value = [

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
      mode, layout: computed(() => {
        return $q.screen.lt.sm ? 'dense' : ($q.screen.lt.md ? 'comfortable' : 'loose')
      }),
      check1: ref(true),
      check2: ref(false),
      check3: ref(false),

      notif1: ref(true),
      notif2: ref(true),
      notif3: ref(false),
      isLeftOpen,
      inner_search,
      opacity_value,
      currentPage,
      dynasty,
      events,

      contents_heads,
      smoothScroll,
      scrollToMyEl
    }
  }
}
</script>
