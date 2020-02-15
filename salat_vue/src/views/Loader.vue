<template lang="html">
  <div class="loader">
    <div class="items-center">
      <div class="rounded shadow-lg rounded items-center card">
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
        <button class="bg-red-600 hover:bg-red-700 text-white font-bold py-2 px-4 rounded">
          Upload
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
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

.loader button {
  width: 120px;
}

</style>
