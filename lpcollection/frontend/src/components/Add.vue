<template>
  <div>
    <basicform/> <br>
    <b-button><router-link to="Overview">Return</router-link></b-button>
  </div>
</template>
<script>
import basicform from './basicform.vue';

export default {
  name: "Add",
  components: {
     basicform
  },

};
</script>