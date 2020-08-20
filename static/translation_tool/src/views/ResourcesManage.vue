<template>
  <div class="resources-manage-block">
    <h1>Resources Manage</h1>
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

    <table class="table">
      <thead>
        <tr>
          <th scope="col">Key\Locale</th>
          <th v-for="res in getResources" scope="col" :key="res.id">{{res.locale}}</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th scope="row"></th>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: "ResourcesManage",
  components: {},
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
    getResourcesKeys() {
      return ''
    }
  },
  methods: {
    templateChangeHandler() {
      this.$store.dispatch("getResources", this.selectedTemplateId);
      if (this.selectedTemplateId) {
        this.selected_template = this.$store.getters.getTemplateById(
          this.selectedTemplateId
        );
      }
    },
  },
};
</script>


<style lang="scss" scoped>
* {
  font-family: Consolas, "Andale Mono WT", "Andale Mono", "Lucida Console",
    "Lucida Sans Typewriter", "DejaVu Sans Mono", "Bitstream Vera Sans Mono",
    "Liberation Mono", "Nimbus Mono L", Monaco, "Courier New", Courier,
    monospace;
}

.resources-manage-block {
  width: 90%;
  margin: 30px auto 60px auto;
  // padding-top: 10px;
}

h2.sub-headline {
  text-align: left;
  margin: 30px 0;
}
</style>