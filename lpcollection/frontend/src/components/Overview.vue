<template>
  <div>
    <div v-if="loading" class="loading">Loading...</div>

    <div v-if="error" class="error">{{ error }}</div>

    <div v-if="items" class="content">
      <h2>{{ msg }}</h2>
      <p>Here will be your collection. </p>
<button><router-link to="Add">Add new</router-link></button>
<button><router-link :to="editUrl">Edit selected</router-link></button>
<button @click="remove">Remove selected</button>
      <b-table
        striped
        hover
        dark
        selectable
        select-mode="single"
        :items="items"
        :fields="fields"
        @row-selected="onRowSelected"
      ></b-table>

      <p>Currently selected: {{selected}}</p>
    </div>
  </div>
</template>
<!-- When importing data, it must be imported into "items"-object --->
<script>

const axios = require('axios'); //required for ajax calls

export default {
  name: "Collection",
  data() {
    return {
      loading: true,
      error: null,
      msg: "This is your collection",
      selected: [],
      items: [],
      fields: [
          {
            key: 'name',
            sortable: true
          },
          {
            key: 'artist',
            sortable: true
          },
          {
            key: 'year',
            sortable: true,
          }
        ],
    };
  },
  created() {
    // fetch the data when the view is created and the data is
    // already being observed
    this.fetchData();
  },
  computed: {
    editUrl: function () {
      var url;
      if (this.selected.length == 0){
        url = "";
      }
      else {
        url = "Edit?id=" + this.selected[0]._id.$oid;
      }
      return url;
    }
  },
  watch: {
    // call again the method if the route changes
    $route: "fetchData"
  },
  methods: {
    fetchData(){
      axios
        .get('http://127.0.0.1:8000/catalog/fetchAll') //sends a message to server
        .then(data => (this.items = data.data)) 
        .catch(error => (this.error = error))
        .then(this.loading = false)
    },
    onRowSelected(items) { //selects a row when clicking
      this.selected = items;
    },
    remove: function() {
      axios
        .get('http://127.0.0.1:8000/catalog/removeOne/' + this.selected[0]._id.$oid) //sends a message to server
        .then(response => (alert(response.data))) 
        .catch(error => (this.error = error))
    }
     
  }
};
</script>

<!-- CSS that is limited to this element only -->
<style scoped></style>
