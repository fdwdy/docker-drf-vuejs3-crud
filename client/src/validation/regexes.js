import { helpers } from "@vuelidate/validators";


const phone = helpers.regex(/^\+\d{9,15}$/);
const date = helpers.regex(/^\d{4}-\d{2}-\d{2}$/);
const float = helpers.regex(/^\d+((.\d+))?(,\d+((.\d+))?)*$/);
const greaterThanZero = (value) => value > 0;

export { phone, date, float, greaterThanZero }