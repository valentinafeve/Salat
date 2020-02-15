<template lang="html">
  <div class="footer">
    <div class="info">
      <div class="item">
        <div class="icon">
          <img src="https://image.flaticon.com/icons/svg/1034/1034131.svg" alt="" style="height: 42px">
        </div>
        <div class="title">
          Llámanos
        </div>
        <div class="info">
          1234567
        </div>
        <div class="vl"/>
      </div>
      <div class="item">
        <div class="icon">
          <img src="https://image.flaticon.com/icons/svg/1034/1034162.svg" alt="" style="height: 42px">
        </div>
        <div class="title">
          ¿Necesitas información?
        </div>
        <div class="info">
          email@unemail.com
        </div>
        <div class="vl"/>
      </div>
      <div class="item">
        <div class="icon">
          <img src="https://image.flaticon.com/icons/svg/1034/1034129.svg" alt="" style="height: 42px">
        </div>
        <div class="title">
          ¿Dónde estámos?
        </div>
        <div class="info">
          Dirección, Bogotá, Colombia
        </div>
      </div>
    </div>
    <div class="more_info">
      Más palabras
    </div>
  </div>
</template>

<script>
export default {
}
</script>

<style lang="css" scoped>

.footer {
  width: 100%;
  height: 270px;
  color: white;
  position: relative;
  margin-top: 30px;
  padding-top: 40px;
  padding-bottom: 90px;
  background: #3e3e4d;
  box-shadow: -1px -6px 20px 9px rgba(0, 0, 0, 0.1);
}

.footer .item{
  color: #efefef;
  width: 25%;
  vertical-align: top;
  min-width: 120px;
  display: inline-block;
  position: relative;
}

.footer .item .icon img{
  margin: 0 auto;
  margin-bottom: 15px;
}
.footer .item .title{
  margin: 0 auto;
  font-size: 1.2em;
  margin-bottom: 10px;
}
.footer .more_info{
  padding-top: 15px;
  font-size: 0.9em;
  width: 100%;
  height: 50px;
  bottom: 0;
  position: absolute;
  background: #ED0722;
}

.footer .vl {
  border-left: 1.5px solid #9e9ead;
  height: 100%;
  position: absolute;
  right: 0;
  top: 0;
}

</style>
