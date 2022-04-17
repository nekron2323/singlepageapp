<template>
  <thead>
    <tr>
      <th scope="col">Дата</th>
      <th scope="col" v-on:click="sortByName">Название</th>
      <th scope="col" v-on:click="sortByAmount">Количество</th>
      <th scope="col" v-on:click="sortByDistance">Расстояние</th>
    </tr>
  </thead>
</template>

<script>
export default {
  methods: {
    sortByName () {
      this.$emit('sortByName')
    },
    sortByAmount () {
      this.$emit('sortByAmount')
    },
    sortByDistance () {
      this.$emit('sortByDistance')
    }
  }
}
</script>
