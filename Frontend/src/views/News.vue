<!-- views/NewsPage.vue -->
<template>
  <div class="min-h-screen bg-gray-50 pt-20">
    <!-- Header -->
    <AppHeader />
    
    <main>
      <!-- Hero Section -->
      <section class="bg-gradient-to-br from-apogee-red to-apogee-darkRed text-white py-16">
        <div class="container mx-auto px-6">
          <div class="max-w-4xl mx-auto text-center">
            <h1 class="text-4xl md:text-5xl font-bold mb-6 font-display">Новости компании</h1>
            <p class="text-xl text-white/90 leading-relaxed">
              Будьте в курсе последних событий и достижений Апогея
            </p>
          </div>
        </div>
      </section>

      <!-- Список новостей -->
      <section class="py-12">
        <div class="container mx-auto px-6">
          <!-- Индикатор загрузки -->
          <div v-if="isLoading" class="text-center py-12">
            <div class="inline-flex items-center">
              <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-apogee-red"></div>
              <span class="ml-4 text-gray-600">Загружаем новости...</span>
            </div>
          </div>

          <!-- Сетка новостей -->
          <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            <!-- Карточка новости -->
            <article 
              v-for="newsItem in news" 
              :key="newsItem.id"
              @click="goToNews(newsItem.id)"
              class="bg-white rounded-2xl shadow-lg overflow-hidden cursor-pointer hover:shadow-xl transition-all duration-300 group"
            >
              <!-- Изображение -->
              <div class="relative overflow-hidden h-48">
                <img 
                  :src="getNewsImage(newsItem.image_url)" 
                  :alt="newsItem.title"
                  class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105"
                />
                <div class="absolute inset-0 bg-black bg-opacity-0 group-hover:bg-opacity-10 transition-opacity duration-300"></div>
                <div class="absolute top-4 left-4">
                  <span class="bg-apogee-red text-white px-3 py-1 rounded-full text-sm font-semibold">
                    Новость
                  </span>
                </div>
              </div>

              <!-- Контент -->
              <div class="p-6">
                <!-- Дата -->
                <p class="text-sm text-gray-500 mb-3">
                  {{ formatDate(newsItem.published_at) }}
                </p>
                
                <!-- Заголовок -->
                <h2 class="text-xl font-bold text-apogee-dark mb-3 line-clamp-2 group-hover:text-apogee-red transition-colors">
                  {{ newsItem.title }}
                </h2>
                
                <!-- Превью -->
                <p class="text-gray-600 leading-relaxed mb-4 line-clamp-3">
                  {{ newsItem.preview }}
                </p>
                
                <!-- Читать далее -->
                <div class="flex items-center text-apogee-red font-semibold">
                  <span>Читать далее</span>
                  <svg class="w-4 h-4 ml-2 transform group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
                  </svg>
                </div>
              </div>
            </article>
          </div>

          <!-- Сообщение если нет новостей -->
          <div v-if="!isLoading && news.length === 0" class="text-center py-16">
            <div class="w-24 h-24 mx-auto mb-6 bg-gray-100 rounded-full flex items-center justify-center">
              <span class="text-3xl">📰</span>
            </div>
            <h3 class="text-2xl font-bold text-gray-600 mb-4">Новостей пока нет</h3>
            <p class="text-gray-500 max-w-md mx-auto">
              Следите за обновлениями, скоро здесь появятся свежие новости
            </p>
          </div>
        </div>
      </section>
    </main>
  </div>
</template>

<script>
import AppHeader from '@/components/Header.vue'
import { newsAPI } from '@/services/api'

export default {
  name: 'NewsPage',
  components: {
    AppHeader
  },
  data() {
    return {
      news: [],
      isLoading: false
    }
  },
  async mounted() {
    await this.loadNews()
  },
  methods: {
    async loadNews() {
      this.isLoading = true
      try {
        const response = await newsAPI.getNews()
        this.news = response.data.results || response.data
      } catch (error) {
        console.error('Ошибка загрузки новостей:', error)
        // Fallback данные
        this.news = this.getFallbackNews()
      } finally {
        this.isLoading = false
      }
    },

    goToNews(id) {
      this.$router.push({ name: 'NewsArticle', params: { id } })
    },

    formatDate(dateString) {
      try {
        const options = { 
          year: 'numeric', 
          month: 'long', 
          day: 'numeric',
          timeZone: 'Europe/Moscow'
        }
        return new Date(dateString).toLocaleDateString('ru-RU', options)
      } catch (error) {
        return 'Дата не указана'
      }
    },

    getNewsImage(imageUrl) {
      if (imageUrl) {
        return imageUrl
      }
      // Заглушки для изображений
      const placeholders = [
        'https://images.unsplash.com/photo-1556761175-5973dc0f32e7?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1000&q=80',
        'https://images.unsplash.com/photo-1551434678-e076c223a692?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1000&q=80',
        'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1000&q=80'
      ]
      return placeholders[Math.floor(Math.random() * placeholders.length)]
    },

    getFallbackNews() {
      return [
        {
          id: 1,
          title: 'Компания расширяет географию',
          preview: 'Мы открыли новый офис в Санкт-Петербурге, чтобы лучше обслуживать наших клиентов.',
          content: 'Полный текст новости о расширении компании...',
          image_url: 'https://images.unsplash.com/photo-1497366754035-f200968a6e72?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1000&q=80',
          published_at: '2024-06-01T10:00:00Z',
          is_published: true
        },
        {
          id: 2,
          title: 'Обновление продукта',
          preview: 'Выпущена новая версия симулятора задач с улучшенным интерфейсом и дополнительными функциями.',
          content: 'Подробности обновления продукта...',
          image_url: 'https://images.unsplash.com/photo-1551650975-87deedd944c3?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1000&q=80',
          published_at: '2024-05-15T14:30:00Z',
          is_published: true
        },
        {
          id: 3,
          title: 'Партнерство с крупной фирмой',
          preview: 'Заключено стратегическое партнерство с ведущей ИТ-компанией для совместной разработки решений.',
          content: 'Детали партнерства...',
          image_url: 'https://images.unsplash.com/photo-1521737711867-e3b97375f902?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1000&q=80',
          published_at: '2024-04-20T09:15:00Z',
          is_published: true
        }
      ]
    }
  }
}
</script>

<style scoped>
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.line-clamp-3 {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>