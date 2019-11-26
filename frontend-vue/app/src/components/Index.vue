<style>
.texto {
  font-family: fantasy;
}
.fundo2 {
  height: 2000px;
}
.bolakick {
  background-color: #ffffff;
}
.triangulo {
  width: 0;
  height: 0;
  border-left: 1600px solid transparent;
  border-top: 150px solid white;
}
</style>
<template>
 <div class="fundo2">
  <!-- <section class="container"> -->
  <section>
    <br />
    <br />
    <br />
    <h3 align="center">
          <v-list-item three-line>
            <v-list-item-content>
              <div class="mb-6 texto">
                <h1>Futebol</h1>
              </div>
              <p>
                O objeto usado é uma bola e o objetivo principal do esporte é a marcação de pontos,
                que consiste em fazer a bola atravessar a trave adversária, encontrada na extremidade do campo.
                A instituição internacional responsável pela organização e fiscalização de eventos,
                bem como a regulação e manutenção das regras do esporte é a
                <a
                  href="https://www.fifa.com/"
                  target="_blank"
                >FIFA</a>, Federação Internacional de Futebol.
              </p>
            </v-list-item-content>
          </v-list-item>
    </h3>

    <v-spacer></v-spacer>
      <v-row align="center" justify="center">
        <v-container fluid>
          <div class="bolakick">
            <v-row justify="space-around">
              <v-col cols="7">
                <v-carousel cycle height="500" hide-delimiter-background>
                  <v-carousel-item v-for="(item,i) in items" :key="i" :src="item.src">
                    <v-row class="fill-height" align="center" justify="center">
                      <div class="display-2">{{ slide }}</div>
                    </v-row>
                  </v-carousel-item>
                </v-carousel>
              </v-col>
              <v-col cols="4">
                <img src="../img/bolakick.gif" alt />
              </v-col>
            </v-row>
          </div>
          <div class="triangulo"></div>
        </v-container>
      </v-row>

  </section>
  </div>
</template>

<script>
import router from "../router";

export default {
  name: "Index",
  data() {
    return {
      items: [
        {
          src:
            "http://www.photobackgroundhd.com/wp-content/uploads/2018/10/lionel-messi-wallpaper-download-high-quality.jpg"
        },
        {
          src: "../img/copa1958.jpg"
        },
        {
          src: "https://wallpaperaccess.com/full/493700.jpg"
        },
        {
          src: "https://wallpapercave.com/wp/wp1956988.jpg"
        }
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