<template>
<organ-spec :organ="organ">
  <div>
    <client-only>
      <div class="twelve columns">
        <carousel :per-page="1" :mouse-drag="true" :autoplay="true" :autoplay-timeout="7000" :speed="500" :loop="true" :pagination-enabled="true" :autoplay-hover-pause="false">
          <slide>
            <figure><img src='/images/opus/38/a.jpg'>
              <figcaption>Bigelow & Company Organ Builders - Opus 38 - Photo by Heidi Jensen</figcaption>
            </figure>
          </slide>
          <slide>
            <figure><img src='/images/opus/38/b.jpg'>
              <figcaption>Bigelow & Company Organ Builders - Opus 38 - Photograph dated 1915</figcaption>
            </figure>
          </slide>
          <slide>
            <figure><img src='/images/opus/38/c.jpg'>
              <figcaption>Bigelow & Company Organ Builders - Opus 38 - Photo by Heidi Jensen</figcaption>
            </figure>
          </slide>
          <slide>
            <figure><img src='/images/opus/38/d.jpg'>
              <figcaption>Bigelow & Company Organ Builders - Opus 38 - Photo by Heidi Jensen</figcaption>
            </figure>
          </slide>
          <slide>
            <figure><img src='/images/opus/38/e.jpg'>
              <figcaption>Bigelow & Company Organ Builders - Opus 38 - Photo by Heidi Jensen</figcaption>
            </figure>
          </slide>
          <slide>
            <figure><img src='/images/opus/38/f.jpg'>
              <figcaption>Bigelow & Company Organ Builders - Opus 38 - Photo by Heidi Jensen</figcaption>
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
