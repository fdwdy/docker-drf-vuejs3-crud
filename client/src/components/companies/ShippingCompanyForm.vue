<template>
  <div v-if="company" class="edit-form">
    <h4>Add new shipping company</h4>

    <form class="form-group" @submit.prevent>
      <div class="form-group">
        <label for="name">Name</label>
        <input
          v-model="company.name"
          data-testid="name-input"
          class="form-control"
          name="name"
          type="text"
        />
        <div :class="{ 'text-danger': !valid }">
          <div v-if="v$.name.required.$invalid">Name field is required</div>
          <div v-if="v$.name.minLength.$invalid">
            Must have a length no less than 4.
          </div>
          <div v-if="v$.name.maxLength.$invalid">
            Must have a length no more than 255.
          </div>
        </div>

        <label for="office">Office</label>
        <input
          v-model="company.office"
          data-testid="office-input"
          class="form-control"
          type="text"
          name="office"
        />
        <div :class="{ 'text-danger': !valid }">
          <div v-if="v$.office.required.$invalid">Office field is required</div>
          <div v-if="v$.office.minLength.$invalid">
            Must have a length no less than 4.
          </div>
          <div v-if="v$.office.maxLength.$invalid">
            Must have a length no more than 255.
          </div>
        </div>

        <label for="contact">Contact Person</label>
        <input
          v-model="company.contact"
          data-testid="contact-input"
          class="form-control"
          type="text"
          name="contact"
        />
        <div :class="{ 'text-danger': !valid }">
          <div v-if="v$.contact.required.$invalid">
            Contact person field is required
          </div>
          <div v-if="v$.contact.minLength.$invalid">
            Must have a length no less than 4.
          </div>
          <div v-if="v$.contact.maxLength.$invalid">
            Must have a length no more than 500.
          </div>
        </div>

        <label for="phone_number">Phone</label>
        <input
          v-model="company.phone_number"
          data-testid="phone-input"
          class="form-control"
          type="text"
          name="phone-number"
        />
        <div :class="{ 'text-danger': !valid }">
          <div v-if="v$.phone_number.required.$invalid">
            Contact phone field is required
          </div>
          <div v-if="v$.phone_number.phone.$invalid">
            Phone format: +XXX 9-15 digits
          </div>
        </div>
      </div>
    </form>
    <div v-if="!valid">
      <div v-for="error of v$.$errors" :key="error.$uid">
        {{ error.$message }}
      </div>
    </div>
    <div class="btn-toolbar" role="toolbar">
      <div v-if="edit">
        <button name="remove-company" class="" @click="remove">Delete</button>
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
import rules from "../../validation/company-rules";
import { useVuelidate } from "@vuelidate/core";
import { useToast } from "vue-toastification";
import router from "../../router/index";
import axios from "../../services/api-agent";

export default {
  name: "ShippingCompanyItem",
  components: {},
  props: ["item", "editMode"],
  data() {
    return {
      valid: false,
      toast: useToast(),
      edit: this.editMode,
      company: this.item,
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
      axios.post("/companies/", this.company).then((response) => {
        this.toast.success("Shipping company successfully created!");
        router.push(`/companies/${response.data.id}`);
      });
    },
    async update() {
      const result = await this.v$.$validate();
      if (!result) {
        this.valid = false;
        this.toast.warning("Please provide valid data");
        return;
      }
      axios.put(`/companies/${this.company.id}/`, this.company).then(() => {
        this.toast.success("Shipping company successfully updated!");
        router.push(`/companies/${this.company.id}`);
      });
    },
    async remove() {
      axios.delete(`/companies/${this.company.id}`).then(() => {
        this.toast.success("Shipping company successfully removed!");
        this.$router.push({ name: "shipments" });
      });
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
