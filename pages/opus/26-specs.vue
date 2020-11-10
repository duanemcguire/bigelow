<template>
<organ-spec :organ="organ">
  <div>
    <client-only>
      <div class="twelve columns">
        <carousel :per-page="1" :mouse-drag="true" :autoplay="true" :autoplay-timeout="7000" :speed="500" :loop="true" :pagination-enabled="true" :autoplay-hover-pause="false">
          <slide>
            <figure><a href="/images/opus/26/hi-res/a.jpg" title="Click to see larger image"><img src="/images/opus/26/a.jpg" alt="Bigelow &amp; Co. Opus 26 - Photo by James Richardson"></a>
              <figcaption>Bigelow & Co. Opus 26 - Photo by James Richardson</figcaption>
            </figure>
          </slide>
          <slide>
            <figure><a href="/images/opus/26/hi-res/b.jpg" title="Click to see larger image"><img src="/images/opus/26/b.jpg" alt="Bigelow &amp; Co. Opus 26 - Photo by James Richardson"></a>
              <figcaption>Bigelow & Co. Opus 26 - Photo by James Richardson</figcaption>
            </figure>
          </slide>
          <slide>
            <figure><a href="/images/opus/26/hi-res/c.jpg" title="Click to see larger image"><img src="/images/opus/26/c.jpg" alt="Bigelow &amp; Co. Opus 26 - Photo by James Richardson"></a>
              <figcaption>Bigelow & Co. Opus 26 - Photo by James Richardson</figcaption>
            </figure>
          </slide>
          <slide>
            <figure><a href="/images/opus/26/hi-res/d.jpg" title="Click to see larger image"><img src="/images/opus/26/d.jpg" alt="Bigelow &amp; Co. Opus 26 - Photo by James Richardson"></a>
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
