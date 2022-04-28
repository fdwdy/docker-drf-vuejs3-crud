import { required, minLength, maxLength } from "@vuelidate/validators";
import { computed } from "vue";
import { phone } from '../validation/regexes'
import { requiredField, minLengthField, maxLengthField, phoneField } from "../validation/messages";


export default computed(() => {
    const localRules = {
        name: {
            required: requiredField('Name', required),
            minLength: minLengthField('Name', 4, minLength(4)),
            maxLength: maxLengthField('Name', 255, maxLength(255)),
        },
        office: {
            required: requiredField('office', required),
            minLength: minLengthField('office', 4, minLength(4)),
            maxLength: maxLengthField('office', 255, maxLength(255)),
        },
        contact: {
            required: requiredField('contact', required),
            minLength: minLengthField('contact', 4, minLength(4)),
            maxLength: maxLengthField('contact', 255, maxLength(255)),
        },
        phone_number: {
            required: requiredField('Phone', required),
            phone: phoneField(phone),
        },
    };
    return localRules;
});