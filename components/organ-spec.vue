<template>
<div class="container">
  <div class="organ-spec four columns">
    <h3>Opus {{organ.opus}}</h3>
    <p>{{organ.year}}</p>
    <p><span v-for="owner of organ.owner" v-html="owner + '<BR>'"></span></p>
    <p>{{organ.location}}</p>
    <p></p>
    <p>{{organ.manuals}} Manuals</p>
    <p>{{organ.voices}} Voices</p>
    <p>{{organ.ranks}} Ranks </p>
    <p></p>
    <a href="#">Stop List</a>
  </div>
  <slot></slot>
</div>
</template>
<script>
export default {
  props: {
    organ: {
      type: Object,
      required: true
    }
  }
}
</script>
<style >
.container {
  margin: 0 auto;
}

#carouselContainer {
  padding: 0 60px;
}

.VueCarousel-slide {
  position: relative;
  font-family: Arial;
  font-size: 24px;
  text-align: center;
  min-height: 100px;
}

.label {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

img {
  max-width: 600px;
  margin: 0 auto;

}

@media screen and (max-width: 1000px) {
  img {
    max-width: 450px;
  }
}

@media screen and (max-width: 800px) {
  img {
    max-width: 200px;
  }
}
</style>
