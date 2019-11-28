<style>
.dropdown {
  text-align: center;
  height: 200px;
  width: 400px;
}
</style>
<template>
  <div class="text-center">
    <v-menu offset-y>
      <template v-slot:activator="{ on }">
        <v-btn dark v-on="on">Links do curso</v-btn>
      </template>
      <v-list class="dropdown">
        <v-list-item-title>
          Endereço: Rodovia BR 280 - km 27
          <br />Cx. Postal 21 - CEP 89245-000
          <br />Araquari - SC - Fone (47)
          3803-7200
          <br />

          <a href="https://araquari.ifc.edu.br/" target="_blank">
            Instituto Federal Catarinense campus
            Araquari
          </a>
          <br />Site do Professor:
          <a
            href="https://sites.google.com/view/eduardodasilva"
            target="_blank"
          >Eduardo da Silva</a>
          <br />Site da Materia:
          <a
            href="https://sites.google.com/view/eduardodasilva/ensino/desenvolvimento-web-ii"
            target="_blank"
          >Desenvolvimento Web II</a>
        </v-list-item-title>
      </v-list>
    </v-menu>
    <v-menu offset-y>
      <template v-slot:activator="{ on }">
        <v-btn dark v-on="on">Links do curso</v-btn>
      </template>
      <v-list class="dropdown">
        <v-list-item-title>
          Endereço: Rodovia BR 280 - km 27
          <br />Cx. Postal 21 - CEP 89245-000
          <br />Araquari - SC - Fone (47)
          3803-7200
          <br />

          <a href="https://araquari.ifc.edu.br/" target="_blank">
            Instituto Federal Catarinense campus
            Araquari
          </a>
          <br />Site do Professor:
          <a
            href="https://sites.google.com/view/eduardodasilva"
            target="_blank"
          >Eduardo da Silva</a>
          <br />Site da Materia:
          <a
            href="https://sites.google.com/view/eduardodasilva/ensino/desenvolvimento-web-ii"
            target="_blank"
          >Desenvolvimento Web II</a>
        </v-list-item-title>
      </v-list>
    </v-menu>
    <v-divider vertical></v-divider>

    <v-menu offset-y>
      <template v-slot:activator="{ on }">
        <v-btn dark v-on="on">Links do curso</v-btn>
      </template>
      <v-list class="dropdown">
        <v-list-item-title>
          Endereço: Rodovia BR 280 - km 27
          <br />Cx. Postal 21 - CEP 89245-000
          <br />Araquari - SC - Fone (47)
          3803-7200
          <br />

          <a href="https://araquari.ifc.edu.br/" target="_blank">
            Instituto Federal Catarinense campus
            Araquari
          </a>
          <br />Site do Professor:
          <a
            href="https://sites.google.com/view/eduardodasilva"
            target="_blank"
          >Eduardo da Silva</a>
          <br />Site da Materia:
          <a
            href="https://sites.google.com/view/eduardodasilva/ensino/desenvolvimento-web-ii"
            target="_blank"
          >Desenvolvimento Web II</a>
        </v-list-item-title>
      </v-list>
    </v-menu>
  </div>
</template>

