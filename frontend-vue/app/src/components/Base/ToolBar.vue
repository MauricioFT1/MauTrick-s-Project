<template>
  <div>
    <v-toolbar>
      <v-app-bar-nav-icon :to="'/'">
        <img
          src="https://imagepng.org/wp-content/uploads/2017/10/bola.png"
          width="40px"
          alt
          title="Futebol"
        />
      </v-app-bar-nav-icon>

      <v-spacer></v-spacer>

      <v-divider vertical></v-divider>
      <v-toolbar-items v-for="item in items" :key="item.title">
        <v-btn text :to="item.endpoint">{{item.title}}</v-btn>

        <v-divider vertical></v-divider>
      </v-toolbar-items>

      <div class="text-center">
        <v-menu offset-y>
          <template v-slot:activator="{ on }">
            <v-btn text dark v-on="on">Brasileirão</v-btn>
          </template>
          <v-list>
            <v-list-item  v-for="drop in drops" :key="drop.title">
              <v-btn text :to="drop.endpoint">{{drop.title}}</v-btn>
                      
            </v-list-item>
          </v-list>
        </v-menu>
      </div>
    <v-divider vertical></v-divider>
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
        // { title: "Home ", endpoint: "/" },
        // { title: "My Account", endpoint: "/user" },
        // { title: "Users", endpoint: "/users" },
        { title: "Campeonatos", endpoint: "/editionc" },
        { title: "Times", endpoint: "/teams" },
        { title: "Origem", endpoint: "/origem" },
        { title: "Copas", endpoint: "/copa" },
        // { title: "Brasileirão2018", endpoint: "/brasileirao2018" },
        // { title: "Brasileirão2008", endpoint: "/brasileirao2008" },
        { title: "Regulamento", endpoint: "/regulamento" },
        // { title: "Teste", endpoint: "/teste" }
      ],
      drops: [
        { title: "Brasileirão2019", endpoint: "/brasileirao2019" },
        { title: "Brasileirão2018", endpoint: "/brasileirao2018" },
        { title: "Brasileirão2008", endpoint: "/brasileirao2008" },
      ],
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

