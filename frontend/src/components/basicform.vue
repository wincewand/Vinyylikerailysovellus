<template>
  <b-form @submit="submitForm" @reset="resetForm">
    <b-form-group id="input-group-1" label="Record name:" label-for="input-1">
      <b-form-input id="input-1" v-model="form.name" required placeholder="Enter record name" ></b-form-input>
    </b-form-group>
    <b-form-group id="input-group-2" label="Year:" label-for="input-2">
      <b-form-input id="input-2" v-model="form.year" required placeholder="Enter publishing year"></b-form-input>
    </b-form-group>
    <b-form-group id="input-group-3" label="Artist:" label-for="input-3">
      <b-form-input id="input-3" v-model="form.artist" required placeholder="Enter artist name"></b-form-input>
    </b-form-group>
    <b-button type="submit" variant="primary">Submit</b-button>
    <b-button type="reset" variant="danger">Reset</b-button>

<b-popover :show.sync="show" target="input-1" title="Popover" triggers="manual">
        Did you mean <strong>{{this.fetched.name}}?</strong><br>
        <b-button @click="suggestionSelected">Select</b-button>
      </b-popover>
  </b-form>

  
</template>
<script>
const axios = require('axios'); //required for ajax calls
var _ = require('lodash');

const basicform = {
  name: 'basicform',
  data () {
    return {
    form: {
      name: "",
      year: "",
      artist: ""
    },
    fetched: {
      name: "",
      year: "",
      artist: "",
    },
    show: false,
    justChanged: false
    }
  },
  props: ['id'],
  created: function() {
    //create a delay to data fetch, so that it doesn't make too many calls
    this.fetchMatch = _.debounce(this.fetchMatch, 300)
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
      status = 200;
      axios
        .post("http://127.0.0.1:8000/catalog/addNew/" + this.form.name + "/" + this.form.artist + "/" + this.form.year + '/' + $cookies.get("user")) //sends a message to server
        .then(response => this.nextStep(response.status))
    },
    resetForm(evt) {
      evt.preventDefault();
      // Reset our form values
      this.form.name = "";
      this.form.year = "";
      this.form.artist = "";
      // Trick to reset/clear native browser form validation state
     
    },
    nextStep(status) {
      if (this.id) { //if editing, not creating
          axios
          .get('http://127.0.0.1:8000/catalog/removeOne/' + this.id) //sends a message to server
          .then(response => (this.$router.push("Overview?status=" + response.status)))
          .catch(error => (this.error = error))
        }
        else {
          this.$router.push("Overview?status=" + status)
        }
    },
    fetchMatch(search) {
      console.log("Fetching matches")
      axios
        .post("http://127.0.0.1:8000/discogs/fetchMatching/" + search) //sends a message to server
        .then(data => (this.suggest(data.data.data[0]))) 
        .catch(error => (this.error = error))
    },
    suggest(data) {
      this.fetched.name = data.name
      this.fetched.year = data.year
      this.fetched.artist = data.artist
      if (this.fetched.name != "") {
        console.log("showing popover")
        this.show = true
      }
        
    },
    suggestionSelected () {
      this.form.name = this.fetched.name
      this.form.year = this.fetched.year
      this.form.artist = this.fetched.artist
      this.show = false
      this.justChanged = true
    }
  },
   watch: {
    'form.name': function (val) {
      //when user writes, search for matching records
      if (!this.justChanged){
        this.fetchMatch(val)
      }else {
        this.justChanged = false
      }
      
    }
    }
};
export default basicform;
</script>


