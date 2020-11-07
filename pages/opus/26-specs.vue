<template>
<organ-spec :organ="organ">
  <div>
    <client-only>
      <div class="twelve columns">
        <carousel :per-page="1" :mouse-drag="true" :autoplay="true" :autoplay-timeout="7000" :speed="500" :loop="true" :pagination-enabled="true" :autoplay-hover-pause="false" navigation-enabled="true">
          <slide>
            <figure><img src='/images/opus/26/a.jpg'>
              <figcaption>Bigelow & Co. Opus 26 - Photo by James Richardson</figcaption>
            </figure>
          </slide>
          <slide>
            <figure><img src='/images/opus/26/b.jpg'>
              <figcaption>Bigelow & Co. Opus 26 - Photo by James Richardson</figcaption>
            </figure>
          </slide>
          <slide>
            <figure><img src='/images/opus/26/c.jpg'>
              <figcaption>Bigelow & Co. Opus 26 - Photo by James Richardson</figcaption>
            </figure>
          </slide>
          <slide>
            <figure><img src='/images/opus/26/d.jpg'>
              <figcaption>Bigelow & Co. Opus 26 - Photo by James Richardson</figcaption>
            </figure>
          </slide>
        </carousel>
      </div>
    </client-only>
  </div>
</organ-spec>
</template>
<script>
export default {
  async asyncData({
    $content,
    route
  }) {
    var path = route.path
    var slug = path.split('/')[2]
    var organ = await $content('organs', slug).fetch()
    return {
      organ
    }
  },
}
</script>
