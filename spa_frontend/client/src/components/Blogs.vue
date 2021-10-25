<template>
   <div class="container">
        <div class="row">
            <div class="col-sm-10">
                <h1>Blog Posts</h1>
                <br><br>
                <table class="table table-hover">
                    <thead>
                        <th scope="col">id</th>
                        <th scope="col">post_date</th>
                        <th scope="col">edit_date</th>
                        <th scope="col">location</th>
                        <th scope="col">author</th>
                        <th scope="col">author_id</th>
                        <th scope="col">post_title</th>
                        <th scope="col">post_subtitle</th>
                        <th scope="col">post_body</th>
                        <th scope="col">post_tags</th>
                    </thead>
                    <tbody>
                        <tr v-for="(blog, index) in blogs" :key="index">
                            <td>{{blog.post_id}}</td>
                            <td>{{blog.post_date}}</td>
                            <td>{{blog.edit_date}}</td>
                            <td>{{blog.location}}</td>
                            <td>{{blog.author}}</td>
                            <td>{{blog.author_id}}</td>
                            <td>{{blog.post_title}}</td>
                            <td>{{blog.post_subtitle}}</td>
                            <td>{{blog.post_body}}</td>
                            <td>{{blog.post_tags}}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
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
