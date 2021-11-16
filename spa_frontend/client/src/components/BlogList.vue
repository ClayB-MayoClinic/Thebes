<template>
    <div class="container">
        <body>
            <ul v-for="blog in blogs" v-bind:key="blog.post_id">
                <div class="card" v-on:click="cardSelect(blog.post_id)" style="width: 30rem;">
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
export default {
  props: {
    blogs: [],
  },
  methods: {
    cardSelect(postId) {
      this.$emit('selectedPost', postId);
    },
  },
};
</script>
