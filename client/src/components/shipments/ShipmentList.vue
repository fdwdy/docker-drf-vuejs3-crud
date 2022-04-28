<template>
  <div class="list row">
    <div class="col-md-6">
      <h4>Shipments List</h4>
      <ul class="list-group">
        <li
          v-for="(shipment, index) in shipments"
          :key="shipment.id"
          class="list-group-item"
          :class="{ active: index == currentIndex }"
          @click="setActiveShipment(shipment, index)"
        >
          {{ shipment.destination }} - {{ shipment.description }}
        </li>
      </ul>
    </div>
    <div class="col-md-6">
      <div class="shipment-details" v-if="currentShipment">
        <h4>Shipment</h4>
        <div>
          <label><strong>Recipient:</strong></label>
          {{ currentShipment.recipient }}
        </div>
        <div>
          <label><strong>Date:</strong></label>
          {{ currentShipment.ship_date }}
        </div>
        <div>
          <label><strong>Destination:</strong></label>
          {{ currentShipment.destination }}
        </div>
        <div>
          <label><strong>Description:</strong></label>
          {{ currentShipment.description }}
        </div>
        <div>
          <label><strong>Date:</strong></label> {{ currentShipment.ship_date }}
        </div>
        <a
          class=""
          :href="'/shipments/' + currentShipment.id"
        > Edit </a>
      </div>
      <div v-else>
        <br>
        <p>Click on shipment</p>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "../../services/api-agent";

export default {
  name: "ShipmentsList",
  data() {
    return {
      shipments: [],
      currentShipment: null,
      currentIndex: -1,
      title: "",
    };
  },
  mounted() {
    this.retrieveShipments();
  },
  methods: {
    retrieveShipments() {
      axios.get("/shipments").then((response) => {
        this.shipments = response.data;
      });
    },
    refreshList() {
      this.retrieveShipments();
      this.currentShipment = null;
      this.currentIndex = -1;
    },
    setActiveShipment(shipment, index) {
      this.currentShipment = shipment;
      this.currentIndex = index;
    },
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