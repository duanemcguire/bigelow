<template>
<organ-spec :organ="organ">
  <div>
    <client-only>
      <div class="twelve columns">
        <carousel :per-page="1" :mouse-drag="true" :autoplay="true" :autoplay-timeout="7000" :speed="500" :loop="true" :pagination-enabled="true" :autoplay-hover-pause="false">
          <slide>
            <figure><img src='/images/opus/16/a.jpg'>
              <figcaption>Bigelow & Co. Opus 16 - View 1</figcaption>
            </figure>
          </slide>
          <slide>
            <figure><img src='/images/opus/16/b.jpg'>
              <figcaption>Bigelow & Co. Opus 16 - View 2</figcaption>
            </figure>
          </slide>
          <slide>
            <figure><img src='/images/opus/16/c.jpg'>
              <figcaption>Bigelow & Co. Opus 16 - View 3</figcaption>
            </figure>
          </slide>
          <slide>
            <figure><img src='/images/opus/16/d.jpg'>
              <figcaption>Bigelow & Co. Opus 16 - View 4</figcaption>
            </figure>
          </slide>
          <slide>
            <figure><img src='/images/opus/16/e.jpg'>
              <figcaption>Bigelow & Co. Opus 16 - View 5</figcaption>
            </figure>
          </slide>
          <slide>
            <figure><img src='/images/opus/16/f.jpg'>
              <figcaption>Bigelow & Co. Opus 16 - View 6</figcaption>
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
