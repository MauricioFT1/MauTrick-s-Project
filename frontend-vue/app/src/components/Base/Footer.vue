<template>
  <v-footer dark padless>
    <v-card flat tile class="lighten-1 white--text text-center">
      <v-card-text>
        <v-btn
          v-for="(icon, i) in icons" 
          :key="i"
          class="mx-4 white--text"
          icon
          :href="icon.link"
          :title="icon.title"
        >
          <v-icon size="24px">{{ icon.icone }}</v-icon>
        </v-btn>
      </v-card-text>

      <v-card-text class="white--text pt-0">
        Esse site foi desenvolvido pelos alunos Mauricio de Freitas Tebechrani e Patrick Vianna Rieger da graduação de Bacharelado
        em Sistemas de informações e tem como principal função o quesito educacional e experimental,
        desenvolvido unicamente e exclusivamente para a aula de Desenvolvimento WEB II, utilizando
        vue com o auxilio do framework boostrap para desenvolver o frontend, 
        juntamente com Django para desenvolvimento do backend.
      </v-card-text>

      <v-divider></v-divider>

      <v-card-text class="white--text">
        {{ new Date().getFullYear() }} —
        <strong>Mautrick's Corp</strong>
      </v-card-text>
    </v-card>
  </v-footer>
</template>

<script>
export default {
  data() {
    return {
      icons: [
        { title: "GitHub", icone: "mdi-github-circle", link: "https://github.com/MauricioFT1/django-vue" },
        { title: "IFC", icone: "mdi-city", link: "http://ifc.edu.br/" },
        { title: "Prof. Eduardo", icone: "mdi-account", link: "https://sites.google.com/view/eduardodasilva" },
        { title: "Materia Dev Web II", icone: "mdi-book-open", link: "https://sites.google.com/view/eduardodasilva/ensino/desenvolvimento-web-ii" },
      ]
    };
  }
};
</script>