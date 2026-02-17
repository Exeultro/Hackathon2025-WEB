  <template>
  <div class="min-h-screen bg-white">
    <!-- Header -->
    <AppHeader />
    
    <!-- Main Content -->
    <main class="pt-20">
      
      <!-- Hero Section -->
      <section id="main" class="relative min-h-screen flex items-center justify-center overflow-hidden gradient-bg">
        <!-- Анимированный фон -->
        <div class="absolute inset-0 russian-pattern"></div>
        
        <!-- Парящие элементы -->
        <div class="absolute inset-0">
          <div v-for="i in 15" :key="i" 
               class="absolute rounded-full bg-white bg-opacity-10 animate-float"
               :style="{
                 width: `${Math.random() * 80 + 30}px`,
                 height: `${Math.random() * 80 + 30}px`,
                 left: `${Math.random() * 100}%`,
                 top: `${Math.random() * 100}%`,
                 animationDelay: `${Math.random() * 5}s`,
                 animationDuration: `${Math.random() * 10 + 10}s`
               }">
          </div>
        </div>

        <div class="container mx-auto px-6 relative z-10">
          <div class="max-w-6xl mx-auto text-center text-white">
            <!-- Заголовок с анимацией -->
            <div class="stagger-animation py-12">
              <h1 class="text-5xl md:text-7xl lg:text-8xl font-bold mb-6 leading-tight font-display">
                <span class="block">АПОГЕЙ</span>
              </h1>

              <!-- Подзаголовок -->
              <p class="text-xl md:text-2xl mb-12 text-white/90 leading-relaxed max-w-4xl mx-auto">
                <span class="text-apogee-gold font-semibold">15 лет</span> создаем цифровое будущее России. 
                Федеральная техподдержка 1С для <span class="text-apogee-gold font-semibold">3000+</span> госучреждений.
              </p>

              <!-- Статистика -->
              <div class="grid grid-cols-2 lg:grid-cols-4 gap-6 mb-12">
                <div v-for="(stat, index) in stats" :key="stat.label" 
                     class="glass-effect rounded-2xl p-6 transform hover:scale-105 transition-all duration-300 hover:bg-white/20"
                     :style="`animation-delay: ${0.3 + index * 0.1}s`">
                  <div class="text-2xl md:text-3xl font-bold text-apogee-gold mb-2">{{ stat.value }}</div>
                  <div class="text-white/80 text-sm font-medium">{{ stat.label }}</div>
                </div>
              </div>

              <!-- Кнопки CTA -->
              <div class="flex flex-col sm:flex-row gap-4 justify-center items-center mb-12">
                <router-link 
                  to="/career-paths"
                  class="btn-gold text-lg px-8 py-4 flex items-center space-x-3 group"
                >
                  <span class="group-hover:scale-110 transition-transform">🎯</span>
                  <span class="font-bold">Начать карьеру</span>
                </router-link>
                <button class="btn-secondary text-lg px-8 py-4 flex items-center space-x-3 group">
                  <span class="group-hover:scale-110 transition-transform">📞</span>
                  <span>Связаться с нами</span>
                </button>
              </div>

              <!-- Быстрый старт для кандидатов -->
              <div class="glass-effect rounded-2xl p-6 max-w-2xl mx-auto mb-8 backdrop-blur-sm border-2 border-apogee-gold/30">
                <div class="flex items-center justify-center space-x-3 mb-4">
                  <span class="text-2xl">⚡</span>
                  <h3 class="text-xl font-bold text-apogee-gold">Быстрый старт в карьере</h3>
                </div>
                <p class="text-white/90 text-lg text-center leading-relaxed">
                  <span class="text-apogee-gold font-semibold">Интересуешься работой в перспективной компании?</span><br>
                  Реши 3 задачи в симуляторе и получи приглашение на собеседование 
                  <span class="text-apogee-gold font-bold">в течение 24 часов</span>, 
                  вместо молчания неделями на HH.ru
                </p>
                <div class="flex justify-center mt-4">
                  <router-link 
                    to="/simulator"
                    class="bg-white text-apogee-dark px-6 py-3 rounded-lg font-semibold hover:bg-apogee-gold transition-all duration-300 flex items-center space-x-2 group"
                  >
                    <span class="group-hover:scale-110 transition-transform">🎮</span>
                    <span>Попробовать симулятор</span>
                  </router-link>
                </div>
              </div>

              <!-- Доверие -->
              <div class="glass-effect rounded-2xl p-6 max-w-2xl mx-auto backdrop-blur-sm ">
                <p class="text-white/90 text-lg">
                  <span class="text-apogee-gold font-semibold">Доверяют:</span> 
                  Минфин РФ • Минздрав РФ • Администрация Президента • Правительство РФ
                </p>
              </div>
            </div>
          </div>
        </div>

        <!-- Scroll indicator -->
        <div class="absolute bottom-8 left-1/2 transform -translate-x-1/2 animate-bounce">
          <div class="w-6 h-10 border-2 border-apogee-gold rounded-full flex justify-center">
            <div class="w-1 h-3 bg-apogee-gold rounded-full mt-2 animate-pulse"></div>
          </div>
        </div>
      </section>

      <!-- Преимущества -->
      <section id="about" class="py-20 bg-white relative overflow-hidden">
        <!-- Декоративные элементы -->
        <div class="absolute top-10 left-10 w-64 h-64 bg-apogee-lightRed rounded-full opacity-50 blur-xl"></div>
        <div class="absolute bottom-10 right-10 w-64 h-64 bg-apogee-lightRed rounded-full opacity-30 blur-xl"></div>
        
        <div class="container mx-auto px-6 relative z-10">
          <div class="text-center mb-16">
            <h2 class="text-4xl md:text-5xl lg:text-6xl font-bold text-apogee-dark mb-6 font-display">
              Почему <span class="gradient-text">Апогей</span>?
            </h2>
            <p class="text-xl text-gray-600 max-w-3xl mx-auto leading-relaxed">
              Мы создаем экосистему, где таланты становятся технологическими лидерами, 
              а амбиции — национальными проектами
            </p>
          </div>

          <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
            <div v-for="(feature, index) in features" :key="index"
                 class="group relative bg-gradient-to-br from-white to-gray-50 rounded-3xl p-8 shadow-lg card-hover border border-gray-100 hover:border-apogee-red/20 transition-all duration-500">
              <!-- Декоративный номер -->
              <div class="absolute -top-3 -left-3 w-10 h-10 bg-apogee-red rounded-full flex items-center justify-center text-white font-bold text-sm shadow-lg">
                {{ index + 1 }}
              </div>
              
              <div class="text-center">
                <div class="w-16 h-16 mx-auto mb-6 rounded-2xl bg-gradient-to-br from-apogee-red to-apogee-darkRed flex items-center justify-center group-hover:scale-110 transition-transform duration-300 shadow-lg">
                  <span class="text-2xl text-white">{{ feature.icon }}</span>
                </div>
                <h3 class="text-2xl font-bold text-apogee-dark mb-4">{{ feature.title }}</h3>
                <p class="text-gray-700 leading-relaxed mb-4 text-base">{{ feature.description }}</p>
                
                <!-- Список преимуществ -->
                <ul class="space-y-3 text-left">
                  <li v-for="point in feature.points" :key="point" 
                      class="flex items-start text-gray-800 text-base">
                    <span class="w-2 h-2 bg-apogee-red rounded-full mt-2 mr-3 flex-shrink-0"></span>
                    <span>{{ point }}</span>
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Калькулятор карьеры -->
      <section class="py-20 bg-gray-50">
        <div class="container mx-auto px-6">
          <div class="text-center mb-16">
            <h2 class="text-4xl md:text-5xl font-bold text-apogee-dark mb-6 font-display">
              Рассчитай свой <span class="gradient-text">карьерный рост</span>
            </h2>
            <p class="text-xl text-gray-600 max-w-2xl mx-auto">
              Узнай, как будет расти твоя зарплата в Апогее от стажера до руководителя
            </p>
          </div>

          <div class="max-w-4xl mx-auto bg-white rounded-3xl shadow-xl p-8">
            <div class="grid md:grid-cols-2 gap-8">
              <!-- Левая часть - настройки -->
              <div class="space-y-6">
                <div>
                  <label class="block text-sm font-semibold text-gray-700 mb-2">Текущий уровень</label>
                  <select v-model="currentLevel" class="w-full p-3 border border-gray-300 rounded-xl focus:border-apogee-red focus:ring-2 focus:ring-apogee-red/20 transition-all">
                    <option value="intern">Стажер</option>
                    <option value="junior">Junior</option>
                    <option value="middle">Middle</option>
                    <option value="senior">Senior</option>
                  </select>
                </div>

                <div>
                  <label class="block text-sm font-semibold text-gray-700 mb-2">Направление</label>
                  <select v-model="careerPath" class="w-full p-3 border border-gray-300 rounded-xl focus:border-apogee-red focus:ring-2 focus:ring-apogee-red/20 transition-all">
                    <option value="programmer">Программист 1С</option>
                    <option value="consultant">Консультант 1С</option>
                    <option value="analyst">Бизнес-аналитик</option>
                  </select>
                </div>

                <div>
                  <label class="block text-sm font-semibold text-gray-700 mb-2">
                    Скорость роста: <span class="text-apogee-red">{{ growthSpeed }} лет на уровень</span>
                  </label>
                  <input 
                    type="range" 
                    v-model="growthSpeed"
                    min="0.5" 
                    max="3" 
                    step="0.5"
                    class="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer slider-red"
                  >
                  <div class="flex justify-between text-xs text-gray-500 mt-1">
                    <span>Быстро</span>
                    <span>Умеренно</span>
                    <span>Стабильно</span>
                  </div>
                </div>

                <div class="bg-apogee-red bg-opacity-10 p-4 rounded-xl">
                  <h4 class="font-semibold text-apogee-red mb-2">💡 Совет</h4>
                  <p class="text-sm text-gray-700">
                    {{ growthTip }}
                  </p>
                </div>
              </div>

              <!-- Правая часть - результат -->
              <div class="bg-gradient-to-br from-apogee-red to-apogee-darkRed rounded-2xl p-6 text-white">
                <h3 class="text-xl font-bold mb-4 text-center">Твой карьерный путь</h3>
                
                <div class="space-y-4">
                  <div v-for="(stage, index) in careerStages" 
                       :key="stage.level"
                       class="flex items-center justify-between p-3 rounded-lg"
                       :class="index === 0 ? 'bg-white/20' : 'bg-white/10'">
                    <div>
                      <div class="font-semibold">{{ stage.level }}</div>
                      <div class="text-sm opacity-80">{{ stage.years }}</div>
                    </div>
                    <div class="text-right">
                      <div class="font-bold text-lg">{{ stage.salary }}</div>
                      <div class="text-sm opacity-80">+{{ stage.bonus }}</div>
                    </div>
                  </div>
                </div>

                <div class="mt-6 pt-4 border-t border-white/20">
                  <div class="flex justify-between items-center">
                    <span class="font-semibold">Через 5 лет:</span>
                    <span class="font-bold text-2xl">{{ fiveYearSalary }}</span>
                  </div>
                  <div class="text-sm opacity-80 mt-1">+ карьерный рост до {{ careerStages[careerStages.length - 1].level }}</div>
                </div>
              </div>
            </div>

            <!-- График роста -->
            <div class="mt-8">
              <h4 class="text-lg font-semibold text-center mb-4">Динамика роста зарплаты</h4>
              <div class="flex items-end justify-between h-32 bg-gray-100 rounded-xl p-4">
                <div v-for="stage in careerStages" 
                     :key="stage.level"
                     class="flex flex-col items-center">
                  <div class="text-xs text-gray-600 mb-1">{{ stage.levelShort }}</div>
                  <div class="w-8 bg-gradient-to-t from-apogee-red to-apogee-darkRed rounded-t transition-all duration-500"
                       :style="{ height: stage.chartHeight + 'px' }"></div>
                  <div class="text-xs font-semibold mt-1">{{ stage.salary }}</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Статистика и достижения -->
      <section class="py-20 gradient-bg relative overflow-hidden">
        <div class="absolute inset-0 russian-pattern"></div>
        
        <div class="container mx-auto px-6 relative z-10">
          <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6 text-center">
            <div v-for="achievement in achievements" :key="achievement.label"
                 class="glass-effect rounded-2xl p-6 transform hover:scale-105 transition-transform duration-300 backdrop-blur-sm">
              <div class="text-3xl md:text-4xl font-bold text-apogee-gold mb-2">{{ achievement.value }}</div>
              <div class="text-white text-lg font-semibold mb-2">{{ achievement.label }}</div>
              <p class="text-red-100 text-sm">{{ achievement.description }}</p>
            </div>
          </div>
        </div>
      </section>

      <!-- Команда (превью) -->
      <section class="py-20 bg-gray-50">
        <div class="container mx-auto px-6">
          <div class="text-center mb-16">
            <h2 class="text-4xl md:text-5xl font-bold text-apogee-dark mb-6 font-display">
              Ты <span class="gradient-text">СТУДЕНТ</span> или <span class="gradient-text">ВЫПУСКНИК?</span>
            </h2>
            <p class="text-xl text-gray-600 max-w-2xl mx-auto">
              Посмотри на карьерный рост выпускников техникумов и институтов:
            </p>
          </div>

          <div class="grid md:grid-cols-3 gap-8">
            <div v-for="member in teamPreview" :key="member.name"
                 class="bg-white rounded-2xl p-6 shadow-lg card-hover text-center group">
              <div class="w-20 h-20 mx-auto mb-4 rounded-full overflow-hidden border-2 border-gradient-to-br from-apogee-red to-apogee-darkRed shadow-lg">
                <img :src="member.image" :alt="member.name" class="w-full h-full object-cover" />
              </div>
              <h3 class="text-lg font-bold text-apogee-dark mb-2">{{ member.name }}</h3>
              <p class="text-apogee-red font-semibold mb-3">{{ member.position }}</p>
              <p class="text-gray-600 text-sm">{{ member.quote }}</p>
            </div>
          </div>
        </div>
      </section>

      <!-- Финальный CTA -->
      <section class="py-20 bg-apogee-dark relative overflow-hidden">
        <div class="absolute inset-0 opacity-5">
          <div class="absolute inset-0 bg-gradient-to-r from-apogee-red to-apogee-gold"></div>
        </div>
        
        <div class="container mx-auto px-6 text-center relative z-10">
          <h2 class="text-3xl md:text-4xl lg:text-5xl font-bold text-white mb-6 font-display">
            Готовы изменить будущее России?
          </h2>
          <p class="text-lg md:text-xl text-gray-300 mb-8 max-w-2xl mx-auto">
            Присоединяйтесь к команде, которая создает технологии для национального масштаба
          </p>
          
          <div class="flex flex-col sm:flex-row gap-4 justify-center items-center">
            <router-link 
              to="/careers"
              class="btn-gold px-10 py-4 text-lg flex items-center space-x-2"
            >
              <span>🚀</span>
              <span>Начать карьеру в Апогее</span>
            </router-link>
            <button class="border-2 border-apogee-gold text-apogee-gold px-10 py-4 rounded-xl font-semibold hover:bg-apogee-gold hover:text-apogee-dark transition-all duration-300">
              📞 Бесплатная консультация
            </button>
          </div>

          <!-- Быстрые ссылки -->
          <div class="mt-12 flex flex-wrap justify-center gap-6 text-white/70">
            <router-link to="/careers" class="hover:text-apogee-gold transition-colors">🔥 Горячие вакансии</router-link>
            <router-link to="/careers" class="hover:text-apogee-gold transition-colors">🎓 Стажировки</router-link>
            <router-link to="/career-paths" class="hover:text-apogee-gold transition-colors">💼 История успеха</router-link>
            <router-link to="/about" class="hover:text-apogee-gold transition-colors">📚 Обучение</router-link>
          </div>
        </div>
      </section>
    </main>
  </div>
