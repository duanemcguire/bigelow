<template>
<div class="carousel-wrapper">
  <VueSlickCarousel v-bind="slickOptions">
    <div><img src="/images/shop.jpg"></div>
    <div><img src="/images/shop-window.jpg"></div>
    <div><img src="/images/opus/37/a.jpg"></div>
    <div><img src="/images/opus/37/c.jpg"></div>
    <div><img src="/images/opus/42/c.jpg"></div>
  </VueSlickCarousel>
</div>
</template>

<script>
export default {
  data() {
    return {
      slickOptions: {
        slidesToShow: 3,
        arrows: false
      }
    }
  }
}
</script>

<style>
.carousel-wrapper {
  padding: 40px;
}

.img-wrapper img {
  margin: auto;
  width: 200px;
  height: 100px;
  background-image: linear-gradient(gray 100%, transparent 0);
}
</style>
