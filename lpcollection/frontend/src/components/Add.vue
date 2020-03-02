<template>
  <div>
     <b-form @submit="submitForm" @reset="resetForm" v-if="show">
      <b-form-group
        id="input-group-1"
        label="Record name:"
        label-for="input-1"
      >
        <b-form-input
          id="input-1"
          v-model="form.name"
          required
          placeholder="Enter record name"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2" label="Year:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="form.year"
          required
          placeholder="Enter publishing year"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-3" label="Artist:" label-for="input-3">
        <b-form-input
          id="input-3"
          v-model="form.artist"
          required
          placeholder="Enter artist's full name"
        ></b-form-input>
      </b-form-group>

      <b-button type="submit" variant="primary">Submit</b-button>
      <b-button type="reset" variant="danger">Reset</b-button>
    </b-form>
    <b-card class="mt-3" header="Form Data Result">
      <pre class="m-0">{{ form }}</pre>
    </b-card>
  </div>
</template>
<script>

const axios = require('axios'); //required for ajax calls

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
