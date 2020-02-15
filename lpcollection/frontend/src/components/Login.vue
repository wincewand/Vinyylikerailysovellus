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
<!-- Temporary link for dev purposes, skips login -->
<router-link to="Overview">Skip</router-link>
  </div>
</template>

<script>
export default {
  name: 'Login',
  data () {
    return {
      msg: 'Login',
      form: {
          email: '',
          password: ''
        }
    }
  },
   methods: {
      onSubmit(evt) {
        evt.preventDefault()
        alert(JSON.stringify(this.form))
      },
      onReset(evt) {
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
