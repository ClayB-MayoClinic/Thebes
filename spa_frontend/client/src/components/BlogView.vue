<template>
 <!-- eslint-disable max-len -->
<div class="container-fluid">
    <div class="row">
        <navbar></navbar>
    </div>
    <div class="row">
        <div class="col-md-8">
           <blogfocus></blogfocus>
        </div>
        <div class="col-md-4">
           <bloglist></bloglist>
        </div>
    </div>
</div>
</template>

<script>
import axios from 'axios';

import BlogList from './BlogList.vue';
import NavBar from './NavBar.vue';
import BlogFocus from './BlogFocus.vue';

export default {
  data() {
    return {
      blogs: [],
    };
  },
  methods: {
    getBlogs() {
      const path = 'http://127.0.0.1:8000/blog/posts';
      axios.get(path)
        .then((res) => {
          this.blogs = res.data.blogs;
        })
        .catch((error) => {
          // eslint-disable-next-line
           console.error(error);
        });
    },
  },
  components: {
    bloglist: BlogList,
    navbar: NavBar,
    blogfocus: BlogFocus,
  },
  created() {
    this.getBlogs();
  },
};
</script>
