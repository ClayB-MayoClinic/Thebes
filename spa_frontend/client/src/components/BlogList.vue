<template>
    <div class="container">
        <body>
            <ul v-for="(blog, index) in blogs" :key="index">
                <div class="card" style="width: 30rem;">
                    <div class="card-body">
                        <h3 class="card-title">{{blog.post_title}}</h3>
                        <p class="card-subtitle mb-2 text-muted">{{blog.post_subtitle}}</p>
                        <h6 class="card-text text-muted">By: {{blog.author}}</h6>
                        <h6 class="card-text text-muted">{{blog.post_date}}</h6>
                    </div>
                </div>
            </ul>
        </body>
    </div>
</template>

<script>
import axios from 'axios';

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
  created() {
    this.getBlogs();
  },
};
</script>
