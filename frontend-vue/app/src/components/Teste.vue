<style>
.cor {
  color: black;
}
</style>

<template>
  <v-carousel
    cycle
    height="400"
    hide-delimiter-background
    :show-arrows="false"
  >
    <v-carousel-item
      v-for="(slide, i) in slides"
      :key="i"
    >
      <v-sheet
        :item="items[i]"
        height="100%"
      >
        <v-row
          class="fill-height"
          align="center"
          justify="center"
        >
          <div class="display-3">{{ slide }} Slide</div>
        </v-row>
      </v-sheet>
    </v-carousel-item>
  </v-carousel>
</template>

<script>
  export default {
    data () {
      return {
        items: [
        {
          src: "https://wallpapercave.com/wp/wp1956988.jpg"
        },
        {
          src: "https://wallpapercave.com/wp/wp1956988.jpg"
        },
        {
          src: "https://wallpapercave.com/wp/wp1956988.jpg"
        },
        {
          src: "https://wallpapercave.com/wp/wp1956988.jpg"
        }
        ],
        slides: [
          'First',
          'Second',
          'Third',
          'Fourth',
          'Fifth',
        ],
      }
    },
  }
</script>





<!--  <style>
.triangulo {
  width: 0; 
  height: 0; 
  border-left: 500px solid transparent;
  border-top: 300px solid blue;
}

</style>

<template>

  <div class="triangulo"></div>


</template>
   
   
   
   
   
   
   
   
   
<v-container fluid>
      <v-row justify="space-around">
        <v-col cols="7">
          <v-carousel cycle height="500" hide-delimiter-background show-arrows-on-hover>
            <v-carousel-item
              v-for="(item,i) in items"
              :key="i"
              :src="item.src"
              reverse-transition="fade-transition"
            >
              <v-row class="fill-height" align="center" justify="center">
                <div class="display-2">{{ slide }}</div>
              </v-row>
            </v-carousel-item>
          </v-carousel>
        </v-col>

        <v-col cols="3">
          <v-card class="mx-right" max-width="1300" max-height="1000" outlined>
            <v-img width="1300" height="700" src="../img/brasil.jpg">
              <strong>Conheça tambem!</strong>
              <v-divider></v-divider>
              <a href="https://www.fifa.com/" target="_blank">FIFA</a>
              <br />
              <a href="http://www.espn.com.br/futebol/" target="_blank">ESPN</a>
              <br />
              <a href="https://globoesporte.globo.com/" target="_blank">Globo Esporte</a>
              <br />
              <v-divider></v-divider>
              <br />
              <li class="list-group-item">
                <strong>Campeonatos Brasil a fora:</strong>

                <br />
                <a
                  href="https://www.google.com/search?ei=wG-3XPXMH__B5OUP3vWSqAU&q=la+liga&oq=la+liga&gs_l=psy-ab.3..35i39i70i253j0i67l2j0j0i131j0j0i67j0l2j0i131.8392.9143..9246...0.0..0.229.984.0j2j3....3..0....1..gws-wiz.......0i71j35i39j0i131i67.ZapXGTTBu9Q"
                  target="_blank"
                >La Liga</a>
                <br />
                <a
                  href="https://www.google.com/search?ei=y2-3XLeLIYDZ5OUPsK272Aw&q=premier+league&oq=Premier+le&gs_l=psy-ab.1.0.35i39i70i253j0j0i67j0i131j0l2j0i67j0j0i67l2.84401.87344..88770...3.0..1.406.3142.2-5j4j1....3..0....1..gws-wiz.....6..0i71j35i39.7AXqWFcsNzo"
                  target="_blank"
                >Premier League</a>
                <br />
                <a
                  href="https://www.google.com/search?ei=JXC3XMqgLfa45OUPmfmC2A0&q=champions+league&oq=cham&gs_l=psy-ab.1.1.35i39i70i253j35i39j0i131j0i131i67l2j0i131j0j0i67j0l2.46488.46864..49071...0.0..0.348.1088.0j1j1j2....3..0....1..gws-wiz.......0i71.e6R0InP6FiE"
                  target="_blank"
                >Champions League</a>
                <br />
                <a
                  href="https://www.google.com/search?ei=WHC3XMCVFeae5OUPzoaN4A4&q=libertadores&oq=libertadores&gs_l=psy-ab.3..35i39i70i253j0i67j0j0i67j0i131j0j0i67j0l2j0i131.12296.14354..14741...0.0..1.548.3941.0j1j3j5j2j1....3..0....1..gws-wiz.......0i71j35i39j0i131i67.NIK_3rPb81w"
                  target="_blank"
                >Libertadores</a>
              </li>
              <v-divider></v-divider>
              <br />
              <li class="list-group-item">
                <strong>Campeonatos:</strong>

                <br />
                <a href="{% url 'brasileirao2018' %}" target="_blank">Brasileirão 2018</a>
                <br />
                <a href="{% url 'brasileirao2008' %}" target="_blank">Brasileirão 2008</a>
                <br />
                <a href="{% url 'copadomundo' %}" target="_blank">Copa do Mundo</a>
              </li>
            </v-img>
          </v-card>
        </v-col>
      </v-row>
    </v-container>-->