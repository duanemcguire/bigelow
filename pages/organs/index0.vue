<template>
<div class="container">
  <div id="opuslistmobile">
    <div style="border: 1px solid black; max-width: 250px; margin-bottom: 5px;" v-for="organ of organs" :key="organs.opus" :onclick="'location.href=\'/opus/' + organ.slug + '\''">
      <a :href="'/opus/' + organ.slug">
        <img v-bind:src="'/images/opus/' + organ.opus + '/thumb.jpg'" /><BR />
      </a>
      Opus {{organ.opus}}<BR />
      {{organ.year}}<BR />
      <span v-for="owner of organ.owner" v-html="owner + '<BR/>'"></span>
      {{organ.location}}

    </div>
  </div>
</div>
</template>

<script>
export default {

  async asyncData({
    $content,
    params
  }) {
    var organs = await $content('organs')
      .sortBy('opus', 'desc')
      .fetch()


    return {
      organs
    }
  },
  head() {
    return {
      title: 'Bigelow Organs - Opus List',
      meta: [
        // hid is used as unique identifier. Do not use `vmid` for it as it will not work
        {
          hid: 'blog-index',
          name: 'description',
          content: 'Tracker pipe organs produced by Bigelow Organs from 1979 to present'
        }
      ]
    }
  },
}
</script>
