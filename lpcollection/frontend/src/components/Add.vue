<template>
  <div>
<!-- <basicform></basicform> -->
    <b-card class="mt-3" header="Form Data Result">
      <pre class="m-0">{{ form }}</pre>
    </b-card>
  </div>
</template>
<script>

const axios = require('axios'); //required for ajax calls
// import basicform from './basicform';

export default {
  name: "Add",
  data() {
    return {
        show: true,
        form: {
          name: '',
          year: '',
          artist: '',
        },
        message: "",
    };
  },
  components: {
    // 'basicform': basicform
  },
  methods: {
    submitForm(evt){
         evt.preventDefault()
        alert(JSON.stringify(this.form))
      axios
        .post('http://127.0.0.1:8000/catalog/addNew') //sends a message to server
        .then(data => (this.message = data.data.data)) //this is stupid but works :P
        .catch(error => (this.error = error))
        .then(this.loading = false)
    },
    resetForm(evt){
         evt.preventDefault()
        // Reset our form values
        this.form.name = ''
        this.form.year = ''
        this.form.artist = ''
         // Trick to reset/clear native browser form validation state
        this.show = false
        this.$nextTick(() => {
          this.show = true
        })
    }
  }
};
</script>

<!-- CSS that is limited to this element only -->
<style scoped></style>
