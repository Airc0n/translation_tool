<script>
import Mustache from "mustache";
import VJsoneditor from "v-jsoneditor/src/index";

export default {
  name: "HTMLGenerator",
  components: {
    VJsoneditor,
  },
  data() {
    return {};
  },
  mounted() {
    this.$store.dispatch("getHtmlTemplates");
  },
  computed: {
    templates() {
      return this.$store.getters.getTemplates;
    },
    getResources() {
      return this.$store.getters.getResources;
    },
    selectedTemplateId: {
      get() {
        return this.$store.state.selected_template_id;
      },
      set(tid) {
        this.$store.commit("selectTemplate", tid);
      },
    },
    selectedTemplate() {
      return this.$store.getters.getTemplateById(this.selectedTemplateId);
    },
  },
  methods: {
    onError() {
      // this method is for VJsoneditor
      console.log("error");
    },
    templateChangeHandler() {
      this.$store.dispatch("getResources", this.selectedTemplateId);
      if (this.selectedTemplateId) {
        this.selected_template = this.$store.getters.getTemplateById(
          this.selectedTemplateId
        );
      }
    },
    render_html(data) {
      if (this.selectedTemplateId) {
        let html = this.selectedTemplate.html;
        return Mustache.render(html, data);
      }
    },
    previewTemplate(rid) {
      console.log(rid);
    },
    copyToClipboard(str) {
      const el = document.createElement("textarea");
      el.value = str;
      document.body.appendChild(el);
      el.select();
      document.execCommand("copy");
      document.body.removeChild(el);
    },
    copyHTML(resource) {
      let html = this.render_html(resource.data);
      this.copyToClipboard(html);
      this.$notify({
        group: "html-generator",
        text: "Copy HTML successful!",
      });
    },
  },
};
</script>

<template>
  <div class="html-generator-block">
    <h1>HTML Generator</h1>
    <notifications group="html-generator" position="top center"/>
    <hr />
    <h2 class="sub-headline">STEP 1. Select A Template</h2>
    <div class="form-group row">
      <label for="templateSelection" class="col-sm-2 col-form-label">Template</label>
      <div class="col-sm-10">
        <select
          id="templateSelection"
          class="form-control form-control-lg"
          @change="templateChangeHandler"
          v-model="selectedTemplateId"
        >
          <option value="null">Plese select a template</option>
          <option
            v-for="template in templates"
            :value="template.id"
            :key="template.id"
          >{{template.name}}</option>
        </select>
      </div>
    </div>

    <pre class="text-left" v-if="selectedTemplate">{{ selectedTemplate.html }}</pre>

    <h2 v-if="selectedTemplateId" class="sub-headline">STEP 2. Select Locale You Want</h2>

    <div class="card" v-for="(res, rid) in getResources" :key="res.id">
      <a
        href="###"
        data-toggle="collapse"
        aria-expanded="true"
        :aria-controls="'#collapse_'+res.locale"
        :data-target="'#collapse_'+res.locale"
      >
        <div class="card-header" :id="'heading_'+res.locale">
          <h4 class="mb-0">{{ res.locale }}</h4>
          <div>Last modifed @{{ res.modified_at }} by {{ res.modified_by }}</div>
        </div>
      </a>

      <div class="collapse" :id="'collapse_'+res.locale" :aria-labelledby="'heading_'+res.locale">
        <div class="text-right">
          <button @click="previewTemplate(rid)">Preview</button>
          <button @click="copyHTML(res)">CopyHTML</button>
        </div>

        <div class="card-body">
          <div class="row mt-5">
            <div class="col-md-6">
              <h5>JSON</h5>
              <v-jsoneditor v-model="res.data" @error="onError"></v-jsoneditor>
            </div>
            <div class="col-md-6">
              <h5>HTML</h5>
              <pre class="text-left">{{ render_html(res.data)}}</pre>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
* {
  font-family: Consolas, "Andale Mono WT", "Andale Mono", "Lucida Console",
    "Lucida Sans Typewriter", "DejaVu Sans Mono", "Bitstream Vera Sans Mono",
    "Liberation Mono", "Nimbus Mono L", Monaco, "Courier New", Courier,
    monospace;
}

.html-generator-block {
  width: 90%;
  margin: 30px auto 60px auto;
  // padding-top: 10px;
}

h2.sub-headline {
  text-align: left;
  margin: 30px 0;
}
.card-header {
  text-align: left;
}
a {
  text-decoration: none;
  color: #2c3e50;
}

pre {
  display: block;
  padding: 9.5px;
  margin: 0 0 10px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #333;
  word-break: break-all;
  word-wrap: break-word;
  background-color: #f5f5f5;
  border: 1px solid #ccc;
  border-radius: 4px;
}
</style>
