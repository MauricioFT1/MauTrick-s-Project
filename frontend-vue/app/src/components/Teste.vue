<style>
.teste{
  max-height: 500px;
  max-width: 500px;
  margin: auto;
}

.back {
  background-color: black;
}

</style>
<template>
  <div class="black">
      <v-carousel cycle height="700">
      <div class="teste">
      <v-carousel-item
        v-for="(item,i) in items"
        :key="i"
        :src="item.src"
        reverse-transition="fade-transition"
        transition="fade-transition"
      >
      </v-carousel-item>
      </div>
    </v-carousel>
  </div>
</template>

<script>
export default {
      data() {
    return {
      items: [
        {
          src:
            "https://thumbs.dreamstime.com/t/bola-de-futebol-no-fundo-preto-rendi%C3%A7%C3%A3o-d-75694023.jpg"
        },
        {
          src: "http://pngimg.com/uploads/football/football_PNG52772.png"
        },
        {
          src: "http://pngimg.com/uploads/football/football_PNG52791.png"
        },
        {
          src: "http://pngimg.com/uploads/football/football_PNG52797.png"
        }
      ]
    };
  },
}
</script> 