<template>
  <v-app id="booksandbooks">
    <v-btn
      v-scroll="onScroll"
      v-show="fab"
      fab
      dark
      fixed
      bottom
      right
      color="primary"
      @click="toTop"
      >
        <v-icon>keyboard_arrow_up</v-icon>
      </v-btn>
      <ToolBar @toggle-drawer="$refs.drawer.drawer = !$refs.drawer.drawer"></ToolBar>
    
    <v-content>
      <router-view></router-view>
    </v-content>
    <Footer @toggle-drawer="$refs.drawer.drawer = !$refs.drawer.drawer"></Footer>
  </v-app>
</template>

<script>
import ToolBar from "@/components/Base/ToolBar"
import Footer from"@/components/Base/Footer"

export default {
  name: "App",
  components: {
    ToolBar: ToolBar,
    Footer: Footer
  },
  data: () => ({
    fab: false
  }),
  methods: {
    onScroll(e) {
      if (typeof window === "undefined") return;
      const top = window.pageYOffset || e.target.scrollTop || 0;
      this.fab = top > 20;
    },
    toTop() {
      this.$vuetify.goTo(0);
    }
  }
};
</script>

