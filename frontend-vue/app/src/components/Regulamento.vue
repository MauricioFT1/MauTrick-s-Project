<template>
  <v-container class="backgroud" fluid>
    <v-row justify="space-around">

    <!-- Inicio coluna da esquerda (Botões) -->
      <v-col cols="3">
        <v-card class="mx-right" max-width="1300" max-height="1000" outlined>
          <v-img width="1300" height="506" src="../img/brasil.jpg">
          <v-btn href="#item-1-2" block dark>1.1 Campo</v-btn>
            <v-btn href="#item-1-2" block color="#9E9E9E">1.2 Bola</v-btn>
            <v-btn href="#item-1-3" block dark>1.3 Jogadores</v-btn>
            <v-btn href="#item-1-4" block color="#9E9E9E">1.4 Equipamento dos Jogadores</v-btn>
            <v-btn href="#item-1-5" block dark>1.5 Arbitragem</v-btn>
            <v-btn href="#item-1-6" block color="#9E9E9E">1.6 Duração da partida</v-btn>
            <v-btn href="#item-1-7" block dark>1.7 A início e o reinício do jogo</v-btn>
            <v-btn href="#item-1-8" block color="#9E9E9E">1.8 A bola em jogo e fora de jogo</v-btn>
            <v-btn href="#item-1-9" block dark>1.9 O gol</v-btn>
            <v-btn href="#item-1-10" block color="#9E9E9E">1.10 O impedimento</v-btn>
            <v-btn href="#item-1-11" block dark>1.11 Tiro livre direto</v-btn>
            <v-btn href="#item-1-12" block color="#9E9E9E">1.12 Pênalti</v-btn>
            <v-btn href="#item-1-13" block dark>1.13 arremesso lateral</v-btn>
            <v-btn href="#item-1-14" block color="#9E9E9E">1.14 tiro de meta</v-btn>
          </v-img>
        </v-card>
      </v-col>
    <!-- Final coluna da esquerda (Botões) -->

    <!-- Inicio coluna da direita (Regras) -->
      <v-col cols="7">
        <div data-spy="scroll" data-target="#navbar-exemplo3" data-offset="0">
          <h1 id="item-1">1. Regras</h1>
          <br />
          <h2 id="item-1-1">1.1 Campo</h2>
          <li>
            O campo de jogo deve ser retangular, com um máximo de 120 m e um mínimo de 90 m de
            comprimento,
            por uma largura máxima de 90 m e mínima de 45 m. Em partidas internacionais, essas medidas
            mudam
            para 110/100 m de comprimento e 75/64 m de largura.
          </li>

          <li>
            Deve ser marcado com linhas visíveis de no máximo 12 cm de largura, sendo chamadas laterais
            as
            mais longas e de fundo as mais curtas. Em cada canto do retângulo deve haver uma bandeirola
            de
            no máximo 1,50 m de altura.
          </li>

          <li>
            O centro do campo será marcado com um ponto, em torno do qual se traçará uma circunferência
            com
            9,15 m de raio
          </li>

          <li>
            A pequena área será delimitada por duas linhas perpendiculares à linha de fundo, traçadas a
            5,50
            m de cada trave e avançando 5,50 m para dentro do campo, unidas então por outra linha.
          </li>

          <li>
            A grande área terá linhas semelhantes, colocadas a 16,50 m de cada trave a avançando outros
            16,50 m campo adentro. Essa também é a área de pênalti, penalidade a ser cobrada de um ponto
            situado a 11 m do centro do gol. Desse ponto serão traçados, no exterior de cada grande
            área,
            arcos com 9,15 m de raio.
          </li>
          <li>
            Bandeirinhas de escanteio - Em cada canto do campo de jogo será colocado um poste não
            pontiagudo
            com uma bandeirinha. A altura mínima do poste será de 1,5m de altura. Também poderão ser
            colocadas bandeirinhas em cada extremidade da linha do meio de campo, a uma distância mínima
            de
            1 metro do lado de fora da linha lateral do campo.
          </li>

          <li>Em cada canto, a partir da bandeirola, devem ser traçados arcos com 1 m de raio.</li>

          <li>
            Balizas: Na parte central de cada linha de fundo serão colocadas traves, separadas entre si,
            interiormente, por 7,32 m, unidas em cima por um travessão colocado a 2,44 m do solo. Estes
            postes e estes travessões deverão ser de cor branca. A largura ou diâmetro das traves e
            travessões não pode exceder 12 cm, e do lado de fora do campo elas podem ser guarnecidas por
            redes. Se forem usadas, estas redes devem ser fixadas nas metas e no solo atrás da meta, com
            a
            condição de que estejam presas de forma conveniente e não atrapalhem o goleiro.
          </li>
          <br />
          <h2 id="item-1-2">1.2 Bola</h2>

          <strong>A bola de jogo deve:</strong>

          <li>Ser esférica;</li>

          <li>Ser de borracha ou outro material duro;</li>

          <li>Com uma circunferência não superior a 70 cm e não inferior a 68 cm;</li>

          <li>Com peso não superior a 450 g e não inferior a 410 g, no começo da partida;</li>
          <br />

          <h2 id="item-1-3">1.3 Jogadores</h2>

          <li>
            A partida será jogada por duas equipes formadas por no máximo 11 jogadores e no mínimo 7. A
            partida não pode ser iniciada se um dos times estiver com menos de sete jogadores, dos quais
            um
            será o goleiro.
          </li>

          <li>
            Em competições oficiais organizadas: pela FIFA, o máximo de substituições num jogo é de três
            jogadores. O regulamento da competição deve precisar o número de suplentes - entre três no
            minimo e sete no máximo - que é possível designarem nessa qualidade. Em jogos de Seleções
            Nacionais "A" pode utilizar-se um máximo de seis suplentes. Nos restantes jogos é possível
            utilizar um maior numero de suplentes desde que haja um acordo prévio entre as equipes
            envolvidas, quanto ao número máximo de substituições e o árbitro seja informado antes do
            início
            do jogo.
          </li>

          <li>
            A substituição de jogadores só ocorre com a autorização do árbitro, e deve ocorrer fora do
            terreno de jogo, junto à linha do meio campo. O jogador substituto só pode entrar em campo,
            quando o substituído já tiver saído. Se a substituição ocorrer de forma irregular, o árbitro
            deverá paralisar a partida, ordenar a saída do jogador que entrou irregularmente e reiniciar
            o
            jogo com um pontapé de livre indireto. Considera-se substituição consumada no momento em que
            suplente entra em campo. O jogador substituído não pode voltar a jogar mais no jogo. Em
            qualquer
            jogo, os nomes dos suplentes deverão constar na ficha de jogo antes do início do jogo. Caso
            contrário, não poderá participar, por não ter sido inscrito.
          </li>

          <li>Os goleiros podem ser substituídos 1 vez e à 2ª vez entra um defesa com a ordem do árbitro.</li>

          <br />

          <h2 id="item-1-4">1.4 equipamento dos jogadores</h2>Os jogadores não podem utilizar nenhum objeto que seja perigoso para eles mesmos ou para os
          demais
          jogadores (incluindo qualquer tipo de jóias). O uniforme completo consiste de:
          <li>Camisa de mangas curtas ou compridas</li>

          <li>Calções</li>

          <li>Meias Compridas</li>

          <li>Caneleiras (material adequado)</li>

          <li>Chuteiras com cravo</li>

          <li>Munhequeiras</li>As cores das camisas das duas equipes devem ser diferentes, para não confundir o público e nem a
          arbitragem. Cada guarda-redes (PT-PT) ou goleiro (PT-BR) deve usar um equipamento de cores que o
          distingua dos jogadores, do árbitro e dos árbitros assistentes.
          A cor da camisa do quarteto de arbitragem deve ser diferente das cores das camisas de ambos os
          times,
          e cada um com seu próprio número.
          <br>
          <br>
          <h2 id="item-1-5">1.5 Arbitragem</h2>Cada partida será controlada por um árbitro, que terá a autoridade total para se fazer cumprir as
          regras de jogo na partida para a qual tenha sido designado.
          O árbitro controlará a partida em cooperação com os árbitros assistentes. Interromperá,
          suspenderá ou
          finalizará a partida quando julgar oportuno, no caso de que se cometam infrações às regras de
          jogo.
          As decisões do árbitro sobre fatos em relação com o jogo são definitivas.
          O árbitro poderá mudar sua decisão unicamente se perceber que sua decisão é incorreta ou, se o
          julgar
          necessário conforme indicação de outro membro do quarteto de arbitragem, sempre que ainda não
          tenha
          reiniciado a partida.
          A reclamação com o árbitro, com o que ele apitou pode lhe custar uma expulsão caso ele se sinta
          ofendido.
          São dois os árbitros assistente. Deverão ser designados aos dois árbitros assistentes, sempre
          submetido à decisão do árbitro e tem o dever de indicar:
          <li>quando a bola sair completamente do campo de jogo</li>

          <li>quando deverá ser punido um jogador por estar em posição de fora-de-jogo</li>

          <li>quando for solicitada uma substituição</li>

          <li>quando ocorrer uma infração ou um incidente fora do campo visual do árbitro</li>

          <li>
            quando forem cometidas infrações em que os árbitros assistentes estejam mais perto da ação
            que o
            árbitro (isso inclui em certas circunstâncias, infrações cometidas dentro da área penal)
          </li>

          <li>
            quando, nos pontapés de grande penalidade, o guarda-redes se adiantar além da linha de
            baliza
            antes de a bola ser chutada e se a bola ultrapassar a linha de baliza.
          </li>

          <br>

          <h2 id="item-1-6">1.6 duração da partida</h2>A partida deve durar 90 minutos, divididos em dois tempos de 45 minutos, com um intervalo de no
          máximo 15 minutos.
          O intervalo não deve exceder os 15 minutos. Um jogo interrompido definitivamente antes do seu
          termo
          deve ser repetido, salvo disposição contrária estipulada no regulamento da competição. Todos os
          jogos devem acrescer seu tempo de acréscimo, que varia de 2 a 4 minutos a mais dos 90 minutos
          normal
          de uma partida de futebol. Depende da condição temporária do jogo, caso ele fique parado por
          muito
          tempo por motivos de falta de luz, brigas, contusões sérias que tenham dificuldades de retira-lo
          de
          campo, o acréscimo poderá ser muito mais elevado.
          <br>
          <br>

          <h2 id="item-1-7">1.7 o início e o reinício do jogo</h2>Para começar será lançada uma moeda e a equipe que ganhar começará dando uma direção ao jogo. O
          lançamento inicial é uma forma de iniciar e reiniciar o jogo. Caso acontecer alguma falta ou
          infração o arbitro deixará cair a bola no lugar onde em que se encontrava quando foi
          interrompida a
          partida e o jogo será considerado reiniciado quando a bola tocar ao solo.
          <br>
          <br>
          <h2 id="item-1-8">1.8 a bola em jogo e fora de jogo</h2>A bola está fora de jogo quando:
          <li>
            Tiver ultrapassado completamente uma das linhas que delimitam o campo, seja por terra ou
            pelo
            ar;
          </li>

          <li>O jogo tiver sido interrompido pelo árbitro.</li>A bola está em jogo quando:
          <li>Rebater nas traves,travessões ou nas bandeirinhas de canto;</li>

          <li>Rebater no árbitro ou nos assistentes.</li>

          <br />

          <h2 id="item-1-9">1.9 O gol</h2>Quando um jogador chuta uma bola para o gol do seu time é gol contra, que significa que o jogador
          fez
          um gol pelo time adversário (a favor do time adversário). Também há o gol direto, em que o
          jogador
          vai até a área e chuta a bola, e o gol indireto, onde o jogador passa a bola para outro, que faz
          o
          gol.
          <br>
          <br>

          <h2 id="item-1-10">1.10 O impedimento</h2>A regra de impedimento entende-se melhor quando a dividimos em duas partes: a posição de
          impedimento
          e a marcação da irregularidade.
          Um jogador se encontra em posição de impedimento quando quatro condições se cumprem:
          <li>Este jogador está no campo de ataque;</li>

          <li>Ele está mais próximo da linha de fundo adversária do que a própria bola;</li>

          <li>
            Ele se encontra mais próximo da linha de fundo adversária do que o penúltimo oponente -
            qualquer
            parte do seu corpo, tronco, cabeça ou pés, exceto as mãos;
          </li>

          <li>
            O companheiro que lhe passa diretamente a bola não está cobrando um tiro de meta, um
            escanteio
            ou um arremesso lateral.
          </li>Porém, o simples fato de um jogador estar em posição de impedimento não implica a marcação
          automática
          da irregularidade. O juiz só deve apitar tiro livre indireto, paralisando o jogo, no momento em
          que
          a bola tocar acidentalmente esse jogador em posição irregular, ou no momento em que a bola lhe
          for
          destinada num passe direto, e mesmo assim, somente quando na opinião do juiz, uma das três
          condições
          abaixo se cumpra:
          <li>
            O jogador em posição de impedimento participa ativamente da jogada: ao receber um passe, ou
            desviar a bola;
          </li>

          <li>
            Esse jogador obtém vantagem direta a partir do impedimento: ao aproveitar um rebote, se no
            momento do chute ou cabeçada estava adiantado;
          </li>

          <li>
            Ele atrapalha diretamente um adversário: ao obstruir claramente sua visão, ou enganá-lo com
            uma
            finta de corpo.
          </li>

          <br>

          <h2 id="item-1-11">1.11 tiro livre direto</h2>Tanto para os tiros livres indiretos como para os diretos, a bola deverá estar imóvel quando se
          lança
          o tiro e o executor não poderá voltar a jogar a bola antes de que esta tenha tocado a outro
          jogador
          <br>
          <br>

          <h2 id="item-1-12">1.12 Pênalti</h2>Será concedido um tiro penal contra a equipe que cometer uma das dez faltas que levam a um tiro direto, dentro de sua própria área penal enquanto a bola está em jogo.
          Um gol poderá ser marcado diretamente de um tiro penal.
          Será concedido tempo adicional para poder executar um tiro penal ao final de cada tempo ou ao final dos períodos suplementares.
          <br>
          <br>

          <h2 id="item-1-13">1.13 Arremesso lateral</h2>O lançamento lateral deve ser executado com as mãos, sempre repondo a bola em jogo quando esta sair por uma das linhas laterais. Um gol não pode ser marcado direto de um arremesso lateral. No momento do lançamento, o jogador deve estar de frente para o campo, com os dois pés sobre a linha lateral ou sobre o terreno exterior a esta linha e segurando a bola com as duas mãos e acima da cabeça.
          <br>
          <br>

          <h2 id="item-1-14">1.14 Tiro de meta</h2><br>O tiro de meta ou pontapé de baliza é um dos métodos para reiniciar a partida. Deve ser feito pela equipe defensiva quando a bola sair completamente do campo pela linha de fundo sem que um gol tenha sido marcado, tendo sido tocada por último por um jogador atacante adversário.
          Um gol pode ser marcado diretamente a partir de um pontapé de baliza, mas apenas contra o lado do adversário (ou seja, um gol contra não pode ser marcado).
          Quando o goleiro posiciona a bola para dar o pontapé de Baliza, o adversário não pode roubar a bola, somente depois que o goleiro tocar nela.
          <br>
        </div>
      </v-col>
    <!-- Inicio coluna da direita (Regras) -->
    
    </v-row>
  </v-container>
<!-- </v-parallax> -->
</template>
