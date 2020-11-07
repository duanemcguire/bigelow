<template>
<organ-spec :organ="organ">
  <div>
    <client-only>
      <div class="twelve columns">
        <carousel :per-page="1" :mouse-drag="true" :autoplay="true" :autoplay-timeout="7000" :speed="500" :loop="true" :pagination-enabled="true" :autoplay-hover-pause="false" navigation-enabled="true">
          <slide>
            <figure><img src='/images/opus/43/a.jpg'>
              <figcaption>Bigelow & Co. Opus 43 - completed in shop</figcaption>
            </figure>
          </slide>
          <slide>
            <figure><img src='/images/opus/43/b.jpg'>
              <figcaption>Bigelow & Co. Opus 43 - reconfigured case (lower pedal towers, new swell enclosure) </figcaption>
            </figure>
          </slide>
          <slide>
            <figure><img src='/images/opus/43/c.jpg'>
              <figcaption>Bigelow & Co. Opus 43 - New key desk with original keys</figcaption>
            </figure>
          </slide>
          <slide>
            <figure><img src='/images/opus/43/d.jpg'>
              <figcaption>Bigelow & Co. Opus 43 - New key desk with original keys</figcaption>
            </figure>
          </slide>
          <slide>
            <figure><img src='/images/opus/43/e.jpg'>
              <figcaption>Bigelow & Co. Opus 43 - Coupler chassis (back side of key desk)</figcaption>
            </figure>
          </slide>
          <slide>
            <figure><img src='/images/opus/43/f.jpg'>
              <figcaption>Bigelow & Co. Opus 43 - pencil drawing</figcaption>
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
