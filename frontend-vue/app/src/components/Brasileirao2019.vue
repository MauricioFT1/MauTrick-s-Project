<style>
.Titulo {
  text-align: center;
  color: #777;
  font-size: 55px;
  font-family: arial;
  font-weight: bold;
  text-shadow: 0 1px 0 #cccccc, 0 2px 0 #c9c9c9, 0 3px 0 #bbbbbb,
    0 4px 0 #b9b9b9, 0 5px 0 #aaaaaa, 0 6px 1px rgba(0, 0, 0, 0.1),
    0 0 5px rgba(0, 0, 0, 0.1), 0 1px 3px rgba(0, 0, 0, 0.3),
    0 3px 5px rgba(0, 0, 0, 0.2), 0 5px 10px rgba(0, 0, 0, 0.25),
    0 10px 10px rgba(0, 0, 0, 0.2), 0 20px 20px rgba(0, 0, 0, 0.15);
}
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
}

td,
th {
  border-: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
  width: 10%;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
</style>

<template>
  <div>
    <v-parallax src="../img/back.jpg" height="1300">
      <div class="Titulo">Brasileirão 2019</div>
      <br />
      <div id="app" class="mx-12">
        <v-app id="inspire">
          <!-- <v-card> -->
          <br />

          <!-- <v-data-table v-for="team in items" v-bind:key="team.score"></v-data-table> -->
          <v-btn href="http://127.0.0.1:8000/api/brasileiraomontar/" target="_blank">Atualizar dados</v-btn>
          <br />
          <table>
            <tr>
              <th>Pocisão</th>
              <th>Pontos</th>
              <th>Jogos</th>
              <th>Vitórias</th>
              <th>Empates</th>
              <th>Derrotas</th>
            </tr>
          </table>
          <table v-for="team in items" v-bind:key="team.score">
            <tr>
              <th>{{team.name}}</th>
              <th>{{team.score}}</th>
              <th>{{team.games}}</th>
              <th>{{team.wins}}</th>
              <th>{{team.draws}}</th>
              <th>{{team.loses}}</th>
            </tr>
          </table>
          <!-- </v-card> -->
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
          text: "Pocisão ",
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