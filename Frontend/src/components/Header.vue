<template>
  <header class="fixed top-0 left-0 right-0 z-50 bg-white shadow-lg border-b border-gray-200">
    <nav class="container mx-auto px-6 py-4">
        <div class="flex items-center justify-between relative">
        <!-- Логотип -->
        <router-link to="/" class="flex items-center space-x-4 group cursor-pointer">
          <div class="relative">
            <div class="w-16 h-16 bg-white rounded-xl flex items-center justify-center shadow-lg group-hover:scale-110 transition-transform duration-300 overflow-hidden">
              <img 
                src="@/assets/images/apoget.png" 
                alt="Apogee Career" 
                class="w-full h-full object-contain p-1"
              />
            </div>
          </div>
          <div>
            <h1 class="text-2xl font-bold text-apogee-red font-display">АПОГЕЙ</h1>
            <p class="text-gray-600 text-xs font-semibold">Технологии для России</p>
          </div>
        </router-link>

        <!-- Навигация -->
        <div class="hidden lg:flex items-center space-x-8 absolute left-1/2 transform -translate-x-1/2">
          <router-link 
            v-for="item in navigation" 
            :key="item.name"
            :to="item.path"
            class="text-gray-700 hover:text-apogee-red font-medium transition-all duration-300 relative group"
            active-class="text-apogee-red font-semibold"
          >
            {{ item.name }}
            <span class="absolute -bottom-1 left-0 w-0 h-0.5 bg-apogee-red transition-all duration-300 group-hover:w-full"></span>
          </router-link>
        </div>  

        <!-- Мобильное меню -->
        <button 
          @click="isMobileMenuOpen = !isMobileMenuOpen"
          class="lg:hidden p-2 rounded-lg hover:bg-gray-100 transition-colors"
        >
          <svg class="w-6 h-6 text-apogee-red" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path 
              stroke-linecap="round" 
              stroke-linejoin="round" 
              stroke-width="2" 
              :d="isMobileMenuOpen ? 'M6 18L18 6M6 6l12 12' : 'M4 6h16M4 12h16M4 18h16'"
            />
          </svg>
        </button>
      </div>

      <!-- Мобильное меню -->
      <div 
        v-if="isMobileMenuOpen"
        class="lg:hidden mt-4 py-4 bg-white rounded-lg shadow-xl border border-gray-200"
      >
        <router-link 
          v-for="item in navigation" 
          :key="item.name"
          :to="item.path"
          @click="isMobileMenuOpen = false"
          class="block py-3 px-4 text-gray-700 hover:bg-apogee-red hover:text-white font-medium transition-all duration-300"
          active-class="text-apogee-red bg-red-50"
        >
          {{ item.name }}
        </router-link>
      </div>
    </nav>
  </header>
</template>

<script>
export default {
  name: 'AppHeader',
  data() {
    return {
      isMobileMenuOpen: false,
      navigation: [
        { name: 'Главная', path: '/' },
        { name: 'О компании', path: '/about' },
        { name: 'Карьерные пути', path: '/career-paths' },
        { name: 'Наши таланты', path: '/team' },
        { name: 'Новости', path: '/news' }
      ]
    }
  }
}
</script>   