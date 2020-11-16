<template>
<organ-spec :organ="organ">
  <div>
    <client-only>
      <div class="twelve columns">
        <carousel :per-page="1" :mouse-drag="true" :autoplay="true" :autoplay-timeout="7000" :speed="500" :loop="true" :pagination-enabled="true" :autoplay-hover-pause="false">
          <slide>
            <figure><img src="/images/opus/26/a.jpg" alt="Bigelow &amp; Co. Opus 26 - Photo by James Richardson">
              <figcaption>
                Bigelow & Co. Opus 26 - Photo by James Richardson<BR />
                <a target="hi-res" href="/hi-res.html?/images/opus/26/hi-res/a.jpg" title="Click to see larger image">View Larger Photo</a>
              </figcaption>
            </figure>
          </slide>
          <slide>
            <figure><img src="/images/opus/26/b.jpg" alt="Bigelow &amp; Co. Opus 26 - Photo by James Richardson">
              <figcaption>
                Bigelow & Co. Opus 26 - Photo by James Richardson<BR />
                <a target="hi-res" href="/hi-res.html?/images/opus/26/hi-res/b.jpg" title="Click to see larger image">View Larger Photo</a>
              </figcaption>
            </figure>
          </slide>
          <slide>
            <figure><img src="/images/opus/26/c.jpg" alt="Bigelow &amp; Co. Opus 26 - Photo by James Richardson">
              <figcaption>
                Bigelow & Co. Opus 26 - Photo by James Richardson<BR />
                <a target="hi-res" href="/hi-res.html?/images/opus/26/hi-res/c.jpg" title="Click to see larger image">View Larger Photo</a>
              </figcaption>
            </figure>
          </slide>
          <slide>
            <figure><img src="/images/opus/26/d.jpg" alt="Bigelow &amp; Co. Opus 26 - Photo by James Richardson">
              <figcaption>
                Bigelow & Co. Opus 26 - Photo by James Richardson<BR />
                <a target="hi-res" href="/hi-res.html?/images/opus/26/hi-res/d.jpg" title="Click to see larger image">View Larger Photo</a>
              </figcaption>
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
    var organs = await $content('organs')
      .only(['opus'])
      .sortBy('opus', 'desc')
      .fetch()
    var path = route.path
    var slug = path.split('/')[2]
    var organ = await $content('organs', slug).fetch()
    organ.prev = organ.opus - 1
    organ.next = organ.opus + 1
    if (organ.opus == 1) organ.prev = ''
    if (organ.opus == organs[0].opus) organ.next = ''
    return {
      organ
    }
  },
}
</script>
