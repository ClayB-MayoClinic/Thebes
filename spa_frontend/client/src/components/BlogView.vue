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
import BlogList from './BlogList.vue';
import NavBar from './NavBar.vue';
import BlogFocus from './BlogFocus.vue';

export default {
  components: {
    bloglist: BlogList,
    navbar: NavBar,
    blogfocus: BlogFocus,
  },
};
</script>
