<template>
  <v-alert
      :dismissible=true
      :type="msg_type"
      class="mb-4"
  >
    <slot></slot>
  </v-alert>
</template>

<script>
export default {
  props: {
    msg_type: {
      type: String,
      default: 'error'
    }
  }
}
</script>

<style>

</style>