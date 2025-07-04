<!-- assume passing in YYYY-MM-DD format, 2024-12-29 -->
<template>
  <div>
    <label :for="id" class="block text-sm font-medium text-theme-300">
      {{ label }}
    </label>
    <div class="relative mt-2 grid grid-cols-1 text-left">
      <input
        :name="name"
        :id="id"
        :autocomplete="autocomplete"
        :placeholder="placeholder"
        v-model="model"
        :disabled="disabled"
        type="text"
        class="col-start-1 row-start-1 block w-full rounded-md bg-gray-200 px-4 py-2 pr-10 pl-3 text-base text-theme-300 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-theme-100 focus:outline-2 focus:-outline-offset-2 focus:outline-theme-200 sm:pr-9 sm:text-sm/6"
      />
      <button
        type="button"
        :disabled="disabled"
        class="col-start-1 row-start-1 mr-3 cursor-pointer self-center justify-self-end text-theme-300 disabled:cursor-not-allowed"
        @click="isOpen = !isOpen"
      >
        <svg
          class="size-6 sm:size-5"
          xmlns="http://www.w3.org/2000/svg"
          width="32"
          height="32"
          viewBox="0 0 24 24"
        >
          <!-- Icon from Material Symbols by Google - https://github.com/google/material-design-icons/blob/master/LICENSE -->
          <path
            fill="currentColor"
            d="M5 22q-.825 0-1.412-.587T3 20V6q0-.825.588-1.412T5 4h1V2h2v2h8V2h2v2h1q.825 0 1.413.588T21 6v14q0 .825-.587 1.413T19 22zm0-2h14V10H5zM5 8h14V6H5zm0 0V6zm7 6q-.425 0-.712-.288T11 13t.288-.712T12 12t.713.288T13 13t-.288.713T12 14m-4 0q-.425 0-.712-.288T7 13t.288-.712T8 12t.713.288T9 13t-.288.713T8 14m8 0q-.425 0-.712-.288T15 13t.288-.712T16 12t.713.288T17 13t-.288.713T16 14m-4 4q-.425 0-.712-.288T11 17t.288-.712T12 16t.713.288T13 17t-.288.713T12 18m-4 0q-.425 0-.712-.288T7 17t.288-.712T8 16t.713.288T9 17t-.288.713T8 18m8 0q-.425 0-.712-.288T15 17t.288-.712T16 16t.713.288T17 17t-.288.713T16 18"
          />
        </svg>
      </button>
      <div
        v-show="isOpen"
        class="absolute top-10 right-0 z-10 mt-2 w-80 origin-top-right divide-y divide-gray-100 rounded-md bg-white shadow-lg ring-1 ring-black/5 focus:outline-hidden"
        role="menu"
        aria-orientation="vertical"
        aria-labelledby="menu-button"
        tabindex="-1"
      >
        <div
          class="mt-4 text-center lg:col-start-8 lg:col-end-13 lg:row-start-1 xl:col-start-9"
        >
          <div class="flex items-center text-gray-900">
            <button
              type="button"
              @click="
                displayMonthDate = new Date(
                  displayMonthDate.getFullYear(),
                  displayMonthDate.getMonth() - 1,
                )
              "
              class="-m-1.5 flex flex-none items-center justify-center p-1.5 text-gray-400 hover:text-gray-500"
            >
              <span class="sr-only">Previous month</span>
              <svg
                class="size-5"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                data-slot="icon"
              >
                <path
                  fill-rule="evenodd"
                  d="M11.78 5.22a.75.75 0 0 1 0 1.06L8.06 10l3.72 3.72a.75.75 0 1 1-1.06 1.06l-4.25-4.25a.75.75 0 0 1 0-1.06l4.25-4.25a.75.75 0 0 1 1.06 0Z"
                  clip-rule="evenodd"
                />
              </svg>
            </button>
            <div class="flex-auto text-sm font-semibold">
              {{
                displayMonthDate.toLocaleDateString("en-US", {
                  month: "long",
                  year: "numeric",
                })
              }}
            </div>
            <button
              type="button"
              @click="
                displayMonthDate = new Date(
                  displayMonthDate.getFullYear(),
                  displayMonthDate.getMonth() + 1,
                )
              "
              class="-m-1.5 flex flex-none items-center justify-center p-1.5 text-gray-400 hover:text-gray-500"
            >
              <span class="sr-only">Next month</span>
              <svg
                class="size-5"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                data-slot="icon"
              >
                <path
                  fill-rule="evenodd"
                  d="M8.22 5.22a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.75.75 0 0 1-1.06-1.06L11.94 10 8.22 6.28a.75.75 0 0 1 0-1.06Z"
                  clip-rule="evenodd"
                />
              </svg>
            </button>
          </div>
          <div class="mt-6 grid grid-cols-7 text-xs/6 text-gray-500">
            <div>S</div>
            <div>M</div>
            <div>T</div>
            <div>W</div>
            <div>T</div>
            <div>F</div>
            <div>S</div>
          </div>
          <div
            class="isolate mt-2 grid grid-cols-7 gap-px rounded-lg bg-gray-200 text-sm shadow-sm ring-1 ring-gray-200"
          >
            <!--
          Always include: "py-1.5 hover:bg-gray-100 focus:z-10"
          Is current month, include: "bg-white"
          Is not current month, include: "bg-gray-50"
          Is selected or is today, include: "font-semibold"
          Is selected, include: "text-white"
          Is not selected, is not today, and is current month, include: "text-gray-900"
          Is not selected, is not today, and is not current month, include: "text-gray-400"
          Is today and is not selected, include: "text-indigo-600"

          Top left day, include: "rounded-tl-lg"
          Top right day, include: "rounded-tr-lg"
          Bottom left day, include: "rounded-bl-lg"
          Bottom right day, include: "rounded-br-lg"
        -->
            <button
              v-for="(d, index) in dateArr"
              :key="d"
              type="button"
              @click="date = d"
              class="py-1.5 hover:bg-gray-100 focus:z-10"
              :class="{
                'bg-white': d.getMonth() == displayMonthDate.getMonth(),
                'bg-gray-50': d.getMonth() != displayMonthDate.getMonth(),
                'font-semibold':
                  d.toISOString().split('T')[0] == model || d == new Date(),
                'text-white': d.toISOString().split('T')[0] == model,
                'text-gray-900':
                  d.toISOString().split('T')[0] != model &&
                  d != new Date() &&
                  d.getMonth() == displayMonthDate.getMonth(),
                'text-gray-400':
                  d.toISOString().split('T')[0] != model &&
                  d != new Date() &&
                  d.getMonth() != displayMonthDate.getMonth(),
                'text-indigo-600 underline':
                  d == new Date() && d.toISOString().split('T')[0] != model,
                'rounded-tl-lg': index == 0,
                'rounded-tr-lg': index == 6,
                'rounded-bl-lg': index == dateArr.length - 7,
                'rounded-br-lg': index == dateArr.length - 1,
              }"
            >
              <!--
            Always include: "mx-auto flex size-7 items-center justify-center rounded-full"
            Is selected and is today, include: "bg-indigo-600"
            Is selected and is not today, include: "bg-gray-900"
          -->
              <time
                :datetime="d.toISOString().split('T')[0]"
                class="mx-auto flex size-7 items-center justify-center rounded-full"
                :class="{
                  'bg-indigo-600':
                    d.toISOString().split('T')[0] == model && d == new Date(),
                  'bg-theme-300':
                    d.toISOString().split('T')[0] == model && d != new Date(),
                }"
              >
                {{ d.getDate() }}
              </time>
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div></div>
</template>

