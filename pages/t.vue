<template>
<div>
  <Carousel>
    <Slide>HI</SLIDE>
    <Slide>There</SLIDE>

  </Carousel>
</div>
</template>

<script>
import Vue from 'vue'
import {
  Carosel,
  Slide
} from 'vue-carousel'
Vue.component('carousel', Carousel)
Vue.component('slide', Slide)

export default {}
</script>
