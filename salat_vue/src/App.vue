<template>
  <div id="app">
    <Header/>
    <div id="main_container">
      <router-View></router-View>
    </div>
    <Footer/>
  </div>
</template>

<script>
import Header from './components/header.vue'
import Footer from './components/footer.vue'

export default {
  name: 'App',
  components: {
    Header,
    Footer
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
  margin-top: 0px;
  width: 100%;
  background: url("https://cdn.pixabay.com/photo/2018/12/25/11/10/deer-3894103_960_720.png");
}
#main_container{
  width: 100%;
  padding-top: 50px;
  padding-bottom: 40px;
}
</style>
