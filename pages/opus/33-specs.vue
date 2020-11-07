<template>
<organ-spec :organ="organ">
  <div>
    <client-only>
      <div class="twelve columns">
        <carousel :per-page="1" :mouse-drag="true" :autoplay="true" :autoplay-timeout="7000" :speed="500" :loop="true" :pagination-enabled="true" :autoplay-hover-pause="false" >
          <slide>
            <figure><img src='/images/opus/33/a.jpg'>
              <figcaption>Bigelow & Co. Opus 33 - View 1</figcaption>
            </figure>
          </slide>
          <slide>
            <figure><img src='/images/opus/33/b.jpg'>
              <figcaption>Bigelow & Co. Opus 33 - View 2</figcaption>
            </figure>
          </slide>
          <slide>
            <figure><img src='/images/opus/33/c.jpg'>
              <figcaption>Bigelow & Co. Opus 33 - View 3</figcaption>
            </figure>
          </slide>
          <slide>
            <figure><img src='/images/opus/33/d.jpg'>
              <figcaption>Bigelow & Co. Opus 33 - keydesk</figcaption>
            </figure>
          </slide>
          <slide>
            <figure><img src='/images/opus/33/e.jpg'>
              <figcaption>Bigelow & Co. Opus 33 - keydesk</figcaption>
            </figure>
          </slide>
          <slide>
            <figure><img src='/images/opus/33/f.jpg'>
              <figcaption>Bigelow & Co. Opus 33 - keydesk with video monitors deployed</figcaption>
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
