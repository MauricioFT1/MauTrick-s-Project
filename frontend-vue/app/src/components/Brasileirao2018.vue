<style>
.Titulo{
text-align: center;
color: #777;
font-size: 55px;
font-family: arial;
font-weight:bold;
text-shadow: 0 1px 0 #cccccc, 0 2px 0 #c9c9c9,
0 3px 0 #bbbbbb, 0 4px 0 #b9b9b9,
0 5px 0 #aaaaaa, 0 6px 1px rgba(0, 0, 0, 0.1),
0 0 5px rgba(0, 0, 0, 0.1), 0 1px 3px rgba(0, 0, 0, 0.3),
0 3px 5px rgba(0, 0, 0, 0.2), 0 5px 10px rgba(0, 0, 0, 0.25),
0 10px 10px rgba(0, 0, 0, 0.2), 0 20px 20px rgba(0, 0, 0, 0.15);
}
</style>

<template>
  <div>
    <v-parallax src="../img/back.jpg" height="1300">
        <div class="Titulo">Brasileirão 2018</div>
      <br />
      <div id="app" class="mx-12">
        <v-app id="inspire">
          <v-card>
            <br />

            <v-data-table :headers="headers" :items="desserts"></v-data-table>
          </v-card>
        </v-app>
      </div>
    </v-parallax>
  </div>
</template>


<script>
export default {
  data() {
    return {
      headers: [
        {
          text: "Pocisão ",
          align: "left",
          sortable: false,
          value: "name"
        },
        { text: "Pontos", value: "pontos" },
        { text: "Jogos", value: "jogos" },
        { text: "Vitórias", value: "vitorias" },
        { text: "Empates", value: "empates" },
        { text: "Derotas", value: "derotas" }
      ],
      desserts: [
        {
          name: "1. Palmeiras",
          pontos: 80,
          jogos: 38,
          vitorias: 23,
          empates: 11,
          derotas: "4"
        },
        {
          name: "2. Flamengo",
          pontos: 72,
          jogos: 38,
          vitorias: 21,
          empates: 9,
          derotas: "8"
        },
        {
          name: "3. Internacional",
          pontos: 69,
          jogos: 38,
          vitorias: 19,
          empates: 12,
          derotas: "7"
        },
        {
          name: "4. Grêmio",
          pontos: 66,
          jogos: 38,
          vitorias: 18,
          empates: 12,
          derotas: "8"
        },
        {
          name: "5. São Paulo",
          pontos: 63,
          jogos: 38,
          vitorias: 16,
          empates: 16,
          derotas: "7"
        },
        {
          name: "6. Atlético-MG",
          pontos: 59,
          jogos: 38,
          vitorias: 17,
          empates: 8,
          derotas: "13"
        },
        {
          name: " 7. Athletico-PR",
          pontos: 57,
          jogos: 38,
          vitorias: 16,
          empates: 9,
          derotas: "13"
        },
        {
          name: "8. Cruzeiro",
          pontos: 53,
          jogos: 38,
          vitorias: 14,
          empates: 11,
          derotas: "13"
        },
        {
          name: "9. Botafogo",
          pontos: 51,
          jogos: 38,
          vitorias: 13,
          empates: 12,
          derotas: "13"
        },
        {
          name: "10. Santos",
          pontos: 50,
          jogos: 38,
          vitorias: 13,
          empates: 11,
          derotas: "14"
        },
        {
          name: "11. Bahia	",
          pontos: 48,
          jogos: 38,
          vitorias: 12,
          empates: 12,
          derotas: "14"
        },
        {
          name: "12. Fluminense",
          pontos: 45,
          jogos: 38,
          vitorias: 12,
          empates: 9,
          derotas: "17"
        },
        {
          name: "13. Corinthians",
          pontos: 44,
          jogos: 38,
          vitorias: 11,
          empates: 11,
          derotas: "16"
        },
        {
          name: "14. Chapecoense",
          pontos: 44,
          jogos: 38,
          vitorias: 11,
          empates: 11,
          derotas: "16"
        },
        {
          name: "15. Ceará",
          pontos: 44,
          jogos: 38,
          vitorias: 10,
          empates: 14,
          derotas: "14"
        },
        {
          name: "16. Vasco",
          pontos: 43,
          jogos: 38,
          vitorias: 10,
          empates: 13,
          derotas: "15"
        },
        {
          name: "17. Sport",
          pontos: 42,
          jogos: 38,
          vitorias: 11,
          empates: 9,
          derotas: "18"
        },
        {
          name: "18. América-MG",
          pontos: 40,
          jogos: 38,
          vitorias: 10,
          empates: 10,
          derotas: "18"
        },
        {
          name: "19. Vitória",
          pontos: 37,
          jogos: 38,
          vitorias: 9,
          empates: 10,
          derotas: "19"
        },
        {
          name: "20. Paraná",
          pontos: 23,
          jogos: 38,
          vitorias: 4,
          empates: 11,
          derotas: "23"
        }
      ]
    };
  }
};
</script>