<template>
  
</template>

<script>
import axios from 'axios'
import router from "../router"

export default {
  created () {
    if (this.$session.has('token')) {
      axios
        .post("http://localhost:8000/auth/token/logout/", null,
          {
            headers: {
              Authorization: `Token ${this.$session.get("token")}`
            }
          }
        )
        .then(res => {
          this.$session.remove("token")
          this.$session.destroy()
          router.push("/")
        })
        .catch(e => {
          this.errorShow = true
          console.log(e)
        });
    }
  }
}
</script>

<style>

</style>