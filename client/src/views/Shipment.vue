<template>
  <div>
    <h3 class="heading">ShipmentView</h3>
    <ShipmentForm
      :item="shipment"
      :companies="shippingCompanies"
      :edit-mode="edit"
    />
  </div>
</template>
<script>
import dayjs from "dayjs";
import ShipmentForm from "../components/shipments/ShipmentForm.vue";
import axios from "../services/api-agent";

export default {
  name: "ShipmentItem",
  components: { ShipmentForm },
  beforeRouteEnter(to, from, next) {
    if (!to.params.id) {
      let shipment = {
        id: null,
        shipping_company: "",
        recipient: "",
        destination: "",
        description: "",
        contact_phone: "",
        ship_date: dayjs().format("YYYY-MM-DD"),
        cargoes: [],
      };
      axios.get("/companies").then(function (response) {
        next((vm) => {
          vm.edit = false;
          Object.assign(vm.shipment, shipment);
          Object.assign(vm.shippingCompanies, response.data);
        });
      });
    } else {
      axios
        .get(`/shipments/${to.params.id}`)
        .then(function (response) {
          let shipment = response.data;
          axios.get("/companies").then(function (response) {
            next((vm) => {
              vm.edit = true;
              Object.assign(vm.shipment, shipment);
              Object.assign(vm.shippingCompanies, response.data);
            });
          });
        })
        .catch(function () {
          next();
        });
    }
  },
  data() {
    return {
      edit: false,
      shipment: {},
      shippingCompanies: [],
    };
  },
};
</script>
<style>
.edit-form {
  max-width: 300px;
  margin: auto;
}
</style>
