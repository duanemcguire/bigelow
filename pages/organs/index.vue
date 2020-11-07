<template>
<div class="container">
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
      <tr v-for="organ of organs" :key="organs.opus" :onclick="'location.href=\'/opus/' + organ.slug + '\''">
        <td class="image">
          <a :href="'/opus/' + organ.slug">
            <img v-bind:src="'/images/opus/' + organ.opus + '/thumb.jpg'" />
          </a>
        </td>
        <td class="opus">{{organ.opus}}</td>
        <td class="year">{{organ.year}}</td>
        <td class="owner"><span v-for="owner of organ.owner" v-html="owner + '<BR/>'"></span></td>
        <td class=" location">{{organ.location}}</td>
        <td class="manuals">{{organ.manuals}}</td>
        <td class="voices">{{organ.voices}}</td>
        <td class="ranks">{{organ.ranks}}</td>
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
