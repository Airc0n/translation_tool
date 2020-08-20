<template>
  <div class="html-template-item">
    <div class="card">
      <div class="card-body">
        <h5 class="card-title">{{name}}</h5>
        <h6 class="card-subtitle mb-2 text-muted">by {{modified_by}} @ {{modified_at}}</h6>
        <p class="card-text">
          {{ html }}
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "HTMLTempalteItem",
  props: {},
  data() {
    return {
      name: "This is template name",
      html: "<div>{{test}}</div>",
      modified_by: 'aircon_chen@htc.com',
      modified_at: '2020/08/13'
    };
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.html-template-item {
  width: 90%;
  margin: 10px auto;
}
</style>
