<template>
  <v-container>
      <div v-for="edition in editions" v-bind:key="edition.id">
        <p>{{edition.championship}}</p>
        <v-btn class="ma-2" text icon color="red lighten-2">
          <v-icon class="delete" @click="findTeam(1)"></v-icon>
        </v-btn>
        <v-text>{{team}}</v-text>
        <v-btn class="ma-2" text icon color="green">
          <v-icon class="edit" @click="editChampionship(championship)"></v-icon>
        </v-btn>
        <v-divider></v-divider>
      </div>
      <CreateChampionships @updateChampionships="all"></CreateChampionships>
  </v-container>
</template>


<script>
import axios from "axios";
import router from "@/router/"

export default {
  name: "EditionC",
  data() {
    return {
      editions: [],
      team: [],
    };
  },
  created() {
    this.all();
    this.findTeam();
  },
  methods: {
    all() {
      axios
        .request({
          baseURL: "http://127.0.0.1:8000/",
          method: "get",
          url: "/api/editions/"
        })
        .then(response => {
          this.editions = response.data
          console.log(response)
        });
    },
    findTeam(teamid) {
      axios
        .request({
          baseURL: "http://127.0.0.1:8000/",
          method: "get",
          url: `/api/teams/get/${teamid}/`,
        })
        .then(response => {
          this.team = response.data
          console.log(response)
        });
    }
  }
};
</script>