<template>
  <div>
    <div v-if="loading" class="loading">Loading...</div>

    <div v-if="error" class="error">{{ error }}</div>

    <div v-if="post" class="content">
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
export default {
  name: "Collection",
  data() {
    return {
      loading: false,
      post: null,
      error: null,
      msg: "This is your collection",
      selected: [],
      items: [
        { name: "Title 1", artist: "Somebody" },
        { name: "Title 2", artist: "Somebody else" }
      ]
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
    onRowSelected(items) {
      this.selected = items;
    },
    
     async fetchData () {
      try {
        const { data } = await this.$http.get(
        'http://127.0.0.1:8000/catalog/fetchAll',
          { name: "something" }
        );
        // do stuff
         console.log(data);
        this.post = "dataa";
      } catch (err) {
        // uh oh, didn't work, time for plan B
        this.error = err.toString();
      }
  }}
};
</script>

<!-- CSS that is limited to this element only -->
<style scoped></style>
