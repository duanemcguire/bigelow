<template>
<organ-spec :organ="organ">
  <div>
    <client-only>
      <div class="twelve columns">
        <carousel :per-page="1" :mouse-drag="true" :speed="500" :loop="true">
          <slide>
            <figure><img src='/images/opus/7/a.jpg'>
              <figcaption>Bigelow & Co. Opus 7 - View 1</figcaption>
            </figure>
          </slide>
          <slide>
            <figure><img src='/images/opus/7/b.jpg'>
              <figcaption>Bigelow & Co. Opus 7 - View 2</figcaption>
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
