<template>
  <div class="container">
    <Filters @getParams="getParams"/>
    <hr>
    <div class="row">
      <div class="col-sm-12">
        <table class="table table-hover">
          <TableHead
            @sortByName="sortByName"
            @sortByAmount="sortByAmount"
            @sortByDistance="sortByDistance"/>
          <TableData v-bind:viewData="viewData"/>
        </table>
      </div>
    </div>
    <SwitchPage
      v-bind:isButtonPrevDisabled="isButtonPrevDisabled"
      v-bind:isButtonNextDisabled="isButtonNextDisabled"
      @prevPage="prevPage"
      @nextPage="nextPage"/>
    <hr>
  </div>
</template>

<script>
import Filters from './Filters.vue'
import SwitchPage from './SwitchPage.vue'
import TableData from './TableData.vue'
import TableHead from './TableHead.vue'
import axios from 'axios'

export default {
  components: {
    Filters, SwitchPage, TableData, TableHead
  },
  props: {
    size: {
      type: Number,
      required: false,
      default: 10
    }
  },
  data () {
    return {
      viewData: '',
      page_number: 0,
      isButtonPrevDisabled: true,
      isButtonNextDisabled: false,
      sort: {
        isSortedByName: false,
        isSortedByAmount: false,
        isSortedByDistance: false
      }
    }
  },
  methods: {
    getData () {
      const path = 'http://localhost/table'
      axios.get(path)
        .then((res) => {
          this.data = res.data
          this.viewData = res.data.slice(0, this.size)
        })
    },
    getParams (params) {
      this.column = params.column
      this.condition = params.condition
      this.value = params.value
      if (this.column && this.condition && this.value) this.filterData()
    },
    filterData () {
      let columnFilter
      this.page_number = 0
      switch (this.column) {
        case 'name':
          columnFilter = 1
          break
        case 'amount':
          columnFilter = 2
          break
        case 'distance':
          columnFilter = 3
          break
      }
      switch (this.condition) {
        case 'equals':
          this.tempData = this.data.filter(item => item[columnFilter] == this.value)
          break
        case 'contains':
          this.tempData = this.data.filter(item => item[columnFilter]
                                                    .toString().includes(this.value))
          break
        case 'more':
          this.tempData = this.data.filter(item => {
            if (typeof (item[columnFilter]) === 'string') return item[columnFilter] > this.value
            else return item[columnFilter] > parseInt(this.value)
          })
          break
        case 'less':
          this.tempData = this.data.filter(item => {
            if (typeof (item[columnFilter]) === 'string') return item[columnFilter] < this.value
            else return item[columnFilter] < parseFloat(this.value)
          })
          break
      }
      if (this.tempData.length <= this.size) this.isButtonNextDisabled = true
      else this.isButtonNextDisabled = false
      this.returnToFirstPage(this.tempData)
      this.paginatedData(this.tempData)
    },
    sortByName () {
      if (!this.tempData) this.tempData = this.data
      if (!this.sort.isSortedByName) {
        this.tempData.sort(function (a, b) {
          if (a[1] > b[1]) return 1
          else if (a[1] < b[1]) return -1
          else return 0
        })
        this.sort.isSortedByName = true
      } else {
        this.tempData.sort(function (b, a) {
          if (a[1] > b[1]) return 1
          else if (a[1] < b[1]) return -1
          else return 0
        })
        this.sort.isSortedByName = false
      }
      this.returnToFirstPage(this.tempData)
      this.paginatedData(this.tempData)
    },
    sortByAmount () {
      if (!this.tempData) this.tempData = this.data
      if (!this.sort.isSortedByAmount) {
        this.tempData.sort(function (a, b) {
          if (a[2] > b[2]) return 1
          else if (a[2] < b[2]) return -1
          else return 0
        })
        this.sort.isSortedByAmount = true
      } else {
        this.tempData.sort(function (b, a) {
          if (a[2] > b[2]) return 1
          else if (a[2] < b[2]) return -1
          else return 0
        })
        this.sort.isSortedByAmount = false
      }
      this.returnToFirstPage(this.tempData)
      this.paginatedData(this.tempData)
    },
    sortByDistance () {
      if (!this.tempData) this.tempData = this.data
      if (!this.sort.isSortedByDistance) {
        this.tempData.sort(function (a, b) {
          if (a[3] > b[3]) return 1
          else if (a[3] < b[3]) return -1
          else return 0
        })
        this.sort.isSortedByDistance = true
      } else {
        this.tempData.sort(function (b, a) {
          if (a[3] > b[3]) return 1
          else if (a[3] < b[3]) return -1
          else return 0
        })
        this.sort.isSortedByDistance = false
      }
      this.returnToFirstPage(this.tempData)
      this.paginatedData(this.tempData)
    },
    nextPage () {
      if (!this.tempData) this.tempData = this.data
      this.page_number++
      if (this.page_number >= Math.ceil(this.tempData.length / this.size) - 1) this.isButtonNextDisabled = true
      this.isButtonPrevDisabled = false
      this.paginatedData(this.tempData)
    },
    prevPage () {
      this.page_number--
      this.isButtonNextDisabled = false
      if (this.page_number === 0) this.isButtonPrevDisabled = true
      this.paginatedData(this.tempData)
    },
    paginatedData (data) {
      this.viewData = data.slice(this.page_number * this.size, (this.page_number + 1) * this.size)
    },
    returnToFirstPage (data) {
      this.page_number = 0
      if (data.length <= this.size) this.isButtonNextDisabled = true
      else this.isButtonNextDisabled = false
      this.isButtonPrevDisabled = true
    }
  },
  created () {
    this.getData()
    if (this.data.length <= this.size) this.isButtonNextDisabled = true
  }
}
</script>
