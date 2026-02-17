<!-- views/NewsArticle.vue -->
<template>
  <div class="min-h-screen bg-gray-50 pt-20">
    <!-- Header -->
    <AppHeader />
    
    <main v-if="newsArticle">
      <!-- Hero Section -->
      <section class="bg-gradient-to-br from-apogee-red to-apogee-darkRed text-white py-16">
        <div class="container mx-auto px-6">
          <div class="max-w-4xl mx-auto text-center">
            <div class="mb-4">
              <span class="bg-white/20 text-white px-4 py-2 rounded-full text-sm font-semibold">
                Новость
              </span>
            </div>
            <h1 class="text-4xl md:text-5xl font-bold mb-6 font-display">{{ newsArticle.title }}</h1>
            <p class="text-xl text-white/90">
              {{ formatDate(newsArticle.published_at) }}
            </p>
          </div>
        </div>
      </section>

      <!-- Контент новости -->
      <section class="py-12">
        <div class="container mx-auto px-6">
          <div class="max-w-4xl mx-auto bg-white rounded-2xl shadow-lg overflow-hidden">
            <!-- Изображение -->
            <div class="relative h-80 md:h-96">
              <img 
                :src="getNewsImage(newsArticle.image_url)" 
                :alt="newsArticle.title"
                class="w-full h-full object-cover"
              />
            </div>

            <!-- Содержание -->
            <div class="p-8 md:p-12">
              <!-- Превью -->
              <p class="text-xl text-gray-600 leading-relaxed mb-8 font-medium">
                {{ newsArticle.preview }}
              </p>

              <!-- Основной текст -->
              <div class="prose prose-lg max-w-none">
                <div v-html="formatContent(newsArticle.content)"></div>
              </div>

              <!-- Дополнительная информация -->
              <div class="mt-12 pt-8 border-t border-gray-200">
                <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center text-sm text-gray-500">
                  <div>
                    <p>Опубликовано: {{ formatDateTime(newsArticle.published_at) }}</p>
                    <p v-if="newsArticle.updated_at !== newsArticle.created_at">
                      Обновлено: {{ formatDateTime(newsArticle.updated_at) }}
                    </p>
                  </div>
                  <button 
                    @click="$router.back()"
                    class="mt-4 sm:mt-0 flex items-center space-x-2 text-apogee-red hover:text-apogee-darkRed transition-colors"
                  >
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path>
                    </svg>
                    <span>Назад к новостям</span>
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Другие новости -->
      <section v-if="relatedNews.length > 0" class="py-12 bg-white">
        <div class="container mx-auto px-6">
          <h2 class="text-3xl font-bold text-apogee-dark mb-8 text-center">Другие новости</h2>
          <div class="grid grid-cols-1 md:grid-cols-3 gap-6 max-w-6xl mx-auto">
            <article 
              v-for="newsItem in relatedNews" 
              :key="newsItem.id"
              @click="goToNews(newsItem.id)"
              class="bg-gray-50 rounded-xl p-6 cursor-pointer hover:shadow-md transition-all duration-300"
            >
              <h3 class="text-lg font-semibold text-apogee-dark mb-2 line-clamp-2">
                {{ newsItem.title }}
              </h3>
              <p class="text-sm text-gray-500 mb-3">
                {{ formatDate(newsItem.published_at) }}
              </p>
              <p class="text-gray-600 text-sm line-clamp-2">
                {{ newsItem.preview }}
              </p>
            </article>
          </div>
        </div>
      </section>
    </main>

    <!-- Загрузка -->
    <div v-else-if="isLoading" class="min-h-screen flex items-center justify-center">
      <div class="text-center">
        <div class="animate-spin rounded-full h-16 w-16 border-b-2 border-apogee-red mx-auto"></div>
        <p class="mt-4 text-gray-600">Загружаем новость...</p>
      </div>
    </div>

    <!-- Ошибка -->
    <div v-else class="min-h-screen flex items-center justify-center">
      <div class="text-center">
        <div class="w-24 h-24 mx-auto mb-6 bg-gray-100 rounded-full flex items-center justify-center">
          <span class="text-3xl">😕</span>
        </div>
        <h3 class="text-2xl font-bold text-gray-600 mb-4">Новость не найдена</h3>
        <p class="text-gray-500 mb-6">Возможно, эта новость была удалена или перемещена</p>
        <button 
          @click="$router.push({ name: 'NewsPage' })"
          class="bg-apogee-red text-white px-6 py-3 rounded-xl font-semibold hover:bg-apogee-darkRed transition-colors"
        >
          Вернуться к новостям
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import AppHeader from '@/components/Header.vue'
import { newsAPI } from '@/services/api'

export default {
  name: 'NewsArticle',
  components: {
    AppHeader
  },
  data() {
    return {
      newsArticle: null,
      relatedNews: [],
      isLoading: true
    }
  },
  async mounted() {
    await this.loadNewsArticle()
    await this.loadRelatedNews()
  },
  methods: {
    async loadNewsArticle() {
      this.isLoading = true
      try {
        const newsId = this.$route.params.id
        const response = await newsAPI.getNewsArticle(newsId)
        this.newsArticle = response.data
      } catch (error) {
        console.error('Ошибка загрузки новости:', error)
        this.newsArticle = null
      } finally {
        this.isLoading = false
      }
    },

    async loadRelatedNews() {
      try {
        const response = await newsAPI.getNews()
        const allNews = response.data.results || response.data
        // Исключаем текущую новость и берем 3 случайные
        this.relatedNews = allNews
          .filter(news => news.id !== parseInt(this.$route.params.id))
          .slice(0, 3)
      } catch (error) {
        console.error('Ошибка загрузки связанных новостей:', error)
        this.relatedNews = []
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

    formatDateTime(dateString) {
      try {
        const options = { 
          year: 'numeric', 
          month: 'long', 
          day: 'numeric',
          hour: '2-digit',
          minute: '2-digit',
          timeZone: 'Europe/Moscow'
        }
        return new Date(dateString).toLocaleDateString('ru-RU', options)
      } catch (error) {
        return 'Дата не указана'
      }
    },

    formatContent(content) {
      // Простая форматировка текста - можно расширить для markdown и т.д.
      return content.replace(/\n/g, '<br>')
    },

    getNewsImage(imageUrl) {
      if (imageUrl) {
        return imageUrl
      }
      return 'https://images.unsplash.com/photo-1556761175-5973dc0f32e7?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1000&q=80'
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
</style>