<template lang="html">
  <div class="loader">
    <div class="items-center">
      <div class="rounded shadow-lg rounded items-center card">
        <div class="title">
          Carga la información.
        </div>
        <hr id="hr1"><hr id="hr2">
        <div class="field">
          <label for="file1" class="bg-gray-400 hover:bg-gray-300 py-2 rounded">
            <img src="https://image.flaticon.com/icons/svg/149/149213.svg" alt="" style="height: 42px;">
            Cargar CSV
          </label>
          <input id="file1" type="file" name="" value="" accept=".csv" style="display:none">
        </div>
        <div class="field">
          <label for="file2" class="bg-gray-400 hover:bg-gray-300 py-2 rounded">
            <img src="https://image.flaticon.com/icons/svg/149/149213.svg" alt="" style="height: 42px;">
            Cargar CSV
          </label>
          <input id="file2" type="file" name="" value="" accept=".csv" style="display:none">
        </div>
        <div class="error_message">
          {{ message }}
        </div>
        <div class="success_message">
          La información se cargó correctamente.
        </div>
        <button class="bg-red-600 hover:bg-red-700 text-white font-bold py-2 px-4 rounded">
          Upload
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data(){
    return {
      message: 'Ocurrió un error en la línea 2 del archivo 1.'
    }
  }
}
</script>

<style lang="css" scoped>
.loader .card {
  display: block;
  padding: 40px;
  width: 80%;
  margin: 0 auto;
  background: white;
}

.loader .card *{
  margin: 0 auto;
}

.loader .title {
  font-size: 1.5em;
  margin-bottom: 40px;
}

.loader .field{
  margin-bottom: 20px;
}

.loader .field label{
  width: 60%;
  height: 120px;
  padding: 20px;
  display: block;
  font-size: 0.9em;
  margin-top: 20px;
  margin-bottom: 8px;
  background: #fafafa;
  border-width: 2px;
  color: #3e3e3e;
  border-style: dashed;
  border-color: #dcdcfe;
  text-align: center;
  vertical-align: middle;
  line-height: 32px;
  cursor: pointer;
}

.loader .error_message{
  margin-top: 20px;
  margin-bottom: 20px;
  padding-top: 10px;
  padding: 12px;
  width: 60%;
  background: #ffcdcd;
  border-radius: 10px;
  color: #454545;
}

.loader .success_message{
  margin-top: 20px;
  margin-bottom: 20px;
  padding-top: 10px;
  padding: 12px;
  width: 60%;
  background: #cdffdd;
  border-radius: 10px;
  color: #454545;
}

.loader button {
  width: 120px;
}

</style>
