<template>
<div>
  <div class="organ-spec four columns">
    <h3>Opus {{organ.opus}}</h3>
    <p>{{organ.year}}</p>
    <p><span v-for="owner of organ.owner">{{owner}}<BR /></span></p>
    <p>{{organ.location}}</p>
    <BR />
    <p>{{organ.manuals}} Manuals</p>
    <p>{{organ.voices}} Voices</p>
    <p>{{organ.ranks}} Ranks </p>
    <BR />
    <strong><a href="/opus/24-stop-list">Stop List</a></strong>
  </div>
  <div class="twelve columns">
    <div style="text-align: center" id="photoCaption"></div>
    <section class="spec slider">
      <div v-for="image of organ.media">
        <div>{{image.caption}}</div>
        <img v-bind:src="image.src" v-bind:alt="image.caption" />
        <div>{{image.caption_b}}</div>
      </div>
    </section>

  </div>

</div>
</template>
<style>
.organ-spec p {
  margin: 0px;
}
</style>
<script>
export default {
  async asyncData({
    $content,
    params
  }) {
    var organ = await $content('organs', params.slug).fetch()
    return {
      organ
    }
  },
  head() {
    return {
      title: "Bigelow Organs Opus" + this.organ.opus,
      meta: [
        // hid is used as unique identifier. Do not use `vmid` for it as it will not work
        {
          hid: this.organ.slug,
          name: 'description',
          content: "Bigelow Organs Opus" + this.organ.opus + " " + this.organ.location
        }
      ]
    }
  },
}
</script>
