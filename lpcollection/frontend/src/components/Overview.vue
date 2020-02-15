<template>
  <div>
    <h2>{{ msg }}</h2>
    <p>Here will be your collection.</p>

    <b-table striped hover dark selectable select-mode="single" :items="items" @row-selected="onRowSelected"></b-table>

<p>Currently selected: {{selected}}</p>
  </div>
</template>
<!-- When importing data, it must be imported into "items"-object --->
<script>
export default {
  name: "Collection",
  data() {
    return {
      msg: "This is your collection",
      selected: [],
      items: [ 
        { name: "Title 1", artist: "Somebody" }, 
        { name: "Title 2", artist: "Somebody else" }
        ]
    };
  },
    methods: {
      onRowSelected(items) {
        this.selected = items
      },
  }
};
</script>

<!-- CSS that is limited to this element only -->
<style scoped></style>
