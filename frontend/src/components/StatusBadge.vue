<template>
  <span
    class="inline-flex items-center rounded-md px-2 py-1 text-xs font-medium"
    :class="{
      'bg-emerald-100 text-emerald-600': normalizedStatus === 'approved',
      'bg-red-100 text-red-600': normalizedStatus === 'rejected',
      'bg-yellow-100 text-yellow-600': normalizedStatus === 'pending',
      'bg-orange-100 text-orange-600': normalizedStatus === 'fraud',
      'bg-black text-white': normalizedStatus === 'anomaly',
    }"
  >
    {{ status }}
  </span>
</template>

<script setup>
  const props = defineProps({
    status: String,
  });

  const normalizedStatus = computed(() => props.status?.toLowerCase() || "");

</script>
