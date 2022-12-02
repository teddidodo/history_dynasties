import { createApp } from 'vue';
import App from './App.vue';
import { Quasar } from 'quasar';
import quasarUserOptions from './quasar-user-options';
import { createPinia } from 'pinia'

import router from './routes/router';

createApp(App)
    .use(Quasar, quasarUserOptions)
    .use(createPinia())
    .use(router)
    .mount('#app');

