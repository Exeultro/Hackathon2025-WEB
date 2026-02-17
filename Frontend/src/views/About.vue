<template>
  <div class="min-h-screen bg-white">
    <!-- Header -->
    <AppHeader />
    
    <main class="pt-20">
      
      <!-- Hero Section -->
      <section class="relative py-20 bg-gradient-to-br from-apogee-red to-apogee-darkRed text-white overflow-hidden">
        <!-- Фон -->
        <div class="absolute inset-0 russian-pattern opacity-20"></div>
        
        <div class="container mx-auto px-6 relative z-10">
          <div class="max-w-4xl mx-auto text-center">
            <h1 class="text-5xl md:text-6xl font-bold mb-6 font-display">О компании</h1>
            <p class="text-xl md:text-2xl text-white/90 leading-relaxed">
              15 лет создаем цифровую инфраструктуру для государственных учреждений России
            </p>
          </div>
        </div>
      </section>

      <!-- Миссия и ценности -->
      <section class="py-20 bg-white">
        <div class="container mx-auto px-6">
          <div class="grid lg:grid-cols-2 gap-12 items-center">
            
            <!-- Текст -->
            <div>
              <h2 class="text-4xl md:text-5xl font-bold text-apogee-dark mb-6 font-display">
                Наша <span class="gradient-text">миссия</span>
              </h2>
              <p class="text-lg text-gray-700 mb-6 leading-relaxed">
                Мы обеспечиваем технологическую независимость и цифровую трансформацию 
                государственного сектора России через внедрение передовых решений 1С.
              </p>
              <p class="text-lg text-gray-700 mb-8 leading-relaxed">
                С 2010 года помогаем госучреждениям работать эффективнее, 
                а гражданам — получать качественные государственные услуги.
              </p>
              
              <div class="flex flex-wrap gap-4">
                <div class="flex items-center space-x-2 text-apogee-red">
                  <span class="text-2xl">🎯</span>
                  <span class="font-semibold">Надежность</span>
                </div>
                <div class="flex items-center space-x-2 text-apogee-red">
                  <span class="text-2xl">⚡</span>
                  <span class="font-semibold">Инновации</span>
                </div>
                <div class="flex items-center space-x-2 text-apogee-red">
                  <span class="text-2xl">🤝</span>
                  <span class="font-semibold">Партнерство</span>
                </div>
              </div>
            </div>

            <!-- Карточки ценностей -->
            <div class="grid gap-6">
              <div v-for="value in values" :key="value.title"
                   class="bg-gradient-to-br from-white to-gray-50 rounded-2xl p-6 shadow-lg border border-gray-100 hover:shadow-xl transition-all duration-300">
                <div class="flex items-center space-x-4">
                  <div class="w-12 h-12 rounded-xl bg-apogee-red flex items-center justify-center text-white text-xl">
                    {{ value.icon }}
                  </div>
                  <div>
                    <h3 class="text-xl font-bold text-apogee-dark mb-2">{{ value.title }}</h3>
                    <p class="text-gray-600">{{ value.description }}</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- История компании -->
      <section class="py-20 bg-gray-50">
        <div class="container mx-auto px-6">
          <div class="text-center mb-16">
            <h2 class="text-4xl md:text-5xl font-bold text-apogee-dark mb-6 font-display">
              Наша <span class="gradient-text">история</span>
            </h2>
            <p class="text-xl text-gray-600 max-w-3xl mx-auto">
              15 лет роста, инноваций и технологических прорывов
            </p>
          </div>

          <!-- Таймлайн -->
          <div class="max-w-4xl mx-auto">
            <div v-for="milestone in milestones" :key="milestone.year"
                 class="flex flex-col md:flex-row gap-8 mb-12">
              <!-- Год -->
              <div class="md:w-1/4 text-center md:text-right">
                <div class="inline-flex items-center justify-center w-20 h-20 bg-apogee-red rounded-full text-white font-bold text-lg shadow-lg">
                  {{ milestone.year }}
                </div>
              </div>
              
              <!-- Содержание -->
              <div class="md:w-3/4 bg-white rounded-2xl p-6 shadow-lg border border-gray-100">
                <h3 class="text-2xl font-bold text-apogee-dark mb-3">{{ milestone.title }}</h3>
                <p class="text-gray-700 mb-4">{{ milestone.description }}</p>
                <div class="flex flex-wrap gap-2">
                  <span v-for="tag in milestone.tags" :key="tag"
                        class="px-3 py-1 bg-red-100 text-apogee-red rounded-full text-sm font-medium">
                    {{ tag }}
                  </span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- География присутствия -->
      <section class="py-20 bg-white">
        <div class="container mx-auto px-6">
          <div class="text-center mb-16">
            <h2 class="text-4xl md:text-5xl font-bold text-apogee-dark mb-6 font-display">
              География <span class="gradient-text">присутствия</span>
            </h2>
            <p class="text-xl text-gray-600 max-w-3xl mx-auto">
              6 филиалов по всей России — от Калининграда до Камчатки
            </p>
          </div>

          <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
            <div v-for="office in offices" :key="office.city"
                 class="bg-gradient-to-br from-white to-gray-50 rounded-2xl p-6 shadow-lg border border-gray-100 hover:shadow-xl transition-all duration-300 group">
              <div class="flex items-center space-x-4 mb-4">
                <div class="w-12 h-12 rounded-xl bg-apogee-red flex items-center justify-center text-white text-xl group-hover:scale-110 transition-transform duration-300">
                  {{ office.emoji }}
                </div>
                <div>
                  <h3 class="text-xl font-bold text-apogee-dark">{{ office.city }}</h3>
                  <p class="text-gray-600">{{ office.role }}</p>
                </div>
              </div>
              <p class="text-gray-700 mb-4">{{ office.description }}</p>
              <div class="flex items-center text-sm text-gray-600">
                <span class="w-2 h-2 bg-green-500 rounded-full mr-2"></span>
                {{ office.clients }} клиентов
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Партнеры и клиенты -->
      <section class="py-20 bg-gray-50">
        <div class="container mx-auto px-6">
          <div class="text-center mb-16">
            <h2 class="text-4xl md:text-5xl font-bold text-apogee-dark mb-6 font-display">
              Нам <span class="gradient-text">доверяют</span>
            </h2>
            <p class="text-xl text-gray-600 max-w-3xl mx-auto">
              Более 3000 государственных учреждений по всей России
            </p>
          </div>

          <div class="bg-white rounded-2xl shadow-lg p-8">
            <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-8 text-center">
              <div v-for="partner in partners" :key="partner.name"
                   class="p-6 rounded-xl border border-gray-200 hover:border-apogee-red hover:shadow-md transition-all duration-300">
                <div class="w-16 h-16 mx-auto mb-4 bg-red-100 rounded-full flex items-center justify-center text-apogee-red text-2xl">
                  {{ partner.emoji }}
                </div>
                <h3 class="font-bold text-gray-800 mb-2">{{ partner.name }}</h3>
                <p class="text-sm text-gray-600">{{ partner.role }}</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Достижения -->
      <section class="py-20 bg-gradient-to-br from-apogee-red to-apogee-darkRed text-white">
        <div class="container mx-auto px-6">
          <div class="text-center mb-16">
            <h2 class="text-4xl md:text-5xl font-bold mb-6 font-display">Наши достижения</h2>
            <p class="text-xl text-white/90 max-w-3xl mx-auto">
              Результаты, которыми мы гордимся
            </p>
          </div>

          <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-8 text-center">
            <div v-for="achievement in achievements" :key="achievement.value"
                 class="bg-white/10 backdrop-blur-sm rounded-2xl p-6 border border-white/20 hover:bg-white/20 transition-all duration-300">
              <div class="text-3xl md:text-4xl font-bold text-apogee-gold mb-2">{{ achievement.value }}</div>
              <div class="text-white font-semibold mb-2">{{ achievement.label }}</div>
              <p class="text-white/80 text-sm">{{ achievement.description }}</p>
            </div>
          </div>
        </div>
      </section>

      <!-- Команда руководителей -->
      <section class="py-20 bg-white">
        <div class="container mx-auto px-6">
          <div class="text-center mb-16">
            <h2 class="text-4xl md:text-5xl font-bold text-apogee-dark mb-6 font-display">
              Руководство <span class="gradient-text">компании</span>
            </h2>
          </div>

          <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
            <div v-for="leader in leadership" :key="leader.name"
                 class="bg-gradient-to-br from-white to-gray-50 rounded-2xl p-6 shadow-lg border border-gray-100 text-center group hover:shadow-xl transition-all duration-300">
              <div class="w-24 h-24 mx-auto mb-4 rounded-full bg-gradient-to-br from-apogee-red to-apogee-darkRed flex items-center justify-center text-white text-2xl font-bold">
                {{ leader.initials }}
              </div>
              <h3 class="text-xl font-bold text-apogee-dark mb-2">{{ leader.name }}</h3>
              <p class="text-apogee-red font-semibold mb-3">{{ leader.position }}</p>
              <p class="text-gray-600 text-sm mb-4">{{ leader.bio }}</p>
              <div class="flex justify-center space-x-3 text-gray-500">
                <span class="text-sm">Опыт: {{ leader.experience }}</span>
                <span class="text-sm">•</span>
                <span class="text-sm">{{ leader.education }}</span>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- CTA Section -->
      <section class="py-20 bg-apogee-dark text-white">
        <div class="container mx-auto px-6 text-center">
          <h2 class="text-3xl md:text-4xl font-bold mb-6 font-display">
            Хотите стать частью нашей истории?
          </h2>
          <p class="text-xl text-gray-300 mb-8 max-w-2xl mx-auto">
            Присоединяйтесь к команде, которая создает технологии для будущего России
          </p>
          
          <div class="flex flex-col sm:flex-row gap-4 justify-center items-center">
            <router-link 
              to="/careers"
              class="bg-apogee-gold text-apogee-dark px-8 py-4 rounded-xl font-semibold hover:bg-yellow-500 transition-all duration-300 flex items-center space-x-2 shadow-lg hover:shadow-xl"
            >
              <span>🚀</span>
              <span>Смотреть вакансии</span>
            </router-link>
            <router-link 
              to="/simulator"
              class="border-2 border-apogee-gold text-apogee-gold px-8 py-4 rounded-xl font-semibold hover:bg-apogee-gold hover:text-apogee-dark transition-all duration-300"
            >
              Попробовать симулятор
            </router-link>
          </div>
        </div>
      </section>

    </main>
  </div>
