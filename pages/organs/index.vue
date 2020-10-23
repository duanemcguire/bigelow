<template>
<div>
  <Table id="opusList">
    <colgroup>
      <col style="width: 120px;">
      <col style="width: 60px;">
      <col style="width: 50px;">
      <col style="width: 200px;">
      <col style="width: 150px;">
      <col style="width: 70px;">
      <col style="width: 60px;">
      <col style="width: 60px;">
    </colgroup>
    <tbody>
      <tr class="head">
        <td class="image">Image</td>
        <td class="opus">Opus</td>
        <td class="year">Year</td>
        <td class="owner">Owner</td>
        <td class="location">Location</td>
        <td class="manuals">Manuals</td>
        <td class="voices">Voices</td>
        <td class="ranks">Ranks</td>
      </tr>
      <tr v-for="organ of organs" :key="organs.opus">
        <td><img v-bind:src="'/images/opus/' + organ.opus + '/thumb.jpg'" /></td>
        <td>{{organ.opus}}</td>
        <td>{{organ.year}}</td>
        <td><span v-for="owner of organ.owner">{{owner}}<BR /></span></td>
        <td>{{organ.location}}</td>
        <td>{{organ.manuals}}</td>
        <td>{{organ.voices}}</td>
        <td>{{organ.ranks}}</td>
      </tr>
    </tbody>
  </table>

</div>
</template>

<script>
export default {

  async asyncData({
    $content,
    params
  }) {
    var organs = await $content('organs', {
        text: true
      })
      .sortBy('opus', 'desc')
      .fetch()


    return {
      organs
    }
  },
  head() {
    return {
      title: 'Blog - McGuire Piano',
      meta: [
        // hid is used as unique identifier. Do not use `vmid` for it as it will not work
        {
          hid: 'blog-index',
          name: 'description',
          content: 'Collection of blog posts about piano rebuilding and restoration'
        }
      ]
    }
  },
}
</script>
