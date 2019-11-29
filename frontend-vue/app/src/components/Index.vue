<style>
.texto {
  font-family: fantasy;
}
.fundo2 {
  height: 2700px;
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
  height: 400px;
  width: 1440px;
  background-image: url("https://image.freepik.com/free-photo/chalkboard-blackboard-dark-wallpaper-background_28629-1125.jpg");
  text-align: center;
  background-size: 1440px;
  font-family: "FreeMono", monospace;
  font-weight: bold;
  /* https://www.belasmensagens.com.br/wp-content/uploads/1970/01/fazer-mil-gols-400x300.jpg */
}

.fraseprincipal {
  font-size: 30px;
}

.testenoticias {
  margin-left: 100px;
}

.noticiasde {
  margin-left: 1120px;
}

.noticiasdeTerra {
  margin-left: 1095px;
}
</style>
<template>
  <div class="fundo2">
    <!-- <section class="container"> -->
    <section>
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
                <v-carousel :show-arrows="false" cycle height="500" hide-delimiters>
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

      <!-- NOTICIAS COMEÇA AQUI -->

      <h1 align="center">
        Notícias de ultima hora!
        <br />
        <v-btn
          title="Atualizar Noticias"
          href="http://127.0.0.1:8000/api/noticiasmontar/"
          target="_blank"
        >
          <v-icon icon>mdi-refresh</v-icon>
        </v-btn>
      </h1>
      <br />

      <div class="testenoticias" v-for="noticia in news" v-bind:key="noticia.id">
        <br />
        <v-hover v-slot:default="{ hover }">
          <v-card
            :elevation="hover ? 16 : 1"
            min-width="1200"
            max-width="1200"
            height="300"
            outlined
          >
            <div>
              <v-list-item three-line>
                <v-list-item-content>
                  <!-- <div class="overline mb-4">LINK: {{noticia.link}}</div> -->
                  <!-- <div class="overline mb-4">
                  <a :href="noticia.link">NOTICIA</a>
                  </div>-->
                  <v-row align="center" justify="center">
                    <v-row justify="space-around">
                      <v-col cols="4">
                        <a :href="noticia.link" target="_blank">
                          <img :src="noticia.image" width="350px" height="240px" />
                        </a>
                      </v-col>
                      <v-col cols="8">
                        <v-list-item-subtitle class="headline mb-1">
                          <a :href="noticia.link" target="_blank">{{noticia.title}}</a>
                        </v-list-item-subtitle>
                        <br />
                        <br />
                        <v-list-item-subtitle>
                          <h4>{{noticia.summary}}</h4>
                        </v-list-item-subtitle>
                      </v-col>
                    </v-row>
                  </v-row>
                </v-list-item-content>
              </v-list-item>
            </div>
          </v-card>
        </v-hover>
      </div>

      <div class="noticiasde">
        Noticias de:
        <a href="https://globoesporte.globo.com/futebol/" target="_blank">globoesporte</a>
      </div>

      <!-- NOTICIAS ACABA AQUI -->

      <br />
      <br />
      <br />
      <br />

      <!-- Frase de efeito -->
      <div class="fraseefeito">
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <div
          class="fraseprincipal"
        >"O dificil, o extraordinario, não é fazer mil gols como Pelé. É fazer um gol como Pelé."</div>
        <br />- Carlos Drummond de Andrade -
      </div>
      <!-- FIm frase de efeito -->

      <br />
      <br />

      <!-- Dropdown -->
      <v-row justify="center">
        <v-expansion-panels>
          <v-expansion-panel style="max-width:400px;">
            <v-expansion-panel-header>Links do curso</v-expansion-panel-header>
            <v-expansion-panel-content>
              Endereço: Rodovia BR 280 - km 27
              <br />Cx. Postal 21 - CEP 89245-000
              <br />Araquari - SC - Fone (47)
              3803-7200
              <br />

              <a href="https://araquari.ifc.edu.br/" target="_blank">
                Instituto Federal Catarinense campus
                Araquari
              </a>
              <br />Site do Professor:
              <a
                href="https://sites.google.com/view/eduardodasilva"
                target="_blank"
              >Eduardo da Silva</a>
              <br />Site da Materia:
              <a
                href="https://sites.google.com/view/eduardodasilva/ensino/desenvolvimento-web-ii"
                target="_blank"
              >Desenvolvimento Web II</a>
            </v-expansion-panel-content>
          </v-expansion-panel>
        </v-expansion-panels>
      </v-row>

        <br />
        <br />
        <br />
        <br />
        <br />

      <!-- Fim dropdown -->
    </section>
  </div>
</template>


<script>
import axios from "axios";
import router from "@/router/";

export default {
  name: "Index",
  data() {
    return {
      news: [],
      items: [
        {
          src:
            "https://image.freepik.com/fotos-gratis/jogador-de-futebol-forte-com-bola-de-futebol-no-fundo-branco-isolado_1368-17780.jpg"
        },
        {
          src:
            "https://image.freepik.com/fotos-gratis/homem-de-jogador-de-futebol-americano-afro-sobre-fundo-branco-isolado_1368-42682.jpg"
        },
        {
          src:
            "https://media.istockphoto.com/photos/professional-african-football-soccer-player-isolated-on-white-picture-id1127748759"
        },
        {
          src:
            "https://image.freepik.com/fotos-gratis/homem-de-jogador-de-futebol-americano-afro-sobre-fundo-branco-isolado_1368-42678.jpg"
        }
      ]
    };
  },
  mounted() {
    this.checkAuthenticated();
  },
  created() {
    this.all();
  },
  methods: {
    all() {
      axios
        .request({
          baseURL: "http://127.0.0.1:8000",
          method: "get",
          url: "/api/noticiasmontar/"
        })
        .then(response => {
          this.news = response.data;
          console.log(response);
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
  }
};
</script>