<template>
  <span
    class="capitalize inline-flex items-center rounded-md px-2 py-1 text-xs font-medium"
    :class="{
      'bg-emerald-100 text-emerald-600': status.toLowerCase() === 'approved',
      'bg-red-100 text-red-600': status.toLowerCase() === 'rejected',
      'bg-yellow-100 text-yellow-600': status.toLowerCase() === 'pending',
      'bg-orange-100 text-orange-600': status.toLowerCase() === 'anomaly',
    }"
  >
    {{ status }}
  </span>
</template>

<script setup>
  const props = defineProps({
    status: String,
  });
</script>
