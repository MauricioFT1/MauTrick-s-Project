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
        <div class="Titulo">Brasileirão 2008</div>
      <br>
      <div id="app" class="mx-12">
        <v-app id="inspire" dark>
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
          name: "1. São Paulo",
          pontos: 75,
          jogos: 38,
          vitorias: 21,
          empates: 12,
          derotas: "5"
        },
        {
          name: "2. Grêmio",
          pontos: 72,
          jogos: 38,
          vitorias: 21,
          empates: 9,
          derotas: "8"
        },
        {
          name: "3. Cruzeiro",
          pontos: 67,
          jogos: 38,
          vitorias: 21,
          empates: 4,
          derotas: "13"
        },
        {
          name: "4. Palmeiras",
          pontos: 65,
          jogos: 38,
          vitorias: 19,
          empates: 8,
          derotas: "11"
        },
        {
          name: "5. Flamengo",
          pontos: 64,
          jogos: 38,
          vitorias: 18,
          empates: 10,
          derotas: "10"
        },
        {
          name: "6. Internacional",
          pontos: 54,
          jogos: 38,
          vitorias: 15,
          empates: 9,
          derotas: "14"
        },
        {
          name: " 7. Botafogo",
          pontos: 53,
          jogos: 38,
          vitorias: 15,
          empates: 5,
          derotas: "15"
        },
        {
          name: "8. Goiás",
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
          name: "10. Vitória",
          pontos: 52,
          jogos: 38,
          vitorias: 15,
          empates: 7,
          derotas: "16"
        },
        {
          name: "11. Sport	",
          pontos: 52,
          jogos: 38,
          vitorias: 14,
          empates: 10,
          derotas: "14"
        },
        {
          name: "12. Atlético-MG",
          pontos: 48,
          jogos: 38,
          vitorias: 12,
          empates: 12,
          derotas: "14"
        },
        {
          name: "13. Atlético-PR",
          pontos: 45,
          jogos: 38,
          vitorias: 12,
          empates: 9,
          derotas: "17"
        },
        {
          name: "14. Fluminense",
          pontos: 45,
          jogos: 38,
          vitorias: 11,
          empates: 12,
          derotas: "15"
        },
        {
          name: "15. Santos",
          pontos: 45,
          jogos: 38,
          vitorias: 11,
          empates: 12,
          derotas: "15"
        },
        {
          name: "16. Náutico",
          pontos: 44,
          jogos: 38,
          vitorias: 11,
          empates: 11,
          derotas: "16"
        },
        {
          name: "17. Figueirense",
          pontos: 44,
          jogos: 38,
          vitorias: 11,
          empates: 11,
          derotas: "16"
        },
        {
          name: "18. Vasco",
          pontos: 40,
          jogos: 38,
          vitorias: 11,
          empates: 7,
          derotas: "20"
        },
        {
          name: "19. Portuguesa",
          pontos: 38,
          jogos: 38,
          vitorias: 9,
          empates: 11,
          derotas: "18"
        },
        {
          name: "20. Ipatinga",
          pontos: 35,
          jogos: 38,
          vitorias: 9,
          empates: 8,
          derotas: "21"
        }
      ]
    };
  }
};
</script>
