<template>
  <div>
    <basicform v-bind:id="id"/> 
  </div>
</template>
<script>
import basicform from './basicform.vue';

export default {
  name: "Edit",
  components: {
     basicform
  },
  props: ['id']

};
</script>