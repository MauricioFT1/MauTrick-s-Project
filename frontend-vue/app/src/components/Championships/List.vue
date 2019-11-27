<template>
  <v-container>
      <div v-for="championship in championships" v-bind:key="championship.id">
        <p>{{championship.name}}</p>
        <p>{{championship.description}}</p>
        <p>{{championship.created}}</p>
        <p>{{championship.role}}</p>
        
        <v-btn class="ma-2" text icon color="red lighten-2">
          <v-icon class="delete" @click="deleteChampionship(championship)"></v-icon>
        </v-btn>
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
import CreateChampionships from "./Create";

export default {
  name: "ListChampionships",
  data() {
    return {
      championships: [],
    };
  },
  components: {
    CreateChampionships: CreateChampionships,
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
          url: "/api/championships/"
        })
        .then(response => {
          this.championships = response.data
          console.log(response)
        });
    },
    deleteChampionship(championship) {
      if (confirm("Excluir " + championship.name)) {
        axios
          .delete(`http://127.0.0.1:8000/api/championships/${championship.id}`, {
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
    editChampionship(championship) {
      router.push(`/championships/edit/${championship.id}`)
    }
  }
};
</script>