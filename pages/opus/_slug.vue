<template>
<div class="container">
  <div class="organ-spec four columns">
    <h3>Opus {{organ.opus}}</h3>
    <p>{{organ.year}}</p>
    <p><span v-for="owner of organ.owner" v-html="owner + '<BR>'"></span></p>
    <p>{{organ.location}}</p>
    <BR />
    <p>{{organ.manuals}} Manuals</p>
    <p>{{organ.voices}} Voices</p>
    <p>{{organ.ranks}} Ranks </p>
    <BR />
    <strong><a href="/opus/24-stop-list">Stop List</a></strong>
  </div>

  <!--
  <div class="twelve columns">
    <div style="text-align: center" id="photoCaption"></div>
    <section class="spec slider">
      <div v-for="image of organ.media">
        <div>{{image.caption}}</div>
        <img v-bind:src="image.src" v-bind:alt="image.caption" />
        <div>{{image.caption_b}}</div>
      </div>
    </section>
  </div>
-->
  <div class="twelve columns">
    <client-only>
      <carousel :per-page="1" :navigation-enabled="true" :mouse-drag="true" :autoplay="true" :autoplay-timeout="7000" :speed="500" :loop="true" :pagination-enabled="true" :auto-play-hover-pause="false">
        <slide v-for="image of organ.media" :key="image.src">
          <div>{{image.caption}}</div>
          <img v-bind:src="image.src" v-bind:alt="image.caption" />
          <div>{{image.caption_b}}</div>
        </slide>
      </carousel>
    </client-only>
  </div>
</div>
</template>

<style scoped>
.organ-spec p {
  margin: 0px;
}


.VueCarousel-navigation-next {
  right: 50;
  transform: translateY(-50%) translateX(100%);
  font-family: "system";
}

.VueCarousel-navigation button {
  margin: 0px;
}

.VueCarousel-slide {
  position: relative;
  font-family: Arial;
  font-size: 14px;
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
    max-width: 500px;
  }
}

@media screen and (max-width: 800px) {
  img {
    max-width: 350px;
  }
}
</style>

<script>
export default {
  async asyncData({
    $content,
    params
  }) {
    var organ = await $content('organs', params.slug).fetch()
    return {
      organ
    }
  },
  head() {
    return {
      title: "Bigelow Organs Opus" + this.organ.opus,
      meta: [
        // hid is used as unique identifier. Do not use `vmid` for it as it will not work
        {
          hid: this.organ.slug,
          name: 'description',
          content: "Bigelow Organs Opus" + this.organ.opus + " " + this.organ.location
        }
      ]
    }
  },
}
</script>
