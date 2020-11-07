<template>
<organ-spec :organ="organ">
  <div>
    <client-only>
      <div class="twelve columns">
        <carousel :per-page="1" :mouse-drag="true" :autoplay="true" :autoplay-timeout="7000" :speed="500" :loop="true" :pagination-enabled="true" :autoplay-hover-pause="false" navigation-enabled="true">
          <slide>
            <figure><img src='/images/opus/30/a.jpg'>
              <figcaption>Bigelow & Co. Opus 30 - View from front of church1</figcaption>
            </figure>
          </slide>
          <slide>
            <figure><img src='/images/opus/30/b.jpg'>
              <figcaption>Bigelow & Co. Opus 30 - View of keydesk built into back of case</figcaption>
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
