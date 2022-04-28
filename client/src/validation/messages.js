import { helpers } from "@vuelidate/validators";


const requiredField = (fieldName, rule) => helpers.withMessage(`${fieldName} field is required`, rule);
const minLengthField = (fieldName, min, rule) => helpers.withMessage(`${fieldName} should be at least ${min} long`, rule);
const maxLengthField = (fieldName, max, rule) => helpers.withMessage(`${fieldName} should be at least ${max} long`, rule);
const phoneField = (rule) => helpers.withMessage(`Phone format: +XXX 9-15 digits`, rule);
const dateField = (rule) => helpers.withMessage(`Invalid Date`, rule);
const dateMinValueField = (rule) => helpers.withMessage(`The date has already passed`, rule);
const floatField = (fieldName, rule) => helpers.withMessage(`${fieldName} must be float`, rule);
const floatMinValueField = (fieldName, rule) => helpers.withMessage(`${fieldName} must be above zero`, rule);

export {
    requiredField, minLengthField, maxLengthField, phoneField,
    dateField, dateMinValueField, floatField, floatMinValueField
}