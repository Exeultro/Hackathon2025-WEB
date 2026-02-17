<template>
  <div class="bg-white rounded-2xl shadow-lg p-6 flex flex-col items-center text-center">
    <img
      :src="photo"
      :alt="name"
      class="w-32 h-32 rounded-full object-cover mb-4 shadow-md"
    />
    <h2 class="text-xl font-semibold text-apogee-dark mb-1">{{ name }}</h2>
    <p class="text-apogee-red font-semibold mb-1">{{ position }}</p>
    <p class="text-gray-700 font-medium mb-1">Город: {{ city }}</p>
    <p class="text-gray-700 font-medium mb-2">Образование: {{ education }}</p>
    <p class="text-gray-600 text-sm">{{ bio }}</p>
  </div>
</template>

<script>
export default {
  name: 'TeamItem',
  props: {
    name: { type: String, required: true },
    position: { type: String, required: true },
    city: { type: String, required: true },
    education: { type: String, required: true },
    bio: { type: String, required: true },
    photo: { type: String, required: true }
  }
}
</script>
