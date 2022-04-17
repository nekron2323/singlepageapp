<template>
    <div class="conteiner">
        <div class="row">
            <div class="col-sm-4">
                <select v-model="column" @change="setParams">
                    <option value="name">Название</option>
                    <option value="amount">Количество</option>
                    <option value="distance">Расстояние</option>
                </select>
            </div>
            <div class="col-sm-4">
                <select v-model="condition" @change="setParams">
                    <option value="equals">Равно</option>
                    <option value="contains">Содержит</option>
                    <option value="more">Больше</option>
                    <option value="less">Меньше</option>
                </select>
            </div>
            <div class="col-sm-4">
                <input v-model="value" @change="setParams" placeholder="Значение">
            </div>
        </div>
</div>
</template>

<script>
export default {
  methods: {
    setParams () {
      this.$emit('getParams', {
        column: this.column,
        condition: this.condition,
        value: this.value
      })
    }
  }
}
</script>