</template>

<script>
import AppHeader from '@/components/Header.vue'

export default {
  name: 'HomePage',
  components: {
    AppHeader
  },
  data() {
    return {
      stats: [
        { value: '15 лет', label: 'Опыта на рынке' },
        { value: '550+', label: 'Профессионалов' },
        { value: '6', label: 'Федеральных филиалов' },
        { value: '3000+', label: 'Довольных клиентов' }
      ],
      features: [
        {
          icon: '🏛️',
          title: 'Федеральный масштаб',
          description: 'Работа с ключевыми государственными институтами',
          points: [
            'Проекты национального значения',
            'Прямое взаимодействие с министерствами',
            'Влияние на цифровую трансформацию'
          ]
        },
        {
          icon: '🚀',
          title: 'Технологический рост',
          description: 'Непрерывное развитие и карьерные перспективы',
          points: [
            'Обучение за счет компании',
            'Международные сертификации', 
            'Карьера от junior до architect'
          ]
        },
        {
          icon: '💎',
          title: 'Элитная команда',
          description: 'Окружение лучших специалистов страны',
          points: [
            'Менторы уровня Team Lead',
            'Code review от экспертов',
            'Сообщество профессионалов'
          ]
        }
      ],
      achievements: [
        { 
          value: '№7', 
          label: 'В России', 
          description: 'Среди партнеров 1С' 
        },
        { 
          value: '99%', 
          label: 'Успешных проектов', 
          description: 'Выполнено в срок' 
        },
        { 
          value: '24/7', 
          label: 'Техподдержка', 
          description: 'Круглосуточная работа' 
        },
        { 
          value: '15+', 
          label: 'Наград', 
          description: 'За технологические инновации' 
        }
      ],
      teamPreview: [
        {
          image: 'https://avatars.mds.yandex.net/i?id=686c0707c99443e56cd0d135fc55d80eeca5ab32-9181120-images-thumbs&n=13',
          name: 'Анна Иванова',
          position: 'Senior разработчик',
          quote: 'В Апогее выросла от junior до Senior разработчика за 4 года'
        },
        {
          image: 'https://avatars.mds.yandex.net/i?id=f35995718ff2433a39eb1827ffcf171be1819746-4024741-images-thumbs&n=13',
          name: 'Максим Петров',
          position: 'Middle-разработчик', 
          quote: 'В Апогее вырос от Junior до Miidle разработчика за 2 года.'
        },
        {
          image: 'https://avatars.mds.yandex.net/i?id=69a6b8d176b6860bed87b9a2ff53bd58_sr-10702479-images-thumbs&n=13',
          name: 'Елена Смирнова',
          position: 'Team Lead команды разработчиков',
          quote: 'В Апогее выросла от Middle разработчика выросла до Team Lead за 4 года'
        }
      ],
      // Данные для калькулятора
      currentLevel: 'junior',
      careerPath: 'programmer',
      growthSpeed: 1.5,
      careerPaths: {
        programmer: {
          intern: { salary: '30-40k', bonus: 'обучение', years: '0-1 год', level: 'Стажер', levelShort: 'СТ' },
          junior: { salary: '50-70k', bonus: 'ментор', years: '1-2 года', level: 'Junior', levelShort: 'JN' },
          middle: { salary: '80-120k', bonus: 'премии', years: '2-3 года', level: 'Middle', levelShort: 'MD' },
          senior: { salary: '120-160k', bonus: 'опционы', years: '3-4 года', level: 'Senior', levelShort: 'SN' },
          lead: { salary: '160-220k', bonus: 'бонусы', years: '4-5 лет', level: 'Team Lead', levelShort: 'TL' }
        },
        consultant: {
          intern: { salary: '35-45k', bonus: 'обучение', years: '0-1 год', level: 'Стажер', levelShort: 'СТ' },
          junior: { salary: '60-80k', bonus: 'ментор', years: '1-2 года', level: 'Консультант', levelShort: 'КН' },
          middle: { salary: '90-130k', bonus: 'премии', years: '2-3 года', level: 'Ведущий', levelShort: 'ВД' },
          senior: { salary: '130-170k', bonus: 'опционы', years: '3-4 года', level: 'Старший', levelShort: 'СТ' },
          lead: { salary: '170-230k', bonus: 'бонусы', years: '4-5 лет', level: 'Руководитель', levelShort: 'РК' }
        },
        analyst: {
          intern: { salary: '40-50k', bonus: 'обучение', years: '0-1 год', level: 'Стажер', levelShort: 'СТ' },
          junior: { salary: '70-90k', bonus: 'ментор', years: '1-2 года', level: 'Аналитик', levelShort: 'АН' },
          middle: { salary: '100-140k', bonus: 'премии', years: '2-3 года', level: 'Старший', levelShort: 'СТ' },
          senior: { salary: '140-180k', bonus: 'опционы', years: '3-4 года', level: 'Ведущий', levelShort: 'ВД' },
          lead: { salary: '180-250k', bonus: 'бонусы', years: '4-5 лет', level: 'Руководитель', levelShort: 'РК' }
        }
      }
    }
  },
  computed: {
    careerStages() {
      const path = this.careerPaths[this.careerPath];
      const levels = ['intern', 'junior', 'middle', 'senior', 'lead'];
      const currentIndex = levels.indexOf(this.currentLevel);
      
      return levels.slice(currentIndex).map((level, index) => {
        const stage = path[level];
        const years = index * this.growthSpeed;
        
        return {
          ...stage,
          years: years === 0 ? 'Сейчас' : `Через ${years} ${this.getYearsText(years)}`,
          chartHeight: 20 + (index * 15),
          levelShort: stage.levelShort
        };
      });
    },
    
    fiveYearSalary() {
      const lastStage = this.careerStages[this.careerStages.length - 1];
      return lastStage ? lastStage.salary : '150-200k';
    },
    
    growthTip() {
      if (this.growthSpeed <= 1) {
        return 'Активное обучение + участие в сложных проектах ускорят рост';
      } else if (this.growthSpeed <= 2) {
        return 'Стабильное развитие с балансом работы и обучения';
      } else {
        return 'Глубокое погружение в технологии гарантирует устойчивый рост';
      }
    }
  },
  methods: {
    addSmoothScroll() {
      const links = document.querySelectorAll('a[href^="#"]');
      links.forEach(link => {
        link.addEventListener('click', (e) => {
          e.preventDefault();
          const target = document.querySelector(link.getAttribute('href'));
          if (target) {
            target.scrollIntoView({ behavior: 'smooth' });
          }
        });
      });
    },
    addScrollAnimations() {
      console.log('Scroll animations ready');
    },
    getYearsText(years) {
      if (years === 1) return 'год';
      if (years >= 2 && years <= 4) return 'года';
      return 'лет';
    }
  },
  mounted() {
    this.addSmoothScroll();
    this.addScrollAnimations();
  }
}
</script>

<style scoped>
.stagger-animation > * {
  opacity: 0;
  transform: translateY(30px);
  animation: fadeInUp 0.8s ease-out forwards;
}

.stagger-animation > *:nth-child(1) { animation-delay: 0.1s; }
.stagger-animation > *:nth-child(2) { animation-delay: 0.2s; }
.stagger-animation > *:nth-child(3) { animation-delay: 0.3s; }
.stagger-animation > *:nth-child(4) { animation-delay: 0.4s; }
.stagger-animation > *:nth-child(5) { animation-delay: 0.5s; }

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(50px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.glass-effect {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.slider-red::-webkit-slider-thumb {
  appearance: none;
  height: 20px;
  width: 20px;
  border-radius: 50%;
  background: #DC2626;
  cursor: pointer;
  border: 2px solid white;
  box-shadow: 0 2px 6px rgba(0,0,0,0.2);
}

.slider-red::-moz-range-thumb {
  height: 20px;
  width: 20px;
  border-radius: 50%;
  background: #DC2626;
  cursor: pointer;
  border: 2px solid white;
  box-shadow: 0 2px 6px rgba(0,0,0,0.2);
}
</style>