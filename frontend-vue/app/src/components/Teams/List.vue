<template>

  <v-container fluid grid-list-xl>
      <h1 align="center">TEAMS</h1>
      <v-layout wrap justify-space-around>
          <v-flex v-for="team in teams" v-bind:key="team.id">
          <v-card
      class="mx-auto"
      min-width="380"
      max-width="380"
      outlined
    >
      <v-list-item three-line>
        <v-list-item-content>
          <div class="overline mb-4">{{team.coach}}</div>
          <v-list-item-title class="headline mb-1">{{team.name}}</v-list-item-title>
          <v-list-item-subtitle>{{team.stadium}}</v-list-item-subtitle>
          <br>
          <p>{{team.foundation}}</p>
        </v-list-item-content>
        <!-- <v-list-item-avatar
          tile
          size="80"
          color="grey"
        ></v-list-item-avatar> -->
      </v-list-item>
  
      <v-card-actions>
          <v-btn>Campeonatos</v-btn>
          <v-spacer></v-spacer>
        <v-btn class="ma-2" text icon color="red lighten-2">
          <v-icon class="delete" @click="deleteTeam(team)"></v-icon>
        </v-btn>
        
        <!-- <v-divider></v-divider>  -->
        <v-btn class="ma-2" text icon color="green">
          <v-icon class="edit" @click="editTeam(team)"></v-icon>
        </v-btn>
      </v-card-actions>
    </v-card>
    <!-- <div v-for="team in teams" v-bind:key="team.id"> 
        <p>{{team.name}}</p>
        <p>{{team.stadium}}</p>
        <p>{{team.coach}}</p>
        <p>{{team.foundation}}</p>
        
        <v-btn class="ma-2" text icon color="red lighten-2">
          <v-icon class="delete" @click="deleteTeam(team)"></v-icon>
        </v-btn>
        <v-btn class="ma-2" text icon color="green">
          <v-icon class="edit" @click="editTeam(team)"></v-icon>
        </v-btn>
        <v-divider></v-divider> 
       </div> -->
       </v-flex>
      </v-layout>
    </v-container>
</template>


<script>
import axios from "axios";
import router from "@/router/"

export default {
  name: "ListTeams",
  data() {
    return {
      teams: [],
    };
  }
  ,
  created() {
    this.all();
    this.getCoach()
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
          this.teams = response.data
          console.log(response)
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
            this.all()
            console.log(response)
          });
      }
    },
    getCoach(coach) {
      axios
      .request({
        baseURL: "http://localhost:8000",
        method: "get",
        url: "/api/peoples/`${coach.id}`"
      })
      .then(response => {
        this.authors = response.data
        console.log(response)
      });
    },
    editTeam(team) {
      router.push(`/teams/edit/${team.id}`)
    }
  }
};
</script>