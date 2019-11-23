<!--<template>
  <v-navigation-drawer app fixed
    class="app---drawer" 
    v-model="drawer"
    :mini-variant.sync="mini"
    :clipped="$vuetify.breakpoint.lgAndUp"
  >
    <v-list-item>
      <v-list-item-avatar>
        <v-img src="https://randomuser.me/api/portraits/men/85.jpg"></v-img>
      </v-list-item-avatar>

      <v-list-item-title>{{user.name}}</v-list-item-title>

      <v-btn icon @click.stop="mini = !mini">
        <v-icon>mdi-chevron-left</v-icon>
      </v-btn>
    </v-list-item>
    <v-divider></v-divider> 

    <v-list dense> 
      <v-list-item :to="item.endpoint" v-for="item in items" :key="item.title" link>
        <v-list-item-content>
          <v-list-item-title >{{ item.title }}</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <template v-if="logged">
        
        <v-list-item :to="item.endpoint" v-for="item in items_logged" :key="item.title" link>
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title >{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </template>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
export default {
  name: "SideMenu",
  data() {
    return {
      user: {},
      items: [
        { title: "Home", icon: "mdi-home-city", endpoint: '/' },
        { title: "My Account", icon: "mdi-account", endpoint: '/user' },
        { title: "Users", icon: "mdi-account-group", endpoint: '/users' },
        { title: "Books", icon: "mdi-library-books", endpoint: '/books'},
        { title: "Experiments", icon: "mdi-chart-pie", endpoint: '/experiments'}

      ],
    }
  }
}
</script> -->