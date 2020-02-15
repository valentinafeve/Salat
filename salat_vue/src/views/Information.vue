<template id="information">
  <div class="information">
    <div class="max-w-sm rounded overflow-hidden shadow-lg card">
        <div class="title">
          Resultados para los últimos X años.
        </div>
        <hr id="hr1"><hr id="hr2">
        <div class="w-full max-w-sm">
          <div class="md:items-center mb-6">

            <div class="data_results">
              Data
            </div>

            <button class="bg-red-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
              Send to email
            </button>
            <button @click="to_pdf" class="bg-red-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
              Export PDF
            </button>
            <button class="bg-red-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
              Login
            </button>
          </div>
        </div>
      </div>
  </div>
</template>
<script type="text/javascript">
import $ from 'jquery';
import jsPDF from 'jsPDF';

export default {
  name: 'Login',
  data(){
    return {
      username:'',
      password:''
    }
  },
  methods:{
    to_pdf(){
      var doc = new jsPDF();
      var elementHTML = $('#data_results').html();
      var specialElementHandlers = {
          '#elementH': function (element, renderer) {
              return true;
          }
      };
      doc.fromHTML(elementHTML, 15, 15, {
          'width': 170,
          'elementHandlers': specialElementHandlers
      });

      // Save the PDF
      doc.save('sample-document.pdf');
    }
  }
}
</script>
<style media="screen">
.information .title {
  font-size: 1.5em;
  margin-bottom: 40px;
}
</style>
