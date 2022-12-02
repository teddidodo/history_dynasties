import {
    createRouter,
    // createWebHashHistory,
    createWebHistory
} from "vue-router";
import routes from "./routes";

import HTTP from "../api/http_common";
import { usePage } from "../store/usePage";

const router = createRouter({
    history: createWebHistory(),
    routes,
})

async function randomDynasty(currentPage) {
    try {
      const random_dynastyPromise = HTTP.get("/random/dynasty");
      const random_dynasty = await random_dynastyPromise;
      currentPage.dynasty_headline = random_dynasty.data;
    } catch (error) {
      console.log(error);
    }
}

router.beforeEach(async (to) => {
    const currentPage = usePage();
    if (to.path === '/') {
        currentPage.page = 'home'
        await randomDynasty(currentPage)
    } else {
        currentPage.page = 'timeline'
        currentPage.dynasty = to.params.dynasty
    }
})


export default router;
