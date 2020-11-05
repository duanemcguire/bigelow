<template>
<div class="container">
  <div class="row">
    <div class="four columns">
      <h1>Bigelow Organs</h1>
      <p>We specialize in building solid, reliable tracker instruments that excel in musical, architectural, and tactile qualities. That's what we've been doing since 1978!</p>
      <p>Please email us at <a href="mailto:mail@bigeloworgans.com">mail@bigeloworgans.com</a><BR />
        See us also on <a href="http://www.facebook.com/pages/Bigelow-Co-Inc-Organ-Builders/122521624517257?sk=wall">Facebook</a>.
      </p>

      <p><BR />
        Featured in the slide show at right:
      <ul>
        <li>Our shop (historic church)</li>
        <li><a href="/opus/37-specs">1859 Robjohn</a></li>
        <li><a href="/opus/42-specs">Opus 42</a> - recent installation</li>
      </ul>
      </p>

    </div>
    <div class="twelve columns">
      <client-only>
        <carousel :per-page="1" :mouse-drag="true" :autoplay="true" :autoplay-timeout="7000" :speed="500" :loop="true" :pagination-enabled="true" :auto-play-hover-pause="false">
          <slide>
            <figure>
              <img src="/images/shop.jpg">
              <figcaption>Our shop (historic church)</figcaption>
            </figure>
          </slide>
          <slide>
            <figure>
              <img src="/images/shop-window.jpg">
              <figcaption>Shop window</figcaption>
            </figure>
          </slide>
          <slide>
            <figure>
              <img src="/images/opus/37/a.jpg">
              <figcaption>1859 Robjohn</figcaption>
            </figure>
          </slide>
          <slide>
            <figure>
              <img src="/images/opus/37/c.jpg">
              <figcaption>1859 Robjohn</figcaption>
            </figure>
          </slide>
          <slide>
            <figure>
              <img src="/images/opus/42/c.jpg">
              <figcaption>Opus 42 - recent installation</figcaption>
            </figure>
          </slide>
        </carousel>
      </client-only>
    </div>
  </div>
</div>
</template>

<script>
export default {

  head() {
    return {
      title: 'Bigelow Organs',
      meta: [
        // hid is used as unique identifier. Do not use `vmid` for it as it will not work
        {
          hid: 'blog-index',
          name: 'description',
          content: 'Bigelow Organs: building solid, reliable tracker pipe organs since 1979 '
        }
      ]
    }
  },
}
</script>


<style scoped>
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

@media screen and (max-width: 800px) {
  img {
    max-width: 320px;
  }
}
</style>
