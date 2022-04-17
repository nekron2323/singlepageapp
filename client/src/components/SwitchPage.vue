<template>
  <div class="row">
     <div class="col-sm-6 text-center">
        <button @click="prevPage" class="btn" v-bind:disabled="isButtonPrevDisabled">
          Previous
        </button>
      </div>
      <div class="col-sm-6 text-center">
        <button @click="nextPage" class="btn" v-bind:disabled="isButtonNextDisabled">
          Next
        </button>
      </div>
  </div>
</template>

<script>
export default {
  props: ['isButtonPrevDisabled', 'isButtonNextDisabled'],
  methods: {
    prevPage () {
      this.$emit('prevPage')
    },
    nextPage () {
      this.$emit('nextPage')
    }
  }
}
</script>
