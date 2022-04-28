<template>
  <div v-if="shipment" class="edit-form">
    <h4 data-testid="shipment-heading">Add new shipment</h4>
    <form class="form-group" @submit.prevent>
      <div class="form-group">
        <label for="Recipient">Recipient</label>
        <input
          v-model="shipment.recipient"
          data-testid="recipient-input"
          class="form-control"
          name="recipient"
          type="text"
          @input="v$.recipient.$touch"
        />
        <div :class="{ 'text-danger': !valid }">
          <div v-if="v$.recipient.required.$invalid">
            Recipient field is required
          </div>
          <div v-if="v$.recipient.minLength.$invalid">
            Must have a length no less than 4.
          </div>
          <div v-if="v$.recipient.maxLength.$invalid">
            Must have a length no more than 255.
          </div>
        </div>

        <label for="destination">Destination</label>
        <input
          v-model="shipment.destination"
          data-testid="destination-input"
          class="form-control"
          type="text"
          name="destination"
          @input="v$.destination.$touch"
        />
        <div :class="{ 'text-danger': !valid }">
          <div v-if="v$.destination.required.$invalid">
            Destination field is required
          </div>
          <div v-if="v$.destination.minLength.$invalid">
            Must have a length no less than 4.
          </div>
          <div v-if="v$.destination.maxLength.$invalid">
            Must have a length no more than 255.
          </div>
        </div>

        <label for="description">Description</label>
        <textarea
          v-model="shipment.description"
          data-testid="description-input"
          class="form-control"
          name="description"
          @input="v$.description.$touch"
        />
        <div :class="{ 'text-danger': !valid }">
          <div v-if="v$.description.required.$invalid">
            Description field is required
          </div>
          <div v-if="v$.description.minLength.$invalid">
            Must have a length no less than 4.
          </div>
          <div v-if="v$.description.maxLength.$invalid">
            Must have a length no more than 500.
          </div>
        </div>

        <label for="contact_phone">Contact Phone</label>
        <input
          v-model="shipment.contact_phone"
          data-testid="contact_phone-input"
          class="form-control"
          type="text"
          name="contact-phone"
          @input="v$.contact_phone.$touch"
        />
        <div :class="{ 'text-danger': !valid }">
          <div v-if="v$.contact_phone.required.$invalid">
            Contact phone field is required
          </div>
          <div v-if="v$.contact_phone.phone.$invalid">
            Phone format: +XXX 9-15 digits
          </div>
        </div>

        <label for="ship_date">Shipping Date</label>
        <input
          v-model="shipment.ship_date"
          class="form-control"
          type="date"
          @input="v$.ship_date.$touch"
        />
        <div :class="{ 'text-danger': !valid }">
          <div v-if="v$.ship_date.required.$invalid">
            Date field is required
          </div>
          <div v-if="v$.ship_date.minValue.$invalid">
            The date has already passed
          </div>
        </div>

        <label for="shipping_company">Shipping company:</label>
        <select v-model="shipment.shipping_company" id="company-select" class="form-control">
          <option disabled value="">You can change it later</option>

          <option
            v-for="company in shippingCompanies"
            :key="company.id"
            :value="company.id"
          >
            {{ company.name }}
          </option>
        </select>
        <div v-if="shipment.cargoes">
          <div v-for="(cargo, index) in shipment.cargoes" :key="cargo.id">
            <span>Cargo #{{ index + 1 }}</span>
            <label for="cargo_name">Name:</label>
            <input
              name="cargo-name"
              v-model="cargo.name"
              class="form-control"
              type="text"
            />
            <div
              v-for="error in v$.cargoes.$each.$response.$errors[index].name"
              :key="error.$uid"
              :class="{ 'text-danger': !valid }"
            >
              {{ error.$message }}
            </div>
            <label for="weight-kg">Weight (kg):</label>
            <input
              name="cargo-weight-kg"
              v-model="cargo.weight_kg"
              class="form-control"
              type="number"
              min="0"
            />
            <div
              v-for="error in v$.cargoes.$each.$response.$errors[index].weight_kg"
              :key="error.$uid"
              :class="{ 'text-danger': !valid }"
            >
              {{ error.$message }}
            </div>
            <label for="volume-m3">Volume (m<sup>3</sup>):</label>
            <input
              name="cargo-volume-m3"
              v-model="cargo.volume_m3"
              class="form-control"
              type="number"
              min="0"
            />
            <div
              v-for="error in v$.cargoes.$each.$response.$errors[index].volume_m3"
              :key="error.$uid"
              :class="{ 'text-danger': !valid }"
            >
              {{ error.$message }}
            </div>
            <button class="" @click="removeCargo(cargo)">Remove cargo</button>
          </div>
        </div>
        <button name="add-cargo" class="" @click="addCargo">Add cargo</button>
      </div>
    </form>
    <div v-if="!valid">
      <div class="error-message" v-for="error of v$.$errors" :key="error.$uid">
        {{ error.$message }}
      </div>
    </div>
    <div class="btn-toolbar" role="toolbar">
      <div v-if="edit">
        <button name="remove-shipment" class="" @click="remove">Delete</button>
        <button type="submit" class="" @click="update">Update</button>
      </div>
      <div v-if="!edit">
        <button type="submit" @click="submit">Save</button>
      </div>
    </div>
  </div>
</template>
<script>
import uniqueId from "lodash.uniqueid";
import rules from "../../validation/shipment-rules";
import { useVuelidate } from "@vuelidate/core";
import { useToast } from "vue-toastification";
import router from "../../router/index";
import axios from "../../services/api-agent";

export default {
  name: "ShipmentItem",
  components: {},
  props: ["item", "companies", "editMode"],
  data() {
    return {
      valid: false,
      toast: useToast(),
      edit: this.editMode,
      shipment: this.item,
      shippingCompanies: this.companies,
      v$: useVuelidate(rules, this.item),
    };
  },
  watch: {
    editMode: function (val) {
      this.edit = val;
    },
  },
  methods: {
    idGen() {
      return uniqueId();
    },
    async submit() {
      const result = await this.v$.$validate();
      if (!result) {
        this.valid = false;
        this.toast.warning("Please provide valid data");
        return;
      }
      axios.post(`/shipments/`, this.shipment).then((response) => {
        this.toast.success("Shipment successfully created!");
        router.push(`/shipments/${response.data.id}`);
      });
    },
    async update() {
      const result = await this.v$.$validate();
      if (!result) {
        this.valid = false;
        this.toast.warning("Please provide valid data");
        return;
      }
      axios.put(`/shipments/${this.shipment.id}/`, this.shipment).then(() => {
        this.toast.success("Shipment successfully updated!");
        router.push(`/shipments/${this.shipment.id}`);
      });
    },
    async remove() {
      axios.delete(`/shipments/${this.shipment.id}`).then(() => {
        this.toast.success("Shipment successfully removed!");
        this.$router.push({ name: "shipments" });
      });
    },
    addCargo() {
      this.shipment.cargoes.push({
        key: this.idGen(),
        name: "",
        weight_kg: 0,
        volume_m3: 0,
      });
    },
    removeCargo(cargo) {
      this.shipment.cargoes.splice(this.shipment.cargoes.indexOf(cargo), 1);
    },
  },
};
</script>
<style>
.edit-form {
  max-width: 300px;
  margin: auto;
}
</style>
