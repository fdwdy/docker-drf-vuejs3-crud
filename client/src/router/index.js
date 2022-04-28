import { createWebHistory, createRouter } from "vue-router";

const routes =  [
  {
    path: "/",
    alias: "/shipments",
    name: "shipments",
    component: () => import("../views/Home.vue")
  },
  {
    path: "/shipments/:id",
    name: "shipments-details",
    component: () => import("../views/Shipment.vue")
  },
  {
    path: "/shipments/add",
    name: "shipments-add",
    component: () => import("../views/Shipment.vue")
  },
  {
    path: "/companies/:id",
    name: "companies-details",
    component: () => import("../views/Company.vue")
  },
  {
    path: "/companies/add",
    name: "companies-add",
    component: () => import("../views/Company.vue")
  }
];
const router = createRouter({
  history: createWebHistory(),
  routes,
});
export default router;