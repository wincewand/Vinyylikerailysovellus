<template>
  <b-form @submit="submitForm" @reset="resetForm">
    <b-form-group id="input-group-1" label="Record name:" label-for="input-1">
      <b-form-input id="input-1" v-model="form.name" required placeholder="Enter record name"></b-form-input>
    </b-form-group>
    <b-form-group id="input-group-2" label="Year:" label-for="input-2">
      <b-form-input id="input-2" v-model="form.year" required placeholder="Enter publishing year"></b-form-input>
    </b-form-group>
    <b-form-group id="input-group-3" label="Artist:" label-for="input-3">
      <b-form-input id="input-3" v-model="form.artist" required placeholder="Enter artist name"></b-form-input>
    </b-form-group>
    <b-button type="submit" variant="primary">Submit</b-button>
    <b-button type="reset" variant="danger">Reset</b-button>
   
  </b-form>
</template>

<script>
const axios = require('axios'); //required for ajax calls
const basicform = {
  name: 'basicform',
  data () {
    return {
    form: {
      name: "",
      year: "",
      artist: ""
    }}
  },
  props: ['id'],
  created: function() {
    if (this.id){
      //fetch data
      axios
        .get('http://127.0.0.1:8000/catalog/fetchOne/' + this.id) //sends a message to server
        .then(data => (this.form = data.data.data[0])) //this is stupid but works :P
        .catch(error => (this.error = error))
    }
  },
  methods: {
    submitForm(evt) {
      evt.preventDefault();
      axios
        .post("http://127.0.0.1:8000/catalog/addNew/" + this.form.name + "/" + this.form.artist + "/" + this.form.year) //sends a message to server
        .then(data => (alert(data.data))) 
        .catch(error => (this.error = error))
        .then((this.loading = false));
    },
    resetForm(evt) {
      evt.preventDefault();
      // Reset our form values
      this.form.name = "";
      this.form.year = "";
      this.form.artist = "";
      // Trick to reset/clear native browser form validation state
      this.show = false;
      this.$nextTick(() => {
        this.show = true;
      });
    }
  }
};
export default basicform;
</script>


