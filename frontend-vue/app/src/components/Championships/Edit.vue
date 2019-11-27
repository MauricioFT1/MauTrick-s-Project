<template>
  <v-container>
    <h1>Edit Championship Info</h1>
    <form>
      <v-text-field
        v-model="championship.name"
        :error-messages="nameErrors"
        :counter="100"
        label="Name"
        required
        @input="$v.championship.name.$touch()"
        @blur="$v.championship.name.$touch()"
      ></v-text-field>
      <v-text-field
        v-model="championship.description"
        :error-messages="descriptionErrors"
        label="Description"
        required
        @input="$v.championship.description.$touch()"
        @blur="$v.championship.description.$touch()"
      ></v-text-field>
      <v-text-field
        v-model="championship.role"
        :error-messages="roleErrors"
        label="Role"
        required
        @input="$v.championship.role.$touch()"
        @blur="$v.championship.role.$touch()"
      ></v-text-field>
      <v-text-field
        v-model="championship.created"
        :error-messages="createdErrors"
        label="Created"
        required
        @input="$v.championship.created.$touch()"
        @blur="$v.championship.created.$touch()"
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
  name: 'EditChampionship',
  created () {
    this.getChampionshipInfo()
  },
  mixins: [validationMixin],

  validations: {
    championship: {
      name: {
        maxLength: maxLength(100),
        required
      },
      description: {
        required
      },
      role: {
        required
      },
      created: {
        required
      },
    }
  },

  data () {
    return {
      name: "",
      role: "",
      description: "",
      created: "",
      championship: {}
    }
  },
  computed: {
    nameErrors () {
      const errors = []
      if (!this.$v.championship.name.$dirty) return errors
      !this.$v.championship.name.maxLength && errors.push('Name must be at most 100 characters long')
      !this.$v.championship.name.required && errors.push('Name is required.')
      return errors
    },
    roleErrors () {
      const errors = []
      if (!this.$v.championship.role.$dirty) return errors
      !this.$v.championship.role.required && errors.push('Role is required')
      return errors
    },
    createdErrors () {
      const errors = []
      if (!this.$v.championship.created.$dirty) return errors
      !this.$v.championship.created.required && errors.push('Created is required')
      return errors
    },
    descriptionErrors () {
      const errors = []
      if (!this.$v.championship.description.$dirty) return errors
      !this.$v.championship.description.required && errors.push('Description is required')
      return errors
    },
  },
  methods: {
    getChampionshipInfo() {
      axios
        .request({
          baseURL: "http://localhost:8000",
          method: "get",
          url: `/api/championships/get/${this.$route.params.id}/`
        })
        .then(res => {
          this.championship = res.data
          console.log(res)
        });
    },
    submit () {
      axios
        .put(
          `http://localhost:8000/api/championships/edit/${this.$route.params.id}/`,
          this.championship, 
          {
            headers: {
              Authorization: `Token ${this.$session.get("token")}`
            }
          }
        )
        .then(res => {
          route.push('/championships/')
          console.log(res)
        });
    },
    clear () {
      route.push('/championships/')
    },
  }
}
</script>