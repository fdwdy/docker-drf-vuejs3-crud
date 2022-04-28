import { createApp } from "vue";

import App from "./App.vue";
import router from "./router";
import Toast from "vue-toastification";

import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import "vue-toastification/dist/index.css";

const app = createApp(App);

app.use(router);
app.use(Toast, {
    transition: "Vue-Toastification__bounce",
    maxToasts: 20,
    newestOnTop: true
  });
app.mount("#app");

