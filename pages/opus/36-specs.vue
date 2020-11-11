<template>
<organ-spec :organ="organ">
  <div>
    <client-only>
      <div class="twelve columns">
        <carousel :per-page="1" :mouse-drag="true" :autoplay="true" :autoplay-timeout="7000" :speed="500" :loop="true" :pagination-enabled="true" :autoplay-hover-pause="false">
          <slide>
            <figure><img src='/images/opus/36/a.jpg'>
              <figcaption></figcaption>
            </figure>
          </slide>
          <slide>
            <figure><img src='/images/opus/36/b.jpg'>
              <figcaption></figcaption>
            </figure>
          </slide>
          <slide>
            <figure><img src='/images/opus/36/c.jpg'>
              <figcaption></figcaption>
            </figure>
          </slide>
          <slide>
            <figure><img src='/images/opus/36/d.jpg'>
              <figcaption></figcaption>
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
