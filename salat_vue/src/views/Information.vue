<template id="information">
  <div class="information">
    <div class="rounded overflow-hidden shadow-lg card items-center card">
        <div class="title">
          Resultados para los últimos X años.
        </div>
        <hr id="hr1"><hr id="hr2">
        <div class="w-full">
          <div class="md:items-center mb-6">
            <div id="data_results">
              <div class="">
                Nombre: {{ name }}
              </div>
              <div class="">
                Dirección: {{ address }}
              </div>
              <table class="table-auto">
                <thead>
                  <tr>
                    <th class="px-4 py-2">Ref</th>
                    <th class="px-4 py-2">Amount</th>
                    <th class="px-4 py-2">Date</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="loan of loans" v-bind:key="loan">
                    <td class="border px-4 py-2">{{ loan.ref }}</td>
                    <td class="border px-4 py-2">{{ loan.amount }}</td>
                    <td class="border px-4 py-2">{{ loan.date}}</td>
                  </tr>
                </tbody>
              </table>
            </div>
            <div class="buttons">
              <button @click="to_pdf" class="bg-red-600 hover:bg-red-700 text-white font-bold py-2 px-4 rounded">
                Exportar a PDF
              </button>
              <button @click="to_email" class="bg-red-600 hover:bg-red-700 text-white font-bold py-2 px-4 rounded">
                Enviar por correo
              </button>
              <button @click="to_print" class="bg-red-600 hover:bg-red-700 text-white font-bold py-2 px-4 rounded">
                Imprimir
              </button>
            </div>
          </div>
        </div>
      </div>
  </div>
</template>
<script type="text/javascript">
import $ from 'jquery';
import jsPDF from 'jspdf';

export default {
  name: 'Login',
  data(){
    return {
      name: 'Dorothy Valencia',
      address: 'Cra 10 #65 - 32',
      loans: [
        {
          ref: '6317893',
          amount: 20000,
          date: '24 DEC 2018'
        },
        {
          ref: '6317893',
          amount: 20000,
          date: '24 DEC 2018'
        },
        {
          ref: '6317893',
          amount: 20000,
          date: '24 DEC 2018'
        },
        {
          ref: '6317893',
          amount: 20000,
          date: '24 DEC 2018'
        }
      ]
    }
  },
  methods:{
    to_pdf(){
      var doc = new jsPDF();
      var elementHTML = $('#data_results').html();
      var specialElementHandlers = {
          '#elementH': function (element, renderer) {
              console.log(element)
              console.log(renderer)
              return true;
          }
      };
      doc.fromHTML(elementHTML, 15, 15, {
          'width': 170,
          'elementHandlers': specialElementHandlers
      });

      // Save the PDF
      var d = new Date()
      doc.save('fondecol_'+d.getTime()+'.pdf');
    },
    to_email(){
      window.open('mailto:test@example.com?subject=subject&body=body');
    },
    to_print(){
      var originalContent = window.document.body.innerHTML;
      var elementHTML = document.getElementById('data_results');
      console.log(elementHTML);
      window.document.body.innerHTML = elementHTML.innerHTML;
      window.print();
      window.document.body.innerHTML = originalContent;
    }
  }
}
</script>
<style media="screen">
.information .card {
  display: block;
  padding: 40px;
  width: 80%;
  margin: 0 auto;
  background: white;
}
.information table {
  margin-top: 20px;
  width: 100%;
}
.information .title {
  font-size: 1.5em;
  margin-bottom: 5px;
}
.information .buttons {
  margin-top: 60px;
}
.information .buttons button{
  margin: 0 auto;
  width: 240px;
  margin-bottom: 10px;
  display: block;
}
#data_results{
  margin: 30px;
}
</style>
