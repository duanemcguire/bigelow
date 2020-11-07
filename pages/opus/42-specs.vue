<template>
<organ-spec :organ="organ">
  <div>
    <client-only>
      <div class="twelve columns">
        <carousel :per-page="1" :mouse-drag="true" :speed="500" :loop="true">
          <slide>
            <figure><img src="/images/opus/42/a.jpg" alt="Bigelow &amp; Co. Opus 42 - View 1" />
              <figcaption>Bigelow &amp; Co. Opus 42 - View 1</figcaption>
            </figure>
          </slide>
          <slide>
            <figure><img src="/images/opus/42/b.jpg" alt="Previous organ - View 2, before">
              <figcaption>Previous organ - View 2, before</figcaption>
            </figure>
          </slide>
          <slide>
            <figure><img src="/images/opus/42/c.jpg" alt="Bigelow &amp; Co. Opus 42 - View 2, after">
              <figcaption>Bigelow &amp; Co. Opus 42 - View 2, after</figcaption>
            </figure>
          </slide>
          <slide>
            <figure><img src="/images/opus/42/d.jpg" alt="Previous organ - View 3 (from the nave), before">
              <figcaption>Previous organ - View 3 (from the nave), before</figcaption>
            </figure>
          </slide>
          <slide>
            <figure><img src="/images/opus/42/e.jpg" alt="Bigelow &amp; Co. Opus 42 - View 3 (from the nave), after">
              <figcaption>Bigelow &amp; Co. Opus 42 - View 3 (from the nave), after</figcaption>
            </figure>
          </slide>
          <slide>
            <figure><img src="/images/opus/42/f.jpg" alt="Bigelow &amp; Co. Opus 42 - View 4">
              <figcaption>Bigelow &amp; Co. Opus 42 - View 4</figcaption>
            </figure>
          </slide>
          <slide>
            <figure><img src="/images/opus/42/g.jpg" alt="Bigelow &amp; Co. Opus 42 - View 5">
              <figcaption>Bigelow &amp; Co. Opus 42 - View 5</figcaption>
            </figure>
          </slide>
          <slide>
            <figure><img src="/images/opus/42/h.jpg" alt="Bigelow &amp; Co. Opus 42 - C#-side flat">
              <figcaption>Bigelow &amp; Co. Opus 42 - C#-side flat</figcaption>
            </figure>
          </slide>
          <slide>
            <figure><img src="/images/opus/42/i.jpg" alt="Bigelow &amp; Co. Opus 42 - keydesk">
              <figcaption>Bigelow &amp; Co. Opus 42 - keydesk</figcaption>
            </figure>
          </slide>
          <slide>
            <figure><img src="/images/opus/42/j.jpg" alt="Bigelow &amp; Co. Opus 42 - name board">
              <figcaption>Bigelow &amp; Co. Opus 42 - name board</figcaption>
            </figure>
          </slide>
          <slide>
            <figure><img src="/images/opus/42/k.jpg" alt="Bigelow &amp; Co. Opus 42 - left stop jamb">
              <figcaption>Bigelow &amp; Co. Opus 42 - left stop jamb</figcaption>
            </figure>
          </slide>
          <slide>
            <figure><img src="/images/opus/42/l.jpg" alt="Bigelow &amp; Co. Opus 42 - right stop jamb">
              <figcaption>Bigelow &amp; Co. Opus 42 - right stop jamb</figcaption>
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
