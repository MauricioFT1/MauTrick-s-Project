<template>
  <v-row justify="center">
    <v-dialog v-model="dialog" persistent max-width="600px">
      <template v-slot:activator="{ on }">
        <v-card-text>
          <v-fab-transition>
            <v-btn primary v-on="on" dark relative fixed bottom right fab>
              <v-icon>mdi-plus</v-icon>
            </v-btn>
          </v-fab-transition>
        </v-card-text>
      </template>

      <v-card>
        <v-card-title>
          <span class="headline">Adicionar Livros</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12">
                <v-text-field v-model="book.name" label="Título*" hint="Título do livro" required></v-text-field>
              </v-col>
              <v-row class="form-group" v-for="(input,k) in bookauthors" :key="k">
                
              <v-col cols="7">
                <v-select
                  :items = "authors"
                  item-value = "id"
                  item-text = "first_name"
                  label = "Autores"
                  attach
                  single-line
                  v-model = "input.author"
                >
                </v-select>
              </v-col>
              <v-col cols="4">
                <v-select
                  :items = "roles"
                  item-value = "id"
                  item-text = "role"
                  label = "Role"
                  attach
                  single-line
                  v-model="input.role"
                >
                </v-select>
              </v-col>
              <v-col cols="1">
                    <v-icon 
                      @click="addauthor(k)"
                    >mdi-plus</v-icon>
                    <v-icon 
                      @click="removeauthor(k)"
                      v-show="k || ( !k && bookauthors.length > 1)">
                       mdi-minus
                    </v-icon>
              </v-col>
              </v-row>
              <v-col cols="12">
                <v-text-field v-model="book.description" label="Descrição*" type="text" required></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-select
                  :items = "genres"
                  item-value = "id"
                  item-text = "name"
                  label = "Gênero"
                  attach
                  v-model = "book.genre"
                >
                </v-select>
              </v-col>
            </v-row>
          </v-container>
          <small>*informações obrigatórias</small>
        </v-card-text>
        <v-card-actions>
          <div class="flex-grow-1"></div>
          <v-btn color="blue darken-1" text @click="dialog = false">Fechar</v-btn>
          <v-btn color="blue darken-1" text @click="add()">Salvar</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>
<script>

import axios from "axios"
require('../../assets/site.css');
export default {
  name: "CreateBook",
  data() {
    return {
      dialog: false,
      genres: [],
      authors: [],
      book: {},
      bookauthors: [{
        author: "",
        role: 0
      }],
      roles: [
        {id: 0, role: "Writer"},
        {id: 1, role: "Translator"},
        {id: 2, role: "Illustrator"},
        {id: 3, role: "Editorss"}
      ]
    };
  },
  created() {
    this.getGenres()
    this.getAuthors()
  },
  methods: {
    addauthor(index) {
      this.bookauthors.push({ name: '', role: ''});
    },
    removeauthor(index) {
      this.bookauthors.splice(index, 1);
    },
    getGenres() {
      axios
      .request({
        baseURL: "http://localhost:8000",
        method: "get",
        url: "/api/genres/"
      })
      .then(response => {
        this.genres = response.data
        console.log(response)
      });
    },
    getRoles() {

    },
    getAuthors() {
      axios
      .request({
        baseURL: "http://localhost:8000",
        method: "get",
        url: "/api/authors/"
      })
      .then(response => {
        this.authors = response.data
        console.log(response)
      });
    },
    add() {
      this.book.authors = this.bookauthors
      axios
        .post("http://localhost:8000/api/books/add/",
          this.book, 
          {
            headers: {
              Authorization: `Token ${this.$session.get("token")}`
            }
          }
        )
        .then(response => {
          this.dialog = false
          this.$emit('updateBooks')
          this.log.console(response)
        });
    }
  }
};
</script>
