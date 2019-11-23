<style>
.fundo{
  background-image: url('../img/brasil.jpg');
  height: 600px;
}

.dimeimg{
  margin-left: 40px;
}
</style>

<template>
  <div class="fundo">
  <v-container class="fill-height" fluid>
      
    <v-spacer></v-spacer>
    <v-row align="center" justify="center">
      <v-col cols="12" sm="8" md="5">
        <AlertMsg v-if="errorShow" >
          Login or password wrong
        </AlertMsg>
        
        <v-card class="elevation-20">
          <LoginToolbar />
          <LoginFields ref="formFields"
            @fillCredentials="fillCredentials"
          />          
          <LoginButtons @login="login"/>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
  </div>
</template>

<script>
import router from "../router";
import axios from "axios";

import AlertMsg from '@/components/AlertMsg.vue'
import LoginToolbar from '@/components/Login/LoginToolbar.vue'
import LoginFields from '@/components/Login/LoginFields.vue' 
import LoginButtons from '@/components/Login/LoginButtons.vue'

 
export default {  
  props: {
    source: String,
  }, 
  components: {AlertMsg, LoginToolbar, LoginFields, LoginButtons},
  data: () => ({
    credentials: {},
    errorShow: false,
    drawer: null,    
  }),
  methods: {
    fillCredentials(credentials) {
      this.credentials = credentials
    },
    login() {
      if (!this.$refs.formFields.$invalid) {
        axios
          .post("http://localhost:8000/auth/token/login", this.credentials)
          .then(res => {
            this.$session.start();
            this.$session.set("token", res.data.auth_token);
            router.push("/");
          })
          .catch(e => {
            this.errorShow = true
          });
      }
    }
  }
};
</script>