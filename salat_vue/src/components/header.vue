<template lang="html">
  <div class="header">
    <div class="title">
      A bank
    </div>
    <hr id="hr-header1">
    <hr id="hr-header2">
  </div>
</template>

<script>
export default {
}
</script>

<style lang="css" scoped>
.header {
  top: 0;
  z-index: 3;
  margin-top: 0px;
  width: 100%;
  height: 140px;
  background: #fefefe;
  box-shadow: 2px 2px 12px 5px rgba(0, 0, 0, 0.2);
  position: relative;
}
.header .title{
  color: #E53E3E;
  font-size: 4em;
  text-shadow: 2px 2px 7px #fefefe;
  margin: 0 auto;
  margin-top: 40px;
  display: inline-block;
}

#hr-header1{
  width: 90%;
  bottom: 0;
  position: absolute;
  border-top: 4px solid #E53E3E;
}
#hr-header2{
  width: 10%;
  bottom: 0;
  right: 0;
  position: absolute;
  border-top: 4px solid #9966ff;
}
</style>
