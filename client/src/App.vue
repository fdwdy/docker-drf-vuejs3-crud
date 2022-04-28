<template>
  <div id="app">
    <NavBar />
    <div class="container mt-3">
      <router-view />
    </div>
  </div>
</template>
<script>
import NavBar from '../src/components/layout/NavBar.vue'
export default {
  name: "App",
  components: { NavBar }
};
</script>