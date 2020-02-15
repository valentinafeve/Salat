<template>
  <div id="app">
    <Information/>
    <Login/>
  </div>
</template>

<script>
import Login from './views/Login'
import Information from './views/Information'
export default {
  name: 'App',
  components: {
    Login,
    Information
  }
}
</script>

<style>
#app {
  font-family: 'Open Sans', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
