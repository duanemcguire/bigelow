<template>
<organ-spec :organ="organ" :stoplist=true>
  <div>
    <a :href="'/pdf/' + organ.opus + '-stop-list.pdf'">Download Stop List PDF</a>
    <embed :src="'/pdf/' + organ.opus + '-stop-list.pdf'" width="718" height="980" type='application/pdf'>
  </div>
</organ-spec>
</template>

<script>
export default {
  async asyncData({
    $content,
    params
  }) {
    const slug = params.stoplist
    var opus = slug.split('-')[0]
    const spec = opus + "-specs"
    var organ = await $content('organs', spec).fetch()
    return {
      organ
    }
  },


}
</script>
