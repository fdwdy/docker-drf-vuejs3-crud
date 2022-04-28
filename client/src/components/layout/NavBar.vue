<template>
  <nav class="navbar navbar-expand navbar-dark bg-dark">
    <router-link
      to="/"
      class="navbar-brand"
    >
      Shipments
    </router-link>
    <div class="navbar-nav mr-auto">
      <li class="nav-item">
        <router-link
          to="/shipments/add"
          data-testid="add-shipment"
          class="nav-link"
        >
          Add Shipment
        </router-link>
      </li>
      <li class="nav-item">
        <router-link
          to="/companies/add"
          class="nav-link"
        >
          Add Company
        </router-link>
      </li>
    </div>
  </nav>
</template>
<script>
export default {
  name: "navigation-bar",
};
</script>