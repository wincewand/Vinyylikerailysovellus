export default
Vue.component('basicform', {
  data: function () {
    return {
      form: {
          name: "",
          year: "",
          artist: ""
      }
    }
  },
  template: '<b>Hei</b>'
//   template: '<b-form @submit="submitForm" @reset="resetForm" v-if="show"><b-form-group id="input-group-1" label="Record name:" label-for="input-1" >        <b-form-input          id="input-1"          v-model="form.name"          required          placeholder="Enter record name"        ></b-form-input>      </b-form-group>      <b-form-group id="input-group-2" label="Year:" label-for="input-2">        <b-form-input          id="input-2"          v-model="form.year"          required          placeholder="Enter publishing year"        ></b-form-input>      </b-form-group>      <b-form-group id="input-group-3" label="Artist:" label-for="input-3">        <b-form-input          id="input-3"          v-model="form.artist"          required          placeholder="Enter artist name"        ></b-form-input>      </b-form-group>      <b-button type="submit" variant="primary">Submit</b-button>      <b-button type="reset" variant="danger">Reset</b-button>    </b-form>'
  })
