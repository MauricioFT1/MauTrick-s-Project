<style>
.Titulo {
  text-align: center;
  color: #777;
  font-size: 55px;
  font-family: arial;
  font-weight: bold;
  text-shadow: 0 1px 0 #cccccc, 0 2px 0 #c9c9c9, 0 3px 0 #bbbbbb,
    0 4px 0 #b9b9b9, 0 5px 0 #aaaaaa, 0 6px 1px rgba(0, 0, 0, 0.1),
    0 0 5px rgba(0, 0, 0, 0.1), 0 1px 3px rgba(0, 0, 0, 0.3),
    0 3px 5px rgba(0, 0, 0, 0.2), 0 5px 10px rgba(0, 0, 0, 0.25),
    0 10px 10px rgba(0, 0, 0, 0.2), 0 20px 20px rgba(0, 0, 0, 0.15);
}
</style>

<template>
  <div id="app">
    <v-app id="inspire">
      <v-parallax src="../img/back.jpg" height="2400">
        <v-timeline :dense="$vuetify.breakpoint.smAndDown">
          <!-- Card 1 -->
          <v-timeline-item right>
            <v-card max-width="420">
              <div class="Titulo">
                <v-card-title class="white">
                  <v-icon dark size="42" class="mr-4"></v-icon>
                  <h2 class="display-1">Copa do mundo de 1958</h2>
                </v-card-title>
              </div>
              <v-container>
                <v-row>
                  <v-col cols="12" md="10">
                    <img src="../img/copa1958.jpg" width="400" height="200" alt />
                  </v-col>
                  <v-dialog v-model="dialog" width="500">
                    <template v-slot:activator="{ on }">
                      <v-btn color="item.color" class="mx-3" outlined v-on="on">Ver mais!</v-btn>
                    </template>

                    <v-card>
                      <v-card-title primary-title><h2>Copa do mundo de 1958</h2></v-card-title>
                      <br />
                      <v-divider></v-divider>
                      <br />
                      <v-card-text>
                        A Copa do Mundo FIFA de 1958 foi a sexta edição da Copa do Mundo FIFA de
                        Futebol, que ocorreu de 10 de junho até 29 de junho de 1958. O evento foi sediado na Suécia.
                        Dezesseis seleções nacionais foram qualificadas para participar desta edição do campeonato,
                        sendo 12 delas europeias.
                        <br />A final entre Brasil e Suécia em frente a um público de 50.000 pessoas. Resultado: Vavá
                        marca
                        gol logo aos nove minutos e vira o jogo ainda no primeiro tempo numa partida excepcional
                        que,
                        mesmo com a derrota sueca por 5 a 2 em casa, foi aplaudida de pé pela torcida anfitriã, ao
                        saudar como campeões do mundo, Assim o Brasil sagrava-se pela primeira vez campeão mundial
                        de
                        futebol.
                      </v-card-text>
                      <br />
                      <v-divider></v-divider>

                      <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="dark" outlined text @click="dialog = false">Fechar</v-btn>
                      </v-card-actions>
                    </v-card>
                  </v-dialog>
                </v-row>
              </v-container>
            </v-card>
          </v-timeline-item>

          <!-- Card 2 -->
          <v-timeline-item left>
            <v-card class="mx-auto" max-width="420">
              <div class="Titulo">
                <v-card-title class="white">
                  <v-icon dark size="42" class="mr-4"></v-icon>
                  <h2 class="display-1">Copa do mundo de 1970</h2>
                </v-card-title>
              </div>
              <v-container>
                <v-row>
                  <v-col cols="12" md="10">
                    <img src="../img/copa70.jpg" width="400" height="200" alt />
                  </v-col>
                  <v-dialog v-model="dialog2" width="500">
                    <template v-slot:activator="{ on }">
                      <v-btn class="mx-3" color="item.color" outlined v-on="on">Ver mais!</v-btn>
                    </template>

                    <v-card>
                      <v-card-title
                        class=""
                        primary-title
                      ><h2>Copa do mundo de 1970</h2></v-card-title>
                      <br />
                      <v-divider></v-divider>
                      <br />
                      <v-card-text>
                        A Copa do Mundo de 1970 foi a 9ª edição da Copa do Mundo FIFA, que ocorreu
                        de
                        31 de maio até 21 de junho. A competição, conquistada pelo Brasil, foi sediada no México,
                        Dezesseis seleções nacionais foram qualificadas para participar desta edição do campeonato,
                        sendo 9 delas europeias, 5 americanas, 1 asiática e 1 africana.
                        <br />A final desta edição foi disputada pelo Brasil e a Itália. A partida foi realizada em 21 de
                        junho no Estádio Azteca na Cidade do México, com um público estimado em 108 000 pessoas. O
                        primeiro tempo terminou empatado em 1-1. Ao final dos 90 minutos, o placar era de 4-1 para a
                        equipe brasileira. O título serviu de propaganda política, quando o país estava no auge da
                        ditadura militar brasileira. Este título também pôs o Brasil como a primeira seleção a ser
                        tricampeã, confirmando a superioridade brasileira em relação ao futebol mundial. O capitão
                        Carlos Alberto Torres levantou a Taça Jules Rimet entregue pela última vez em Copas, agora
                        em
                        caráter definitivo. Pelé assim levanta sua 3 taça e considerado o melhor da copa.
                      </v-card-text>
                      <br>
                      <v-divider></v-divider>

                      <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="dark" outlined text @click="dialog2 = false">Fechar</v-btn>
                      </v-card-actions>
                    </v-card>
                  </v-dialog>
                </v-row>
              </v-container>
            </v-card>
          </v-timeline-item>

          <!-- Card 3 -->

          <v-timeline-item right>
            <v-card max-width="420">
              <div class="Titulo">
                <v-card-title class="white">
                  <v-icon dark size="42" class="mr-4"></v-icon>
                  <h2 class="display-1">Copa do mundo de 1994</h2>
                </v-card-title>
              </div>
              <v-container>
                <v-row>
                  <v-col cols="12" md="10">
                    <img src="../img/copa94.jpg" width="400" height="200" alt />
                  </v-col>
                  <v-dialog v-model="dialog3" width="500">
                    <template v-slot:activator="{ on }">
                      <v-btn color="item.color" class="mx-3" outlined v-on="on">Ver mais!</v-btn>
                    </template>

                    <v-card>
                      <v-card-title
                        class=""
                        primary-title
                      ><h2>Copa do mundo de 1994</h2></v-card-title>
                      <br />
                      <v-divider></v-divider>
                      <br>
                      <v-card-text>
                        A Copa do Mundo de 1994 foi a 15ª Copa do Mundo FIFA que foi sediada nos
                        Estados Unidos, foi o mundial do país que bateu todos os recordes de público, mantidos até
                        os
                        dias de hoje. Com um futebol extremamente eficiente e com um grupo muito unido liderado pelo
                        polêmico craque Romário, a Seleção brasileira conquistou o quarto título mundial ao bater a
                        Itália na final. O titulo do Brasil foi comemorado também como uma homenagem ao tricampeão
                        mundial de fórmula 1 Ayrton Senna, falecido em 1 de maio daquele ano.
                      </v-card-text>
                      <br>
                      <v-divider></v-divider>

                      <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="dark" outlined text @click="dialog3 = false">Fechar</v-btn>
                      </v-card-actions>
                    </v-card>
                  </v-dialog>
                </v-row>
              </v-container>
            </v-card>
          </v-timeline-item>

          <!-- Card 4 -->

          <v-timeline-item left>
            <v-card class="mx-auto" max-width="420">
              <div class="Titulo">
                <v-card-title class="white">
                  <v-icon dark size="42" class="mr-4"></v-icon>
                  <h2 class="display-1">Copa do mundo de 2002</h2>
                </v-card-title>
              </div>
              <v-container>
                <v-row>
                  <v-col cols="12" md="10">
                    <img src="../img/copa02.jpg" width="400" height="200" alt />
                  </v-col>
                  <v-dialog v-model="dialog4" width="500">
                    <template v-slot:activator="{ on }">
                      <v-btn class="mx-3" color="item.color" outlined v-on="on">Ver mais!</v-btn>
                    </template>

                    <v-card>
                      <v-card-title
                        class=""
                        primary-title
                      ><h2>Copa do mundo de 2002</h2></v-card-title>
                      <br />
                      <v-divider></v-divider>
                      <br>
                      <v-card-text>
                        A Copa do Mundo de 2002 foi a 17ª Copa do Mundo FIFA que foi sediada no
                        Japão e
                        Coreia do sul que reuniu 32 equipes entre 31 de maio a 30 de junho. Das 32 sendo 13 delas
                        europeias, 8 americanas, 4 asiática e 5 africana e as duas ultimas vagas foram disputadas
                        por
                        play-off entre AFC e UEFA e entre CONMEBOL e OFC.
                        <br />O país manteve a situação de único país a participar de todas as edições do torneio da FIFA
                        e
                        conquistou o quinto título do torneio ao vencer a Alemanha na final por 2-0, com Ronaldo
                        marcando os dois gols em cima do Oliver Kahn melhor jogador e goleiro do mundo daquele ano.
                      </v-card-text>
                      <br>
                      <v-divider></v-divider>

                      <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="dark" outlined text @click="dialog4= false">Fechar</v-btn>
                      </v-card-actions>
                    </v-card>
                  </v-dialog>
                </v-row>
              </v-container>
            </v-card>
          </v-timeline-item>

          <!-- Card 5 -->

          <v-timeline-item right>
            <v-card max-width="420">
              <div class="Titulo">
                <v-card-title class="white">
                  <v-icon dark size="42" class="mr-4"></v-icon>
                  <h2 class="display-1">Copa do mundo de 2014</h2>
                </v-card-title>
              </div>
              <v-container>
                <v-row>
                  <v-col cols="12" md="10">
                    <img src="../img/copa14.jpg" width="400" height="200" alt />
                  </v-col>
                  <v-dialog v-model="dialog5" width="500">
                    <template v-slot:activator="{ on }">
                      <v-btn color="item.color" class="mx-3" outlined v-on="on">Ver mais!</v-btn>
                    </template>

                    <v-card>
                      <v-card-title
                        class=""
                        primary-title
                      ><h2>Copa do mundo de 2014</h2></v-card-title>
                      <br />
                      <v-divider></v-divider>
                      <br>
                      <v-card-text>
                        A Copa do Mundo de 2014 foi a 20ª Copa do Mundo FIFA que foi sediada no
                        Brasil,
                        anfitrião da competição pela segunda vez. Com doze cidades-sede, o campeonato começou a ser
                        disputado no dia 12 de junho e terminou em 13 de julho. Das 32 sendo 13 delas europeias, 7
                        americanas, 4 asiática, 5 africana e 1 oceania. As duas ultimas vagas foram disputadas por
                        play-off entre AFC e UEFA e entre CONMEBOL e OFC.
                        <br />O jogo das semifinais entre Brasil e Alemanha, realizado no dia 8 de julho, ficou marcado
                        pela
                        esmagadora derrota sofrida pela Seleção Brasileira de Futebol contra a Seleção Alemã de
                        Futebol.
                        A vitória alemã, por expressivos 7–1, é considerada um dos resultados mais notáveis da
                        história
                        do futebol, sendo a Alemanha campeã do mundo em cima da Argentina por 1-0, mesmo o Messi
                        sendo
                        considerado melhor jogador da copa.
                      </v-card-text>
                      <br>
                      <v-divider></v-divider>

                      <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="dark" outlined text @click="dialog5 = false">Fechar</v-btn>
                      </v-card-actions>
                    </v-card>
                  </v-dialog>
                </v-row>
              </v-container>
            </v-card>
          </v-timeline-item>
          <!-- Card 6 -->
          <v-timeline-item left>
            <v-card class="mx-auto" max-width="420">
              <div class="Titulo">
                <v-card-title class="white">
                  <v-icon dark size="42" class="mr-4"></v-icon>
                  <h2 class="display-1">Copa do mundo de 2018</h2>
                </v-card-title>
              </div>
              <v-container>
                <v-row>
                  <v-col cols="12" md="10">
                    <img src="../img/copa18.jpg" width="400" height="200" alt />
                  </v-col>
                  <v-dialog v-model="dialog6" width="500">
                    <template v-slot:activator="{ on }">
                      <v-btn class="mx-3" color="item.color" outlined v-on="on">Ver mais!</v-btn>
                    </template>

                    <v-card>
                      <v-card-title
                        class=""
                        primary-title
                      ><h2>Copa do mundo de 2018</h2></v-card-title>
                      <br />
                      <v-divider></v-divider>
                      <br>
                      <v-card-text>
                        A Copa do Mundo de 2018 foi a 21ª Copa do Mundo FIFA que foi sediada na
                        Russia,
                        Entrou para a história por ter sido a Copa do Mundo mais cara da história até então, com um
                        custo total de 14,2 bilhões de dólares.
                        A seleção brasileira acabou prejudicada por um mau primeiro tempo e superada pela eficiência
                        de
                        Bélgica nesta sexta-feira, em Kazan. A derrota por 2 a 1 pelas quartas de final da Copa do
                        Mundo
                        da Rússia, tendo a França como campeã fazendo 4-2 contra a Croácia que teve com Modric
                        melhor
                        jogador da Copa, porem muito questionado sobre o papel dele.
                      </v-card-text>
                      <br>
                      <v-divider></v-divider>

                      <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="dark" outlined text @click="dialog6 = false">Fechar</v-btn>
                      </v-card-actions>
                    </v-card>
                  </v-dialog>
                </v-row>
              </v-container>
            </v-card>
          </v-timeline-item>
        </v-timeline>
      </v-parallax>
    </v-app>
  </div>
</template>

<script>
export default {
  name: "Copas",
  data() {
    return {
      dialog: false,
      dialog2: false,
      dialog3: false,
      dialog4: false,
      dialog5: false,
      dialog6: false
    };
  }
};
</script>