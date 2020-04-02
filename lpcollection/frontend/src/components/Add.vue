<template>
  <div>
    <basicform/>
    <button><router-link to="Overview">Return</router-link></button>
  </div>
</template>
<script>
import basicform from './basicform.vue'

export default {
  name: 'Add',
  components: {
    basicform
  }

}
</script>
