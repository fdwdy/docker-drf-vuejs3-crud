import { required, minLength, helpers, maxLength } from "@vuelidate/validators";
import { computed } from "vue";
import dayjs from "dayjs";
import { phone, date, greaterThanZero, float } from '../validation/regexes'
import { requiredField, minLengthField, maxLengthField, phoneField } from "../validation/messages";
import { dateField, dateMinValueField, floatField, floatMinValueField } from "../validation/messages";

export default computed(() => {
    const localRules = {
        recipient: {
            required: requiredField('Recipient', required),
            minLength: minLengthField('Recipient', 4, minLength(4)),
            maxLength: maxLengthField('Recipient', 255, maxLength(255)),
        },
        destination: {
            required: requiredField('Destination', required),
            minLength: minLengthField('Destination', 4, minLength(4)),
            maxLength: maxLengthField('Destination', 255, maxLength(255)),
        },
        description: {
            required: requiredField('Description', required),
            minLength: minLengthField('Description', 4, minLength(4)),
            maxLength: maxLengthField('Description', 500, maxLength(500)),
        },
        contact_phone: {
            required: requiredField('Phone', required),
            phone: phoneField(phone),
        },
        ship_date: {
            required: requiredField('Date', required),
            date: dateField(date),
            minValue: dateMinValueField((value) => dayjs(value).diff(dayjs(), "days") >= 0),
        },
        cargoes: {
            required: helpers.withMessage("Please add at least one cargo", required),
            $each: helpers.forEach({
                name: {
                    required: requiredField('Cargo name', required),
                    minLength: minLengthField('Cargo name', 2, minLength(2)),
                },
                weight_kg: {
                    required: requiredField('Cargo weight', required),
                    float: floatField('Cargo weight', float),
                    minValue: floatMinValueField('Weight', greaterThanZero)
                },
                volume_m3: {
                    required: requiredField('Cargo volume', required),
                    float: floatField('Cargo volume', float),
                    minValue: floatMinValueField('Cargo weight', greaterThanZero)
                },
            }),
        },
    };
    return localRules;
});