import axios from "axios";
import { useToast } from 'vue-toastification'

const toast = useToast()

const axios_instance = axios.create({
  baseURL: import.meta.env.VITE_APP_API_URL,
  headers: {
    "Content-type": "application/json",
  }
});

axios_instance.interceptors.request.use(
  (request) => {
    return request;
  },
  (error) => {
    const { status } = error.request;
    toast.error(status + '. ' + error)
    return Promise.reject(error);
  }
);

axios_instance.interceptors.response.use(
  (response) => {
    return response;
  },
  (error) => {
    toast.error('Api error ' + error)
    return Promise.reject(error);
  }
);

export default axios_instance