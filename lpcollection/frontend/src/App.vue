<template>
  <div id="app">
    <b-container>
    <h1>Vinyl Collector</h1>
    <router-view/>
    </b-container>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Kaushan+Script|Oswald&display=swap');
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: white;
  margin-top: 60px;
}
h1 {
font-family: 'Kaushan Script', cursive;
font-size: 3em;
  }
  h2 {
    font-family: 'Oswald', sans-serif;
    }
body {
  background-color:#4d4365;
  }
</style>
