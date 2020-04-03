<template>
  <div>
  
    <b-modal v-model="showStatus">{{msg}}</b-modal>

    <div v-if="items" class="content">
      <br>
<b-form-input
              v-model="filter"
              type="search"
              id="filterInput"
              placeholder="Type to Search"
              class="w-50 m-auto"
            ></b-form-input>
<br>
<b-button><router-link to="Add">Add new</router-link></b-button>
<b-button><router-link :to="editUrl">Edit selected</router-link></b-button>
<b-button @click="remove">Remove selected</b-button>
            
<br><br>
      <b-table
        striped
        hover
        dark
        selectable
        select-mode="single"
        :items="items"
        :fields="fields"
        @row-selected="onRowSelected"
        :filter="filter"
      :filterIncludedFields="filterOn"
      class="dataTable"
      ></b-table>

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
      done: false,
      error: null,
      msg: null,
      showStatus: false,
      selected: [],
      items: [],
      filter: null,
        filterOn: ['name', 'artist', 'year'],
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
  props: ['status'],
  created() {
    // fetch the data when the view is created and the data is
    // already being observed
    this.fetchData();
    if (this.status){
      this.showModal()
    }
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
  methods: {
    fetchData(){
      this.done = false
      axios
        .get('http://127.0.0.1:8000/catalog/fetchAll') //sends a message to server
        .then(data => (this.items = data.data)) 
        .catch(error => (this.error = error))
        
    },
    onRowSelected(items) { //selects a row when clicking
      this.selected = items;
    },
    remove: function() {
      this.done = false
      axios
        .get('http://127.0.0.1:8000/catalog/removeOne/' + this.selected[0]._id.$oid) //sends a message to server
        .then(data => this.status = data.status, this.showModal(), this.fetchData())
        .catch(error => (this.error = error))
    },
    showModal () {
      switch(this.status){
        case "200":
        case 200:
           this.msg = "Action successful!";break;
        default: this.msg = "Something went wrong.";
      }
    this.showStatus = true;
    }
  }
};
</script>

<!-- CSS that is limited to this element only -->
<style scoped></style>
