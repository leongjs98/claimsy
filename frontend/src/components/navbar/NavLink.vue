<template>
  <li class="opacity-0 md:opacity-100">
    <RouterLink
      :to="link"
      class="transition-colors after:block after:origin-[0%_50%] after:scale-x-0 after:border-b-[3px] after:border-b-yellow-300 after:p-0 after:pb-1 after:transition-transform after:duration-[250ms] after:ease-in-out after:content-[''] hover:text-yellow-400 hover:after:origin-[0%_50%] hover:after:scale-x-100 sm:after:pb-4"
      :class="
        isActiveLink()
          ? 'text-yellow-400 after:origin-[0%_50%] after:scale-x-100'
          : ''
      "
    >
      {{ name }}
    </RouterLink>
  </li>
</template>

<script setup>
  import { useRoute } from "vue-router";
  const route = useRoute();
  const props = defineProps({
    link: String,
    name: String,
  });

  function isActiveLink() {
    if (route.path == props.link) {
      return true;
    }

    if (props.link === "/employee/claim/all") {
      if (
        route.path === "/employee/claim/expenses" ||
        route.path === "/employee/claim/approved" ||
        route.path === "/employee/claim/rejected"
      ) {
        return true;
      }
    }
    if (
      props.link === "/employee/invoice/upload" &&
      route.path === "/employee/invoice/edit"
    ) {
      return true;
    }
    if (props.link === "/admin/claim/all") {
      if (route.path.includes("/admin/claim")) {
        return true;
      }
      if (route.path.includes("/admin/invoice/review")) {
        return true;
      }
    }
    if (
      props.link === "/admin/policy/upload" &&
      route.path === "/admin/policy/edit"
    ) {
      return true;
    }
    if (
      props.link === "/ask-claimsy" &&
      route.path.includes("/ask-claimsy/smart-suggest")
    ) {
      return true;
    }
    return false;
  }
</script>
