<template>
  <div>
    <v-toolbar>
      <v-app-bar-nav-icon>
        <img src="/src/img/bola.png" width="40px" alt title="Futebol" />
      </v-app-bar-nav-icon>
      <v-toolbar-title></v-toolbar-title>

      <v-spacer></v-spacer>

      <v-divider vertical></v-divider>
      <v-toolbar-items v-for="item in items" :key="item.title">
        <v-btn text :to="item.endpoint">{{item.title}}</v-btn>
        <v-divider vertical></v-divider>
      </v-toolbar-items>

      <v-spacer></v-spacer>

      <v-btn icon to="/logout" v-if="authenticated">
        <v-icon>mdi-export</v-icon>
      </v-btn>

    </v-toolbar>
  </div>
  
</template>



<script>
export default {
  name: "toolbar",
  data() {
    return {
      authenticated: false,
      user: {},
      items: [
        { title: "Home ", endpoint: "/" },
        { title: "My Account", endpoint: "/user" },
        { title: "Users", endpoint: "/users" },
        { title: "Books", endpoint: "/books" },
        { title: "Experiments", endpoint: "/experiments" },
        { title: "Origem", endpoint: "/origem" },
        { title: "Copas", endpoint: "/copa" },
        { title: "Brasileirão2018", endpoint: "/brasileirao2018" },
        { title: "Brasileirão2008", endpoint: "/brasileirao2008" },
        { title: "Regulamento", endpoint: "/regulamento" },
        { title: "Teste", endpoint: "/teste" }
      ]
    };
  },
  mounted() {
    this.checkAuthenticated();
  },
  methods: {
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

