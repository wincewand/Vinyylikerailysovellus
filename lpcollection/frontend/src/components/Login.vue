<template>
  <div>
    <h2>{{ msg }}</h2>

 <div><b-button :pressed.sync="loginBtn" variant="primary" type="button">{{btnMessage}}</b-button>

    <b-form @submit="onSubmit" @reset="onReset">

      <b-form-group
        id="input-group-1"
        label="Name:"
        label-for="input-1"
      >
        <b-form-input
          id="input-1"
          v-model="form.name"
          type="text"
          required
          placeholder="Enter name"
          
        ></b-form-input>
      </b-form-group>

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
          type="password"
          placeholder="Enter password"
        ></b-form-input>
      </b-form-group>

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
      loginBtn: false,
      form: {
        email: '',
        password: '',
        name: '',
      }
    }
  },
  computed: {
    btnMessage: function () {
      if (this.loginBtn)
        return "Create Account"
      else 
        return "Log In"
    }
  },
  methods: {
    onSubmit (evt) {
       evt.preventDefault()

    if (!this.loginBtn){
      axios
        .get('http://127.0.0.1:8000/login/createUser/' + this.form.name + '/' + this.form.email + '/' + this.form.password) // sends a message to server
        .then(data => alert(data.data)) 
    }
    else {
      axios
      .get('http://127.0.0.1:8000/login/logIn/' + this.form.name + '/' + this.form.email + '/' + this.form.password) // sends a message to server
        .then(data => this.login(data.data)) 
    }
    },
    login (status) {
      if (status == true){
        this.$cookies.set("user", this.form.name)
        this.$router.push("Overview")
      }
      else {
        alert("Login failed!")
      }
    },

    onReset (evt) {
      evt.preventDefault()
      // Reset our form values
      this.form.email = ''
      this.form.password = ''
    },
  }
}
</script>

<!-- CSS that is limited to this element only -->
<style scoped>

</style>
