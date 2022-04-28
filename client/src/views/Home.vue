<template>
  <div>
    <h3 class="heading">Home view goes here</h3>
    <ShipmentList />
  </div>
</template>
<script>
import ShipmentList from "../components/shipments/ShipmentList.vue";
export default {
  name: "HomePage",
  components: {
    ShipmentList,
  },
};
</script>
<style>
.list {
  text-align: left;
  max-width: 750px;
  margin: auto;
}
</style>