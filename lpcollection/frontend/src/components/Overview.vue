<template>
  <div>
    <div v-if="loading" class="loading">Loading...</div>

    <div v-if="error" class="error">{{ error }}</div>

    <div v-if="items" class="content">
      <h2>{{ msg }}</h2>
      <p>Here will be your collection.</p>

      <b-table
        striped
        hover
        dark
        selectable
        select-mode="single"
        :items="items"
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
      items: []
    };
  },
  created() {
    // fetch the data when the view is created and the data is
    // already being observed
    this.fetchData();
  },
  watch: {
    // call again the method if the route changes
    $route: "fetchData"
  },
  methods: {
    fetchData(){
      axios
        .get('http://127.0.0.1:8000/catalog/fetchAll') //sends a message to server
        .then(data => (this.items = data.data.data)) //this is stupid but works :P
        .catch(error => (this.error = error))
        .then(this.loading = false)
    },
    onRowSelected(items) { //selects a row when clicking
      this.selected = items;
    },
    
     
  }
};
</script>

<!-- CSS that is limited to this element only -->
<style scoped></style>
