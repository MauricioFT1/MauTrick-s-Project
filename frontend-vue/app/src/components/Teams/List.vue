<template>
<v-parallax src="../../img/back.jpg" height="1900">
  <v-container fluid grid-list-xl>
    <h1 class="Titulo" align="center">Times</h1>
    <v-layout wrap justify-space-around>
      <v-flex v-for="team in teams" v-bind:key="team.id">
        <v-hover v-slot:default="{ hover }">
          <v-card
            :elevation="hover ? 12 : 2"
            class="mx-auto"
            min-width="380"
            max-width="380"
            outlined
          >
            <v-list-item three-line>
              <v-list-item-content>
                
                <v-list-item-title class="headline mb-1">{{team.name}}</v-list-item-title>
                <v-list-item-subtitle>{{team.stadium}}</v-list-item-subtitle>
                <br />
                <p>{{team.foundation}}</p>
                <br>
                <br>
                <button v-on:click="getCoach(team.coach)"> Técnico: <div v-if="coachs.id == team.coach">{{coachs.name}}</div></button>
              </v-list-item-content>
            </v-list-item>

            <v-card-actions>
              <v-btn :to="'/editionc'">Campeonatos</v-btn>
              <v-spacer></v-spacer>
              <v-btn class="ma-2" text icon color="red lighten-2">
                <v-icon class="delete" @click="deleteTeam(team)"></v-icon>
              </v-btn>

              <v-btn class="ma-2" text icon color="green">
                <v-icon class="edit" @click="editTeam(team)"></v-icon>
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-hover>
      </v-flex>
    </v-layout>
  </v-container>
</v-parallax>
</template>


<script>
import axios from "axios";
import router from "@/router/";

export default {
  name: "ListTeams",
  data() {
    return {
      coachs: [],
      teams: []
    };
  },
  created() {
    this.all();
    this.getCoach();
  },
  methods: {
    all() {
      axios
        .request({
          baseURL: "http://127.0.0.1:8000/",
          method: "get",
          url: "/api/teams/"
        })
        .then(response => {
          this.teams = response.data;
          console.log(response);
        });
    },
    deleteTeam(team) {
      if (confirm("Excluir " + team.name)) {
        axios
          .delete(`http://127.0.0.1:8000/api/teams/${team.id}`, {
            headers: {
              Authorization: `Token ${this.$session.get("token")}`
            }
          })
          .then(response => {
            this.all();
            console.log(response);
          });
      }
    },
    getCoach(coach) {
      axios
        .request({
          baseURL: "http://127.0.0.1:8000",
          method: "get",
          url: `/api/peoples/get/${coach}`
        })
        .then(response => {
          this.coachs = response.data;
          console.log(response);
        });
    },
    editTeam(team) {
      router.push(`/teams/edit/${team.id}`);
    }
  }
};
</script>