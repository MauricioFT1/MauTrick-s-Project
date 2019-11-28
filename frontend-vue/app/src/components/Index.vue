<style>
.texto {
  font-family: fantasy;
}
.fundo2 {
  height: 2000px;
}
.bolakick {
  background-color: #ffffff;
}
.triangulo {
  width: 0;
  height: 0;
  border-left: 1600px solid transparent;
  border-top: 150px solid white;
}
.fraseefeito {
  height: 600px;
  background-image: url("https://brunorabello.com.br/wp-content/uploads/2015/10/steve-jobs.jpg");
  font-size: 16px;
  background-size: 1300px;
  text-align: center;
}
</style>
<template>
  <div class="fundo2">
    <!-- <section class="container"> -->
    <section>
      <br />
      <br />
      <br />
      <h3 align="center">
        <v-list-item three-line>
          <v-list-item-content>
            <div class="mb-6 texto">
              <h1>Futebol</h1>
            </div>
            <p>
              O objeto usado é uma bola e o objetivo principal do esporte é a marcação de pontos,
              que consiste em fazer a bola atravessar a trave adversária, encontrada na extremidade do campo.
              A instituição internacional responsável pela organização e fiscalização de eventos,
              bem como a regulação e manutenção das regras do esporte é a
              <a
                href="https://www.fifa.com/"
                target="_blank"
              >FIFA</a>, Federação Internacional de Futebol.
            </p>
          </v-list-item-content>
        </v-list-item>
      </h3>

      <v-spacer></v-spacer>
      <v-row align="center" justify="center">
        <v-container fluid>
          <div class="bolakick">
            <v-row justify="space-around">
              <v-col cols="7">
                <v-carousel cycle height="500" hide-delimiter-background>
                  <v-carousel-item v-for="(item,i) in items" :key="i" :src="item.src">
                    <v-row class="fill-height" align="center" justify="center">
                      <div class="display-2">{{ slide }}</div>
                    </v-row>
                  </v-carousel-item>
                </v-carousel>
              </v-col>
              <v-col cols="5">
                <img src="../img/bolakick.gif" alt />
              </v-col>
            </v-row>
          </div>
          <div class="triangulo"></div>
        </v-container>
      </v-row>

      <div align="center" class="fraseefeito"></div>


      <!-- NOTICIAS COMEÇA AQUI -->
      <h1 align="center">NEWS FROM: <a href="https://globoesporte.globo.com/futebol/">globoesporte</a></h1>
      <br>
    <v-layout wrap justify-space-around>
          <v-flex v-for="noticia in news" v-bind:key="noticia.id" >
          <v-card
      class="mx-auto"
      min-width="380"
      max-width="380"
      outlined
    >
      <v-list-item three-line>
        <v-list-item-content>
          <div class="overline mb-4">LINK: {{noticia.link}}</div>
          <v-list-item-title class="headline mb-1">TITULO: {{noticia.title}}</v-list-item-title>
          <v-list-item-subtitle>RESUMO: {{noticia.summary}}</v-list-item-subtitle>
          <v-spacer></v-spacer> 
          <v-list-item-subtitle>IMAGEM: {{noticia.image}}</v-list-item-subtitle>
          <br>
          <p></p>
        </v-list-item-content>
        <v-list-item-avatar
          tile
          size="80"
          color="grey"
        > 
        </v-list-item-avatar>
      </v-list-item>
  
      <v-card-actions>
        <v-spacer></v-spacer>
          <v-btn>MUDA ISSO KKK</v-btn>
          <v-spacer></v-spacer>
      </v-card-actions>
    </v-card>
       </v-flex>
      </v-layout>
<!-- NOTICIAS ACABA AQUI -->


    </section>
  </div>
</template>


<script>
import axios from "axios";
import router from "@/router/"

export default {
  name: "Index",
  data() {
    return {
      news: [],
      items: [
        {
          src:
            "http://www.photobackgroundhd.com/wp-content/uploads/2018/10/lionel-messi-wallpaper-download-high-quality.jpg"
        },
        {
          src: "https://wallpaperaccess.com/full/493700.jpg"
        },
        {
          src: "https://wallpaperaccess.com/full/493700.jpg"
        },
        {
          src: "https://wallpapercave.com/wp/wp1956988.jpg"
        }
      ]
    };
  },
  mounted() {
    this.checkAuthenticated();
  }
  ,
  created() {
    this.all();
  },
  methods: {
    all() {
      axios
        .request({
          baseURL: "http://127.0.0.1:8000/",
          method: "get",
          url: "/api/noticiasmontar/"
        })
        .then(response => {
          this.news = response.data
          console.log(response)
        });
    },
    checkAuthenticated() {
      this.$session.start();
      if (!this.$session.has("token")) {
        router.push("/login");
      } else {
        this.authenticated = true;
      }
    }
  }}
</script>