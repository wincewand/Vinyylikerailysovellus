<template>
  <div>
    <h2>{{ msg }}</h2>

 <div>
    <b-form @submit="onSubmit" @reset="onReset">
      <b-form-group
        id="input-group-1"
        label="Email address:"
        label-for="input-1"
      >
        <b-form-input
          id="input-1"
          v-model="form.email"
          type="email"
          required
          placeholder="Enter email"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2" label="Password:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="form.password"
          required
          placeholder="Enter password"
        ></b-form-input>
      </b-form-group>

      <b-button type="AddUser" variant="light">Add User</b-button>
      <b-button type="submit" variant="light">Submit</b-button>
      <b-button type="reset" variant="secondary">Reset</b-button>
    </b-form>
<!---
///This is for debug purposes:
    <b-card class="mt-3" header="Form Data Result">
      <pre class="m-0">{{ form }}</pre>
    </b-card>
-->
  </div>
<!-- Temporary link for dev purposes, skips login --->
<router-link to="Overview">Skip</router-link>
  </div>
</template>

<script>
const axios = require('axios') // required for ajax calls
export default {
  name: 'login',
  data () {
    return {
      msg: 'login',
      form: {
        email: '',
        password: ''
      }
    }
  },
  methods: {
    AddUser (evt) {
      evt.preventDefault()
      alert(JSON.stringify(this.form))
      axios
        .get('http://127.0.0.1:8000/login/fetchOneUser/' + this.email) // sends a message to server
        .then(data => (this.form = data.data.data[0])) // this is stupid but works :P
        .catch(error => (this.error = error))
    },
    onSubmit (evt) {
      evt.preventDefault()
      axios
        .post('http://127.0.0.1:8000/catalog/addNewUser/' + this.form.email + '/' + this.form.password) // sends a message to server
        .then(data => (alert(data.data)))
        .catch(error => (this.error = error))
        .then((this.loading = false))
    },
    onReset (evt) {
      evt.preventDefault()
      // Reset our form values
      this.form.email = ''
      this.form.password = ''
    }
  }
}
</script>

<!-- CSS that is limited to this element only -->
<style scoped>

</style>
