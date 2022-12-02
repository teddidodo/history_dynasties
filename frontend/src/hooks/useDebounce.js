import { ref, onMounted } from 'vue';

export default function useDebounce(value, delay) {
    let debouncedValue = ref(value);

    onMounted(
        () => {
            const handler = setTimeout(() => {
                debouncedValue = value;
            }, delay);
            return () => {
                clearTimeout(handler);
            };
        },
    );
    

    return debouncedValue;
}
