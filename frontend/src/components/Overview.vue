<template>
  <div>
    <div style="position:absolute;left:10px;top:10px;"><b-button @click="logOut">Log Out</b-button></div>
    <h2>Welcome {{loggedUser}}!</h2>

    <b-modal v-model="showStatus">{{msg}}</b-modal>

    <div v-if="items" class="content">
      <br />
      <b-form-input
        v-model="filter"
        type="search"
        id="filterInput"
        placeholder="Type to Search"
        class="w-50 m-auto"
      ></b-form-input>
      <br />
      <b-button>
        <router-link to="Add">Add new</router-link>
      </b-button>
      <b-button>
        <router-link :to="editUrl">Edit selected</router-link>
      </b-button>
      <b-button @click="remove">Remove selected</b-button>

      <br />
      <br />
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
const axios = require("axios"); //required for ajax calls

export default {
  name: "Collection",
  data() {
    return {
      done: false,
      error: null,
      msg: null,
      propStatus: null,
      showStatus: false,
      selected: [],
      items: [],
      filter: null,
      filterOn: ["name", "artist", "year"],
      fields: [
        {
          key: "name",
          sortable: true
        },
        {
          key: "artist",
          sortable: true
        },
        {
          key: "year",
          sortable: true
        }
      ]
    };
  },
  props: ["status"],
  created() {
    // fetch the data when the view is created and the data is
    // already being observed
    this.propStatus = this.status;
    if (this.status) {
      this.showModal(this.status);
    }
    else {
      this.fetchData();
    }
  },
  computed: {
    editUrl: function() {
      var url;
      if (this.selected.length == 0) {
        url = "";
      } else {
        url = "Edit?id=" + this.selected[0]._id.$oid;
      }
      return url;
    },
    loggedUser: function() {
      return $cookies.get("user");
    }
  },
  methods: {
    logOut: function() {
      $cookies.remove('user')
      this.$router.push("/")
    },
    fetchData() {
      axios
        .get("http://127.0.0.1:8000/catalog/fetchAll/" + $cookies.get("user")) //sends a message to server
        .then(data => (this.items = data.data))
        .catch(error => (this.error = error));
    },
    onRowSelected(items) {
      //selects a row when clicking
      this.selected = items;
    },
    remove: function() {
      axios
        .get(
          "http://127.0.0.1:8000/catalog/removeOne/" +
            this.selected[0]._id.$oid +
            "/" +
            $cookies.get("user")
        ) //sends a message to server
        .then(data => this.showModal(data.status))
        .catch(error => (this.error = error));
    },
    showModal(status) {
      this.propStatus = status;
      this.fetchData();
      switch (status) {
        case "200":
        case 200:
          this.msg = "Action successful!";
          break;
        default:
          this.msg = "Something went wrong";
      }
      this.showStatus = true;
    }
  }
};
</script>

<!-- CSS that is limited to this element only -->
<style scoped></style>
