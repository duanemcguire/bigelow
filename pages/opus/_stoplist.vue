<template>
<organ-spec :organ="organ" :stoplist=true>
  <BR />
  <div>
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
    var organs = await $content('organs')
      .only(['opus'])
      .sortBy('opus', 'desc')
      .fetch()
    var organ = await $content('organs', spec).fetch()
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
