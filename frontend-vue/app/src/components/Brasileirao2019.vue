<template>
  <div>
    <v-parallax src="../img/back.jpg" height="1300">
      <div class="Titulo">Brasileirão 2019</div>
      <br>
      <div id="app" class="mx-12">
        <v-app id="inspire">
          <br>
          <v-btn href="http://127.0.0.1:8000/api/brasileiraomontar/" target="_blank">Atualizar dados</v-btn>
          <br>
          
        <!-- Inicio Tabela -->
          <table>
            <tr>
              <th>Posição</th>
              <th>Pontos</th>
              <th>Jogos</th>
              <th>Vitórias</th>
              <th>Empates</th>
              <th>Derrotas</th>
            </tr>
          </table>
          <table v-for="(team,i) in items" v-bind:key="team.score">
            <tr>
              <th>{{i+1}}. {{team.name}}</th>
              <th>{{team.score}}</th>
              <th>{{team.games}}</th>
              <th>{{team.wins}}</th>
              <th>{{team.draws}}</th>
              <th>{{team.loses}}</th>
            </tr>
          </table>
        <!-- Final Tabela -->

          <div class="noticiasdeTerra">
            Tabela de:
            <a
              href="https://www.terra.com.br/esportes/futebol/brasileiro-serie-a/tabela/"
              target="_blank"
            >Terra</a>
          </div>
        </v-app>
      </div>
    </v-parallax>
  </div>
</template>


<script>
import axios from "axios";
import router from "@/router/";

export default {
  name: "Brasileirao2019",
  data() {
    return {
      items: [],
      headers: [
        {
          text: "Posição ",
          align: "left",
          sortable: false,
          value: "name"
        },
        { text: "Pontos", value: "score" },
        { text: "Jogos", value: "games" },
        { text: "Vitórias", value: "wins" },
        { text: "Empates", value: "draws" },
        { text: "Derotas", value: "loses" }
      ],
      desserts: []
    };
  },
  created() {
    this.all();
  },
  methods: {
    all() {
      axios
        .request({
          baseURL: "http://127.0.0.1:8000/",
          method: "get",
          url: "/api/brasileiraomontar/"
        })
        .then(response => {
          this.items = response.data;
          console.log(response);
        });
    }
  }
};
</script>