<template>
  <!-- "after:block after:origin-[0%_50%] after:scale-x-0 after:border-b-[3px] after:border-b-yellow-300 after:p-0 after:pb-1 after:transition-transform after:duration-[250ms] after:ease-in-out after:content-[''] sm:after:pb-4 " , -->
  <!-- "hover:after:origin-[0%_50%] hover:after:scale-x-100 hover:text-yellow-400 transition-colors"=> !$isActive, -->
  <!-- "after:origin-[0%_50%] after:scale-x-100 text-yellow-400" => $isActive, -->
  <li class="opacity-0 md:opacity-100">
    <a :href="link"
      class="after:block after:origin-[0%_50%] after:scale-x-0 after:border-b-[3px] after:border-b-yellow-300 after:p-0 after:pb-1 after:transition-transform after:duration-[250ms] after:ease-in-out after:content-[''] sm:after:pb-4 hover:after:origin-[0%_50%] hover:after:scale-x-100 hover:text-yellow-400 transition-colors">
      {{ name }}
    </a>
  </li>
</template>

<script setup>
  const props = defineProps({
    link: String,
    name: String,
    isActive: Boolean,
  });
</script>
