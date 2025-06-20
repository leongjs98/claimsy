<template>
  <div>
    <div class="hidden py-4 sm:block">
      <div class="border-b border-gray-200">
        <nav class="-mb-px flex items-center justify-center" aria-label="Tabs">
          <RouterLink
            v-for="(tab, index) in tabs"
            :key="index"
            :to="tab.link"
            class="w-1/4 border-b-2 px-1 py-4 text-center text-sm font-medium"
            :class="{
              'border-theme-200 text-theme-300': isActiveTab(tab.link),
              'border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700':
                !isActiveTab(tab.link),
            }"
            :aria-current="isActiveTab(tab.link) ? 'page' : false"
          >
            {{ tab.routeName }}
          </RouterLink>
        </nav>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
  import { useRoute } from "vue-router";

  interface Tab {
    link: string;
    routeName: string;
  }

  interface Props {
    tabs: Tab[];
  }

  const props = withDefaults(defineProps<Props>(), {
    tabs: () => [],
  });

  // Validate tabs prop
  const validateTabs = (tabs: Tab[]): boolean => {
    return tabs.every(
      (tab) => typeof tab === "object" && "link" in tab && "routeName" in tab,
    );
  };

  // Validate props
  if (!validateTabs(props.tabs)) {
    console.warn("CustomTabs: Invalid tabs prop structure");
  }

  const route = useRoute();

  const isActiveTab = (link: string): boolean => {
    return route.path === link;
  };
</script>
