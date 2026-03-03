/* eslint-env node */
require("@rushstack/eslint-patch/modern-module-resolution");

module.exports = {
  extends: [
    "plugin:vue/vue3-recommended",
  ],
  rules: {
    "vue/no-unused-vars": "error",
  },
};
