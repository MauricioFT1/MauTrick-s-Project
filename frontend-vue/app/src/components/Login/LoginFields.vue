

<template>
  <v-card-text class="">
    <v-form ref="form">
      <v-text-field label="Usuário"
        v-model="credentials.username"
        name="login"
        :counter="30"
        prepend-icon="person"
        type="text"
        :rules="rules.username"
        required
      ></v-text-field>

      <v-text-field label="Senha"
        v-model="credentials.password"
        id="password"
        name="password"
        :counter="30"
        prepend-icon="lock"
        type="password"
        :rules="rules.password"
        required
      ></v-text-field>
    </v-form>
  </v-card-text>
</template>

<script>
export default {
  data() {
    return {
      credentials: {},
      rules: {
        username: [v => !!v || "Usuário é obrigatório."],
        password: [
          v => !!v || "Senha é obrigatória.",
          v => (v && v.length > 4) || "A senha deve ser maior que 4 caracteres."
        ]
    }
    }
  },
  watch: {
    credentials: {
      deep: true,
      handler() {
        this.$emit('fillCredentials', this.credentials)
      }
    }
  },
  methods: {
    touch() {
      this.$v.form.$touch()
    }
  }
}
</script>

<style>

</style>