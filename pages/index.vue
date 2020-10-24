<template>
<div class="container">
  <div class="row">
    <div class="four columns">
      <h1>Bigelow Organs</h1>
      <p>We specialize in building solid, reliable tracker instruments that excel in musical, architectural, and tactile qualities. That's what we've been doing since 1978!</p>
      <p>Please email us at <a href="mailto:mail@bigeloworgans.com">mail@bigeloworgans.com</a><BR />
        See us also on <a href="http://www.facebook.com/pages/Bigelow-Co-Inc-Organ-Builders/122521624517257?sk=wall">Facebook</a>.
      </p>

      <p><BR />
        Featured in the slide show at right:
      <ul>
        <li>Our shop (historic church)</li>
        <li><a href="/opus/37-specs">1859 Robjohn</a></li>
        <li><a href="/opus/42-specs">Opus 42</a> - recent installation</li>
      </ul>
      </p>

    </div>
    <div class="twelve columns">

      <div><img src="/images/shop.jpg"></div>
      <div><img src="/images/shop-window.jpg"></div>
      <div><img src="/images/opus/37/a.jpg"></div>
      <div><img src="/images/opus/37/c.jpg"></div>
      <div><img src="/images/opus/42/c.jpg"></div>

    </div>
  </div>
</div>
</template>

<script>
export default {

  head() {
    return {
      title: 'Bigelow Organs',
      meta: [
        // hid is used as unique identifier. Do not use `vmid` for it as it will not work
        {
          hid: 'blog-index',
          name: 'description',
          content: 'Bigelow Organs: building solid, reliable tracker pipe organs ins 1979 '
        }
      ]
    }
  },
}
</script>

<style>
.container {
  margin: 0 auto;
}
</style>
