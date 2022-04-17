<template>
  <tbody>
    <tr v-for="row in viewData" :key="row">
      <td>{{ new Date(row[0]).toLocaleDateString() }}</td>
      <td>{{ row[1] }}</td>
      <td>{{ row[2] }}</td>
      <td>{{ row[3] }}</td>
    </tr>
    </tbody>
</template>

<script>
export default {
  props: ['viewData']
}
</script>
