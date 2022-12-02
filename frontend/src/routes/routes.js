import HTTP from "../api/http_common";

const routes = [    
    {
      path: '/',
      component: () => import('@/layouts/AppLayout.vue'),
      children: [
        {
          path: '',
          name: 'overview',
          component: () => import('../views/Home')
          
        },
        {
          path: '/:dynasty',
          name: 'timeline',
          component: () => import('../views/Timeline'),
          async beforeEnter(to) {
            try {
              const dynastyPromise = HTTP.get("/dynasties/" + to.params.dynasty)
              await dynastyPromise;
            } catch (error) {
              console.log(error);
              return {name: 'not_found'}
            }
          }
        }
      ]
    },
    {
      path: '/not_found',
      name: 'not_found',
      component: () => import('@/views/NotFound.vue'),  
    }
  
  ];
  
  export default routes;
  