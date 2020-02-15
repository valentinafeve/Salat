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
          7565076
        </div>
      </div>
      <div class="item">
        <div class="icon">
          <img src="https://image.flaticon.com/icons/svg/1034/1034162.svg" alt="" style="height: 42px">
        </div>
        <div class="title">
          ¿Necesitas información?
        </div>
        <div class="info">
          asociados@fondecol.co
        </div>
      </div>
      <div class="item">
        <div class="icon">
          <img src="https://image.flaticon.com/icons/svg/1034/1034129.svg" alt="" style="height: 42px">
        </div>
        <div class="title">
          ¿Dónde estámos?
        </div>
        <div class="info">
          Calle 24 No. 9 – 31 Oficina 209, Bogotá, Cundinamarca, 110111, CO
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
  margin-top: 30px;
  font-size: 0.9em;
}

</style>
