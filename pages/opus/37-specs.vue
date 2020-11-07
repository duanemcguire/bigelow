<template>
<organ-spec :organ="organ">
  <div>
    <client-only>
      <div class="twelve columns">
        <carousel :per-page="1" :mouse-drag="true" :speed="500" :loop="true">
          <slide>
            <figure><img src='/images/opus/37/a.jpg'>
              <figcaption>Opus 37 - 1859 Thomas Robjohn - View 1</figcaption>
            </figure>
          </slide>
          <slide>
            <figure><img src='/images/opus/37/b.jpg'>
              <figcaption>Opus 37 - 1859 Thomas Robjohn - courtesy of MIM</figcaption>
            </figure>
          </slide>
          <slide>
            <figure><img src='/images/opus/37/c.jpg'>
              <figcaption>Opus 37 - 1859 Thomas Robjohn - keydesk</figcaption>
            </figure>
          </slide>
          <slide>
            <figure><img src='/images/opus/37/d.jpg'>
              <figcaption>Opus 37 - 1859 Thomas Robjohn - Name plate</figcaption>
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
