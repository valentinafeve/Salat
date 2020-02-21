<template id="login">
  <div class="login">
    <div class="dimmer" :class="{visible : loading}">
      <img src="https://gifimage.net/wp-content/uploads/2017/08/loading-gif-transparent-4.gif" alt="" style="height: 48px;">
    </div>
    <div class="rounded overflow-hidden shadow-lg items-center card">
        <div class="title">
          Ingresa tus credenciales y consulta tus estados financieros.
        </div>
        <hr id="hr1"><hr id="hr2">
        <div class="w-full max-w-sm">
          <div class="md:items-center mb-6">
            <div class="flex items-center border-b border-b-2 border-gray-400 py-2">
              <input id="username_input" placeholder="Usuario" class="appearance-none bg-transparent border-none w-full text-gray-700 mr-3 py-1 px-2 leading-tight focus:outline-none" style="display:block;" type="text" v-model="username">
            </div>
            <div class="flex items-center border-b border-b-2 border-gray-400 py-2">
              <input id="username_input" placeholder="Contraseña" class="appearance-none bg-transparent border-none w-full text-gray-700 mr-3 py-1 px-2 leading-tight focus:outline-none" style="display:block;" type="password" v-model="password">
            </div>
            <div :class="{message: message}">
              {{ message }}
            </div>
            <button @click="login" class="bg-red-600 hover:bg-red-700 text-white font-bold py-2 px-4 rounded">
              Login
            </button>
          </div>
        </div>
      </div>
  </div>
</template>
<script type="text/javascript">
import axios from 'axios';

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
  // these HTTP methods do not require CSRF protection
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

export default {
  name: 'Login',
  data(){
    return {
      username:'',
      password:'',

      message: '',
      loading: false,
    }
  },
  methods:{
    login(){
      if (this.username.length > 2 && this.password.length > 2){

        var csrftoken = getCookie('csrftoken');

        		$.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });

        const options = {
          method: 'POST',
          headers: {
            "X-CSRFToken": getCookie("csrftoken"),
            "Cookie": 'csrftoken='+getCookie("csrftoken"),
          },
          data: {
            'username': this.username,
            'csrftoken': csrftoken,
          },
          xsrfHeaderName: 'X-CSRFToken',
          url,
        };
        axios(options);

        // Is an administrator
        if(authenticated == 1){
          this.$router.push('/loader')
        }
        // Is a normal user
        if(authenticated == 2){
          this.$router.push('/information');
        }
        // Wan't authenticated
        if(authenticated == -1){
          this.message = 'El usuario o la contraseña ingresada no son correctos.'
          this.username = '';
          this.password = '';
        }
      }
      else{
        this.message = 'Por favor escriba su usuario y contraseña.';
        return;
      }
    }
  }
}
</script>
<style media="screen">
.login .card {
  padding: 50px;
  min-width: 150px;
  width: 40%;
  background: white;
  margin: 0 auto;
}

.login .message {
  margin-top: 20px;
  padding-top: 10px;
  padding: 12px;
  background: #ededdd;
  border-radius: 10px;
  color: #454545;
}

.login .title {
  font-size: 1.5em;
  margin-bottom: 40px;
  text-align: left;
}

.login input{
  width: 90%;
  font-size: 1.2em;
  margin-top:20px;
  position: relative;
}

.login button {
  font-size: 1.2em;
  margin-top:40px;
  width: 60%;
}

#hr1{
  width: 20%;
  display:inline-block;
  border-top: 2px solid #E53E3E;
}

#hr2{
  display:inline-block;
  width: 10%;
  border-top: 2px solid #9966ff;
}

.dimmer{
  position: absolute;
  top: 0;
  height: 100%;
  background: #21212180;
  width: 100%;
  z-index: 4;
  display: none;
}

.dimmer.visible{
  display: block;
}

.dimmer img{
  top: 50%;
  right: 50%;
  position: absolute;
}

</style>
