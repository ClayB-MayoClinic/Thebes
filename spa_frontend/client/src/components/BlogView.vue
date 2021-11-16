<template>
 <!-- eslint-disable max-len -->
<div class="container-fluid">
    <div class="row">
        <navbar></navbar>
    </div>
    <div class="row">
        <div class="col-md-8">
           <blogfocus :blog="post"></blogfocus>
        </div>
        <div class="col-md-4">
           <bloglist :blogs="blogs" v-on:selectedPost="postSelectReceived"></bloglist>
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
      post: {},
      focusPostId: String,
    };
  },
  components: {
    bloglist: BlogList,
    navbar: NavBar,
    blogfocus: BlogFocus,
  },
  methods: {
    postSelectReceived(postId) {
      this.focusPostId = postId;
      console.log(`focusPostId: ${this.focusPostId}`);
      this.post = this.blogs[this.blogs.findIndex((x) => x.post_id === this.focusPostId)];
      console.log(`post: ${this.post.post_title}`);
    },
    getBlogs() {
      const path = 'http://127.0.0.1:8000/blog/posts';
      axios.get(path)
        .then((res) => {
          this.blogs = res.data.blogs;
          const [first] = this.blogs;
          this.post = first;
          console.log(res.data.blogs);
        })
        .catch((error) => {
          // eslint-disable-next-line
           console.error(error);
        });
    },
  },
  created() {
    this.getBlogs();
  },
};
</script>
