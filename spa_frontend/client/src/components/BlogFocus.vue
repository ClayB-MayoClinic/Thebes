<template>
   <div class="container">
<!-- eslint-disable max-len -->
    <div class = "blog-focus" >
      <h1>{{blog.post_title}}</h1>
      <h3>{{blog.post_subtitle}}</h3>
      <h5>{{blog.author}}</h5>
      <h5>{{blog.post_date}}</h5>
      <p v-html="blog.post_body">{{blog.post_body}}</p>
    </div>
   </div>
</template>

<script>
export default {
  props: {
    blog: {},
  },
};
</script>
