<template>
<organ-spec :organ="organ">
  <div>
    <client-only>
      <div class="twelve columns">
        <carousel :per-page="1" :mouse-drag="true" :autoplay="true" :autoplay-timeout="7000" :speed="500" :loop="true" :pagination-enabled="true" :autoplay-hover-pause="false" navigation-enabled="true">
          <slide>
            <figure><img src='/images/opus/34/a.jpg'>
              <figcaption>Bigelow & Co. Opus 34 - At home in the music room</figcaption>
            </figure>
          </slide>
          <slide>
            <figure><img src='/images/opus/34/b.jpg'>
              <figcaption>Bigelow & Co. Opus 34 - At home in the music room (2)</figcaption>
            </figure>
          </slide>
          <slide>
            <figure><img src='/images/opus/34/c.jpg'>
              <figcaption>Bigelow & Co. Opus 34 - View 3</figcaption>
            </figure>
          </slide>
          <slide>
            <figure><img src='/images/opus/34/d.jpg'>
              <figcaption>Bigelow & Co. Opus 34 - View 4</figcaption>
            </figure>
          </slide>
          <slide>
            <figure><img src='/images/opus/34/e.jpg'>
              <figcaption>Bigelow & Co. Opus 34 - a look inside</figcaption>
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
