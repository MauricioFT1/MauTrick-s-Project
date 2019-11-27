<template>
  <v-container>
    <h1>Edit Team Info</h1>
    <form>
      <v-text-field
        v-model="team.name"
        :error-messages="nameErrors"
        :counter="100"
        label="Name"
        required
        @input="$v.team.name.$touch()"
        @blur="$v.team.name.$touch()"
      ></v-text-field>
      <v-text-field
        v-model="team.coach"
        :error-messages="coachErrors"
        label="Coach"
        required
        @input="$v.team.coach.$touch()"
        @blur="$v.team.coach.$touch()"
      ></v-text-field>
      <v-text-field
        v-model="team.stadium"
        :error-messages="stadiumErrors"
        label="Stadium"
        required
        @input="$v.team.stadium.$touch()"
        @blur="$v.team.stadium.$touch()"
      ></v-text-field>
      <v-text-field
        v-model="team.foundation"
        :error-messages="foundationErrors"
        label="Foundation"
        required
        @input="$v.team.foundation.$touch()"
        @blur="$v.team.foundation.$touch()"
      ></v-text-field>
      <v-btn class="mr-4" @click="submit">Submit</v-btn>
      <v-btn @click="clear">Clear</v-btn>
    </form>
  </v-container>
</template>

<script>
import axios from "axios"
import route from "@/router/"
import { validationMixin } from 'vuelidate'

import { required, maxLength } from 'vuelidate/lib/validators'

export default {
  name: 'EditTeam',
  created () {
    this.getTeamInfo()
  },
  mixins: [validationMixin],

  validations: {
    team: {
      name: {
        maxLength: maxLength(100),
        required
      },
      stadium: {
        required
      },
      coach: {
        required
      },
      foundation: {
        required
      },
    }
  },

  data () {
    return {
      name: "",
      coach: "",
      stadium: "",
      foundation: "",
      team: {}
    }
  },
  computed: {
    nameErrors () {
      const errors = []
      if (!this.$v.team.name.$dirty) return errors
      !this.$v.team.name.maxLength && errors.push('Name must be at most 100 characters long')
      !this.$v.team.name.required && errors.push('Name is required.')
      return errors
    },
    coachErrors () {
      const errors = []
      if (!this.$v.team.coach.$dirty) return errors
      !this.$v.team.coach.required && errors.push('Coach is required')
      return errors
    },
    stadiumErrors () {
      const errors = []
      if (!this.$v.team.stadium.$dirty) return errors
      !this.$v.team.stadium.required && errors.push('Stadium is required')
      return errors
    },
    FoundationErrors () {
      const errors = []
      if (!this.$v.team.foundation.$dirty) return errors
      !this.$v.team.foundation.required && errors.push('Foundation is required')
      return errors
    },
  },
  methods: {
    getTeamInfo() {
      axios
        .request({
          baseURL: "http://127.0.0.1:8000",
          method: "get",
          url: `/api/teams/get/${this.$route.params.id}/`
        })
        .then(res => {
          this.team = res.data
          console.log(res)
        });
    },
    submit () {
      axios
        .put(
          `http://127.0.0.1:8000/api/teams/edit/${this.$route.params.id}/`,
          this.team, 
          {
            headers: {
              Authorization: `Token ${this.$session.get("token")}`
            }
          }
        )
        .then(res => {
          route.push('/teams/')
          console.log(res)
        });
    },
    clear () {
      route.push('/teams/')
    },
  }
}
</script>