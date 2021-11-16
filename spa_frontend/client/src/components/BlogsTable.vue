<template>
 <!-- eslint-disable max-len -->
   <div class="container-fluid">
      <div class="row">
        <navbar></navbar>
      </div>
      <div class="row">
          <div class="col-sm-10">
              <h1>Blog Posts</h1>
              <br><br>
              <button type="button" class="btn btn-success btn-sm" v-b-modal.blog-modal>Add Post</button>
              <table class="table table-bordered">
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
                          <td>{{blog.post_body}} </td>
                          <td>{{blog.post_tags}}</td>
                          <td>
                            <div class="btn-group" role="group">
                              <button type="button" class="btn btn-warning btn-sm">Update</button>
                            </div>
                          </td>
                      </tr>
                  </tbody>
              </table>
          </div>
      </div>
      <b-modal ref="addBlogModal"
               id="blog-modal"
               title="Add a new post"
               hide-footer>
        <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        </b-form>
      </b-modal>
    </div>
</template>

<script>
import axios from 'axios';

import NavBar from './NavBar.vue';

export default {
  data() {
    return {
      blogs: [],
      addBlogForm: {
        id: '',
        post_date: '',
        edit_date: '',
        location: '',
        author: '',
        author_id: '',
        post_title: '',
        post_subtitle: '',
        post_body: '',
        post_tags: '',
      },
    };
  },
  components: {
    navbar: NavBar,
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
    addBlog(payload) {
      const path = 'http://127.0.0.1:8000/blog/posts';
      axios.post(path, payload)
        .then(() => {
          this.getBlogs();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getBlogs();
        });
    },
    initForm() {
      this.addBlogForm.id = '';
      this.addBlogForm.post_date = '';
      this.addBlogForm.edit_date = '';
      this.addBlogForm.location = '';
      this.addBlogForm.author = '';
      this.addBlogForm.author_id = '';
      this.addBlogForm.post_title = '';
      this.addBlogForm.post_subtitle = '';
      this.addBlogForm.post_body = '';
      this.addBlogForm.post_tags = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addBlogModal.hide();
      const payload = {
        id: this.addBlogForm.id,
        post_date: this.addBlogForm.post_date,
        edit_date: this.addBlogForm.edit_date,
        location: this.addBlogForm.location,
        author: this.addBlogForm.author,
        author_id: this.addBlogForm.author_id,
        post_title: this.addBlogForm.post_title,
        post_subtitle: this.addBlogForm.post_subtitle,
        post_body: this.addBlogForm.post_body,
        post_tags: this.addBlogForm.post_tags,
      };
      this.addBlog(payload);
      this.initForm();
    },
    OnReset(evt) {
      evt.preventDefault();
      this.$refs.addBlogModal.hide();
      this.initForm();
    },
  },
  created() {
    this.getBlogs();
  },
};
</script>