</template>

<script>
import AppHeader from '@/components/Header.vue'

export default {
  name: 'AboutPage',
  components: {
    AppHeader
  },
  data() {
    return {
      values: [
        {
          icon: '🎯',
          title: 'Клиентоориентированность',
          description: 'Ставим интересы клиента на первое место и гарантируем качество услуг'
        },
        {
          icon: '🚀',
          title: 'Инновации',
          description: 'Постоянно развиваемся и внедряем передовые технологии'
        },
        {
          icon: '🤝',
          title: 'Партнерство',
          description: 'Строим долгосрочные отношения на основе взаимного доверия'
        },
        {
          icon: '💎',
          title: 'Профессионализм',
          description: 'Собираем лучших специалистов и инвестируем в их развитие'
        }
      ],
      milestones: [
        {
          year: '2010',
          title: 'Основание компании',
          description: 'Начали работу как небольшая команда энтузиастов в Красноярске',
          tags: ['Старт', 'Красноярск']
        },
        {
          year: '2013',
          title: 'Первый крупный проект',
          description: 'Реализовали проект автоматизации для Министерства финансов региона',
          tags: ['Госсектор', 'Масштабирование']
        },
        {
          year: '2016',
          title: 'Экспансия по России',
          description: 'Открыли филиалы в 4 городах и достигли 1000 клиентов',
          tags: ['Рост', 'Филиалы']
        },
        {
          year: '2019',
          title: 'Технологический прорыв',
          description: 'Внедрили облачные решения и AI-аналитику для госучреждений',
          tags: ['Инновации', 'Облако']
        },
        {
          year: '2023',
          title: 'Лидер рынка',
          description: 'Стали №7 среди 6800 официальных партнеров 1С в России',
          tags: ['Лидерство', '3000+ клиентов']
        }
      ],
      offices: [
        {
          city: 'Красноярск',
          emoji: '🏔️',
          role: 'Головной офис',
          description: 'Основной разработческий и аналитический центр компании',
          clients: '1200+'
        },
        {
          city: 'Краснодар',
          emoji: '☀️',
          role: 'Южный филиал',
          description: 'Обслуживание клиентов Южного федерального округа',
          clients: '450+'
        },
        {
          city: 'Владивосток',
          emoji: '🌊',
          role: 'Дальневосточный филиал',
          description: 'Работа с клиентами Дальнего Востока и Азиатско-Тихоокеанского региона',
          clients: '380+'
        },
        {
          city: 'Екатеринбург',
          emoji: '⛰️',
          role: 'Уральский филиал',
          description: 'Центр компетенций для Уральского федерального округа',
          clients: '520+'
        },
        {
          city: 'Самара',
          emoji: '🚀',
          role: 'Поволжский филиал',
          description: 'Развитие партнерской сети в Поволжском регионе',
          clients: '290+'
        },
        {
          city: 'Иркутск',
          emoji: '❄️',
          role: 'Сибирский филиал',
          description: 'Специализация на решениях для северных территорий',
          clients: '160+'
        }
      ],
      partners: [
        {
          name: 'Минфин России',
          emoji: '💰',
          role: 'Федеральный партнер'
        },
        {
          name: 'Минздрав РФ',
          emoji: '🏥',
          role: 'Стратегический партнер'
        },
        {
          name: 'Администрация Президента',
          emoji: '🏛️',
          role: 'Технологический партнер'
        },
        {
          name: 'Правительство РФ',
          emoji: '📊',
          role: 'Официальный поставщик'
        }
      ],
      achievements: [
        {
          value: '№7',
          label: 'В России',
          description: 'Среди партнеров 1С'
        },
        {
          value: '99.2%',
          label: 'Успешных проектов',
          description: 'Выполнено в срок'
        },
        {
          value: '24/7',
          label: 'Поддержка',
          description: 'Круглосуточная работа'
        },
        {
          value: '15+',
          label: 'Наград',
          description: 'За инновации'
        }
      ],
      leadership: [
        {
          name: 'Александр Петров',
          initials: 'АП',
          position: 'Генеральный директор',
          bio: 'Основатель компании, эксперт в области ERP-систем с 20-летним опытом',
          experience: '20 лет',
          education: 'МГУ'
        },
        {
          name: 'Елена Смирнова',
          initials: 'ЕС',
          position: 'Технический директор',
          bio: 'Руководит разработкой и внедрением технологических решений',
          experience: '15 лет',
          education: 'МФТИ'
        },
        {
          name: 'Дмитрий Иванов',
          initials: 'ДИ',
          position: 'Директор по развитию',
          bio: 'Отвечает за стратегическое развитие и партнерские отношения',
          experience: '12 лет',
          education: 'ВШЭ'
        }
      ]
    }
  }
}
</script>

<style scoped>
.russian-pattern {
  background-image: 
    radial-gradient(circle at 20% 80%, rgba(255, 255, 255, 0.1) 0%, transparent 50%),
    radial-gradient(circle at 80% 20%, rgba(255, 255, 255, 0.1) 0%, transparent 50%);
  background-size: 100% 100%;
}
</style>