<!-- #24292e -->
<template>
  <div class="" :style="{ backgroundColor: 'brown' }">
      <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: "App",
  components: {},
  methods: {
    delay(ms) {
      const startPoint = new Date().getTime();
      while (new Date().getTime() - startPoint <= ms) {
        /* wait */
      }
    }},

  async mounted() {
  },
  setup() {
    return {
    };
  },
};
</script>

<style>
body {
  background-color: "#F8F8FB";
}
</style>
