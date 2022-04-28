<template>
  <div>
    <h3 class="heading">CompanyView</h3>
    <ShippingCompanyForm
      :item="company"
      :edit-mode="edit"
    />
  </div>
</template>
<script>
import axios from "../services/api-agent";
import ShippingCompanyForm from "../components/companies/ShippingCompanyForm.vue";

export default {
  name: "ShippingCompanyItem",
  components: { ShippingCompanyForm },
  beforeRouteEnter(to, from, next) {
    if (!to.params.id) {
      let company = {
        id: null,
        name: "",
        office: "",
        contact: "",
        phone_number: "",
      };
      next((vm) => {
        vm.edit = false;
        Object.assign(vm.company, company);
      });
    } else {
      axios
        .get(`/companies/${to.params.id}`)
        .then(function (response) {
          next((vm) => {
            vm.edit = true;
            Object.assign(vm.company, response.data);
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
      company: {},
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
