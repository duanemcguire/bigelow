<template>
<div class="container">
  <div class="organ-spec four columns organspec">
    <h3>Opus {{organ.opus}}</h3>
    <p>{{organ.year}}</p>
    <p style="margin-bottom:0px;"><span v-for="owner of organ.owner" v-html="owner + '<BR>'"></span></p>
    <p>{{organ.location}}</p>
    <p style="margin-bottom:0px;">{{organ.manuals}} Manuals</p>
    <p style="margin-bottom:0px;">{{organ.voices}} Voices</p>
    <p>{{organ.ranks}} Ranks </p>
    <p></p>
    <p>
      <a v-if="stoplist" :href="'/opus/' + organ.opus + '-specs'">Photos</a>
      <a v-else :href="'/opus/' + organ.opus + '-stop-list'">Stop List</a>
    </p>
    <p style="padding-top 40px;">
      <nuxt-content :document="organ" />
    </p>
  </div>
  <div style=" text-align: center;">
    <div id="prevnextContainer">
      <ul class="menu">
        <span v-if="organ.prev >''">
          <li v-if="stoplist == true">
            <a :href="'/opus/' + organ.prev + '-stoplist'">
              < Opus&nbsp;{{organ.prev}}</a>
          </li>
          <li v-else>
            <a :href="'/opus/' + organ.prev + '-specs'">
              < Opus&nbsp;{{organ.prev}}</a>
          </li>
        </span>
        <span v-if="organ.next > ''">
          <li v-if="stoplist == true">
            <a :href="'/opus/' + organ.next + '-stoplist'">Opus {{organ.next}}&nbsp;></a>
          </li>
          <li v-else>
            <a :href="'/opus/' + organ.next + '-specs'">Opus {{organ.next}}&nbsp;></a>
          </li>
        </span>
      </ul>
    </div>

    <span v-if="onlyonephoto"> &nbsp; </span>
    <span v-else-if="!stoplist">Swipe to scroll through photos</span>
    <slot></slot>


  </div>
</div>
</template>
<script>
export default {
  props: {
    organ: {
      type: Object,
      required: true
    },
    stoplist: {
      type: Boolean,
      required: false
    },
    onlyonephoto: {
      type: Boolean,
      required: false,
    }
  },
  head() {
    return {
      title: 'Bigelow pipe organ specifications',
    }
  },
}
</script>
<style  >
#prevnextContainer {
  position: relative;
  top: 30px;
  left: 50px;
}

#prevnextContainer ul {
  margin-left: 0;
  margin-right: 0;
  margin-top: 0;
  margin-bottom: 10px;
  padding: 0;
  list-style-type: none;
  text-align: left;
}

#prevnextContainer ul li {
  display: inline;
}

#prevnextContainer ul li a {
  font-weight: normal;
  text-decoration: none;
  padding: .1em .5em;
  color: #fff;
  background-color: #5b5650;
}

#prevnextContainer ul li a:hover {
  color: #111;
  background-color: #ffcc66;
}


.organspec a {
  font-weight: bold;
}

.container {
  margin: 0 auto;
}

#carouselContainer {
  padding: 0 60px;
}

.VueCarousel-slide {
  position: relative;
  font-family: Arial;
  font-size: 16px;
  text-align: left;
  min-height: 100px;
}

.label {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

img {
  max-width: 600px;
  margin: 0 auto;

}

@media screen and (max-width: 1000px) {
  img {
    max-width: 450px;

  }

  #prevnextContainer {
    position: relative;
    top: 30px;
    left: 0px;
  }

}

@media screen and (max-width: 800px) {
  img {
    max-width: 200px;
  }

  #prevnextContainer {
    position: relative;
    top: 0px;
  }
}
</style>
