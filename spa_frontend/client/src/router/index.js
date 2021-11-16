import Vue from 'vue';
import Router from 'vue-router';
import Books from '../components/Books.vue';
import Ping from '../components/Ping.vue';
import Blogs from '../components/BlogsTable.vue';
import BlogList from '../components/BlogList.vue';
import BlogView from '../components/BlogView.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Books',
      component: Books,
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
    {
      path: '/blogstable',
      name: 'blogstable',
      component: Blogs,
    },
    {
      path: '/bloglist',
      name: 'BlogList',
      component: BlogList,
    },
    {
      path: '/blog',
      name: 'BlogView',
      component: BlogView,
    },
  ],
});