<script setup lang="ts">
  import { ref } from "vue";

  interface Props {
    label: string;
    name: string;
    id: string;
    autocomplete?: string;
    placeholder?: string;
    disabled?: boolean;
  }

  const isOpen = ref<boolean>(false);
  const props = defineProps<Props>();
  const model = defineModel();

  const dateArr = ref<Date[]>([]);
  const date = ref<Date>(new Date(model));
  const displayMonthDate = ref<Date>(date.value);
  calcDateArrOfMonth(displayMonthDate.value);

  watch(model, (newVal) => {
    console.log(newVal);
    date.value = new Date(newVal);
    displayMonthDate.value = new Date(newVal);
  });

  watch(date, (newDate) => {
    date.value = newDate;
    displayMonthDate.value = newDate;
    calcDateArrOfMonth(newDate);
    model.value = date.value.toISOString().split("T")[0];
  });

  watch(displayMonthDate, (newDate) => {
    displayMonthDate.value = newDate;
    calcDateArrOfMonth(newDate);
  });

  function calcDateArrOfMonth(newDate: Date) {
    const month: number = newDate.getMonth();
    const year: number = newDate.getFullYear();
    const firstDateOfMonth: number = new Date(year, month, 1);
    const lastDateOfMonth: number = new Date(year, month + 1, 0);

    dateArr.value = [];
    for (let i: number = 0; i <= lastDateOfMonth.getDate() - 1; i++) {
      dateArr.value.push(
        new Date(firstDateOfMonth.getTime() + i * 24 * 60 * 60 * 1000),
      );
    }

    // Pad the first week
    for (let i: number = 0; i < firstDateOfMonth.getDay(); i++) {
      dateArr.value.unshift(
        new Date(firstDateOfMonth.getTime() - (i + 1) * 24 * 60 * 60 * 1000),
      );
    }

    // Pad the last week
    for (let i: number = 0; i <= 6 - lastDateOfMonth.getDay() - 1; i++) {
      dateArr.value.push(
        new Date(lastDateOfMonth.getTime() + (i + 1) * 24 * 60 * 60 * 1000),
      );
    }
  }
</script>
