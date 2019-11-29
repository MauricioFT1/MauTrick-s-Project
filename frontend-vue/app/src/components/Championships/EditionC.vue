<template>
  <v-container>
      <div v-for="editionC in editionsChamp" v-bind:key="editionC.id">
        {{editionC.edition}}
        <v-btn class="ma-2" text icon color="green">
          <v-icon class="mdi-information-outline" @click="findEdition(editionC.edition), findChampionship(editionC.championship)">mdi-information-outline</v-icon>
        </v-btn>
        <p>Campeonato: {{champ.name}}</p>
        <p>Descrição: {{champ.description}}</p>
        <p>Data de começo: {{edicao.date}}</p>
        <p>Número da edição: {{edicao.number}}</p>
        <p>Participantes: </p>
        <v-text v-for="part in edicao.participants" v-bind:key="part.id">
        <li>Time {{part}}
          <v-dialog
        v-model="dialog"
        width="500"
      >
          <template v-slot:activator="{ on }">
          <v-btn class="ma-2" text v-on="on" @click="findTeam(part)">
          <v-icon class="mdi-information-outline">mdi-information-outline</v-icon>
            INFO
          </v-btn>
          </template>
         <v-card>
          <v-card-title
            primary-title
          >
            {{team.name}}
          </v-card-title>
          <v-divider></v-divider>
          <v-card-text>
            <br>
           <p>Estádio: {{team.stadium}}</p>
           <p>Fundação: {{team.foundation}}</p>
          </v-card-text>
  
          <v-divider></v-divider>
  
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
              color="primary"
              text
              @click="dialog = false"
            >
              Fechar
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>

        </li>
        </v-text>

        
        <v-divider></v-divider>
      </div>
  </v-container>
</template>


<script>
import axios from "axios";
import router from "@/router/"

export default {
  name: "EditionC",
  data() {
    return {
      dialog: false,
      editionsChamp: [],
      team: [],
      edicao: [],
      champ: [],
    };
  },
  created() {
    this.all();
    // this.findTeam();
    // this.findEdition(editionsChamp.edition);
  },
  methods: {
    all() {
      axios
        .request({
          baseURL: "http://127.0.0.1:8000/",
          method: "get",
          url: "/api/editionschamp/"
        })
        .then(response => {
          this.editionsChamp = response.data
          console.log(response)
        });
    },
    findTeam(teamid) {
      axios
        .request({
          baseURL: "http://127.0.0.1:8000",
          method: "get",
          url: `/api/teams/get/${teamid}/`,
        })
        .then(response => {
          this.team = response.data
          console.log(response)
        });
    }
  ,
  findChampionship(champid) {
      axios
        .request({
          baseURL: "http://127.0.0.1:8000",
          method: "get",
          url: `/api/championships/get/${champid}/`,
        })
        .then(response => {
          this.champ = response.data
          console.log(response)
        });
    }
  ,
  findEdition(editionid) {
      axios
        .request({
          baseURL: "http://127.0.0.1:8000",
          method: "get",
          url: `/api/editions/get/${editionid}/`,
        })
        .then(response => {
          this.edicao = response.data
          console.log(response)
        });
    }}
};
</script>