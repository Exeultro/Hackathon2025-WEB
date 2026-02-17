<template>
  <div class="min-h-screen bg-gray-50">
    <!-- Header -->
    <AppHeader />
    
    <main class="pt-20">
      
      <!-- Hero Section -->
      <section class="relative py-16 bg-gradient-to-br from-apogee-red to-apogee-darkRed text-white overflow-hidden">
        <div class="absolute inset-0 russian-pattern opacity-20"></div>
        
        <div class="container mx-auto px-6 relative z-10">
          <div class="max-w-4xl mx-auto text-center">
            <h1 class="text-4xl md:text-5xl font-bold mb-6 font-display">Карьера в Апогее</h1>
            <p class="text-xl text-white/90 leading-relaxed">
              Присоединяйся к команде, которая создает технологии для будущего России
            </p>
          </div>
        </div>
      </section>

      <!-- Анимация -->
      <TrainAnimation />

      <!-- Фильтры вакансий -->
      <section class="py-12 bg-white">
        <div class="container mx-auto px-6">
          <div class="flex flex-col lg:flex-row gap-6 items-center justify-between">
            <div class="flex flex-wrap gap-4">
              <button 
                v-for="filter in filters" 
                :key="filter.id"
                @click="setActiveFilter(filter.id)"
                :class="[
                  'px-6 py-3 rounded-xl font-semibold transition-all duration-300',
                  activeFilter === filter.id 
                    ? 'bg-apogee-red text-white shadow-lg' 
                    : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                ]"
              >
                {{ filter.name }}
              </button>
            </div>
            
            <div class="flex items-center space-x-4">
              <span class="text-gray-600 font-medium">Найдено вакансий: {{ filteredVacancies.length }}</span>
            </div>
          </div>
        </div>
      </section>

      <!-- Список вакансий -->
      <section class="py-12 bg-gray-50">
        <div class="container mx-auto px-6">
          <!-- Индикатор загрузки -->
          <div v-if="isLoading" class="text-center py-12">
            <div class="inline-flex items-center">
              <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-apogee-red"></div>
              <span class="ml-4 text-gray-600">Загружаем вакансии...</span>
            </div>
          </div>

          <!-- Список вакансий -->
          <div v-else-if="filteredVacancies.length > 0" class="grid gap-8">
            <!-- Вакансия -->
            <div v-for="vacancy in filteredVacancies" :key="vacancy.id"
                 class="bg-white rounded-2xl shadow-lg border border-gray-100 overflow-hidden hover:shadow-xl transition-all duration-300">
              <div class="p-8">
                <div class="flex flex-col lg:flex-row lg:items-start lg:justify-between gap-6">
                  <!-- Основная информация -->
                  <div class="flex-1">
                    <div class="flex items-start justify-between mb-4">
                      <div>
                        <h3 class="text-2xl font-bold text-apogee-dark mb-2">{{ vacancy.title }}</h3>
                        <div class="flex flex-wrap gap-2 mb-4">
                          <span class="px-3 py-1 bg-red-100 text-apogee-red rounded-full text-sm font-semibold">
                            {{ getLevelDisplay(vacancy.level) }}
                          </span>
                          <span class="px-3 py-1 bg-blue-100 text-blue-600 rounded-full text-sm font-semibold">
                            {{ getTypeDisplay(vacancy.type) }}
                          </span>
                          <span class="px-3 py-1 bg-green-100 text-green-600 rounded-full text-sm font-semibold">
                            {{ vacancy.city }}
                          </span>
                          <span v-if="vacancy.is_internship" class="px-3 py-1 bg-purple-100 text-purple-600 rounded-full text-sm font-semibold">
                            🎓 Практика
                          </span>
                        </div>
                      </div>
                      <div class="text-right">
                        <div class="text-2xl font-bold text-apogee-red mb-1">{{ getSalaryDisplay(vacancy) }}</div>
                        <div class="text-sm text-gray-500">зарплата</div>
                      </div>
                    </div>

                    <!-- Описание -->
                    <p class="text-gray-700 mb-6 leading-relaxed">{{ vacancy.description }}</p>

                    <!-- Требования -->
                    <div class="mb-6">
                      <h4 class="font-semibold text-gray-800 mb-3">Требования:</h4>
                      <ul class="grid md:grid-cols-2 gap-2">
                        <li v-for="requirement in vacancy.requirements" :key="requirement"
                            class="flex items-center text-gray-600 text-sm">
                          <span class="w-1.5 h-1.5 bg-apogee-red rounded-full mr-3"></span>
                          {{ requirement }}
                        </li>
                      </ul>
                    </div>

                    <!-- Бонусы -->
                    <div class="flex flex-wrap gap-3">
                      <div v-for="benefit in vacancy.benefits" :key="benefit"
                           class="flex items-center space-x-2 text-sm text-gray-600">
                        <span class="text-green-500">✓</span>
                        <span>{{ benefit }}</span>
                      </div>
                    </div>
                  </div>

                  <!-- Боковая панель с кнопками -->
                  <div class="lg:w-80 flex-shrink-0">
                    <div class="bg-gray-50 rounded-xl p-6">
                      <div class="text-center mb-4">
                        <div class="text-sm text-gray-600 mb-2">Откликов сегодня</div>
                        <div class="text-2xl font-bold text-apogee-red">{{ vacancy.applications_today || 0 }}</div>
                      </div>
                      
                      <!-- Умные кнопки в зависимости от типа вакансии -->
                      <template v-if="vacancy.is_internship && hasActiveInternshipPeriod(vacancy)">
                        <!-- Кнопка ЗАПИСЬ НА ПРАКТИКУ -->
                        <button 
                          @click="openApplicationModal(vacancy, 'internship')"
                          class="w-full bg-gradient-to-r from-green-500 to-green-600 text-white py-4 rounded-xl font-semibold hover:from-green-600 hover:to-green-700 transition-all duration-300 shadow-lg hover:shadow-xl mb-3 flex items-center justify-center space-x-2"
                        >
                          <span>🎓</span>
                          <span>Запись на практику</span>
                        </button>
                        <div class="text-xs text-green-600 text-center mb-3">
                          До {{ getInternshipDeadline(vacancy) }}
                        </div>
                      </template>
                      
                      <!-- Кнопка ОТКЛИКНУТЬСЯ -->
                      <button 
                        @click="openApplicationModal(vacancy, 'regular')"
                        class="w-full bg-apogee-red text-white py-4 rounded-xl font-semibold hover:bg-apogee-darkRed transition-all duration-300 shadow-lg hover:shadow-xl mb-3 flex items-center justify-center space-x-2"
                      >
                        <span>💼</span>
                        <span>Откликнуться</span>
                      </button>
                      
                      <!-- Кнопка ПОДРОБНЕЕ О ВАКАНСИИ -->
                      <button 
                        @click="showVacancyDetails(vacancy)"
                        class="w-full border-2 border-apogee-red text-apogee-red py-3 rounded-xl font-semibold hover:bg-apogee-red hover:text-white transition-all duration-300 flex items-center justify-center space-x-2"
                      >
                        <span>📋</span>
                        <span>Подробнее о вакансии</span>
                      </button>
                    </div>
                  </div>
                </div>

                <!-- Бейдж доступной практики -->
                <div v-if="vacancy.is_internship && hasActiveInternshipPeriod(vacancy)" 
                     class="mt-4 flex items-center justify-between bg-green-50 border border-green-200 rounded-lg p-4">
                  <div class="flex items-center space-x-3">
                    <span class="text-green-600">🎯</span>
                    <div>
                      <div class="font-semibold text-green-800">Доступна запись на практику</div>
                      <div class="text-sm text-green-600">
                        {{ getInternshipPeriodInfo(vacancy) }}
                      </div>
                    </div>
                  </div>
                  <div class="text-right">
                    <div class="text-sm text-green-600">Свободно мест:</div>
                    <div class="font-bold text-green-800">{{ getAvailableSlots(vacancy) }}</div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Сообщение если нет вакансий -->
          <div v-else class="text-center py-16">
            <div class="w-24 h-24 mx-auto mb-6 bg-gray-100 rounded-full flex items-center justify-center">
              <span class="text-3xl">🔍</span>
            </div>
            <h3 class="text-2xl font-bold text-gray-600 mb-4">Вакансии не найдены</h3>
            <p class="text-gray-500 max-w-md mx-auto">
              Попробуйте изменить параметры фильтра или загляните позже
            </p>
          </div>
        </div>
      </section>

      <!-- Преимущества работы -->
      <section class="py-20 bg-white">
        <div class="container mx-auto px-6">
          <div class="text-center mb-16">
            <h2 class="text-4xl md:text-5xl font-bold text-apogee-dark mb-6 font-display">
              Почему выбирают <span class="gradient-text">Апогей</span>?
            </h2>
          </div>

          <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
            <div v-for="benefit in benefits" :key="benefit.title"
                 class="text-center group">
              <div class="w-20 h-20 mx-auto mb-6 rounded-2xl bg-apogee-red flex items-center justify-center text-white text-2xl group-hover:scale-110 transition-transform duration-300">
                {{ benefit.icon }}
              </div>
              <h3 class="text-xl font-bold text-apogee-dark mb-4">{{ benefit.title }}</h3>
              <p class="text-gray-600">{{ benefit.description }}</p>
            </div>
          </div>
        </div>
      </section>

    </main>

    <!-- Модальное окно заявки на ПРАКТИКУ -->
    <div v-if="showApplicationModal && applicationType === 'internship'" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
      <div class="bg-white rounded-2xl max-w-2xl w-full max-h-[90vh] overflow-y-auto">
        <div class="sticky top-0 bg-white border-b border-gray-200 p-6 rounded-t-2xl flex justify-between items-center">
          <div>
            <h2 class="text-2xl font-bold text-apogee-dark">Заявка на практику</h2>
            <p class="text-gray-600 mt-1">{{ selectedVacancy?.title }}</p>
          </div>
          <button @click="closeApplicationModal" class="text-gray-400 hover:text-gray-600 text-2xl">
            ×
          </button>
        </div>

        <div class="p-6">
          <!-- Информация о периоде практики -->
          <div v-if="selectedInternshipPeriod" 
               class="mb-6 p-4 bg-green-50 border border-green-200 rounded-xl">
            <h3 class="font-semibold text-green-800 mb-2">Информация о практике:</h3>
            <p class="text-green-700">{{ selectedInternshipPeriod.name }}</p>
            <p class="text-sm text-green-600">
              Период: {{ formatDate(selectedInternshipPeriod.start_date) }} - {{ formatDate(selectedInternshipPeriod.end_date) }}
            </p>
          </div>

          <form @submit.prevent="submitApplication">
            <!-- Студенческая информация -->
            <div class="mb-6 p-4 bg-blue-50 border border-blue-200 rounded-xl">
              <h3 class="font-semibold text-blue-800 mb-3 flex items-center space-x-2">
                <span>🎓</span>
                <span>Информация о студенте</span>
              </h3>
              
              <div class="grid md:grid-cols-2 gap-4 mb-4">
                <div>
                  <label class="block text-sm font-semibold text-gray-700 mb-2">Фамилия *</label>
                  <input 
                    v-model="applicationForm.lastName"
                    type="text" 
                    required
                    class="w-full p-3 border-2 border-gray-300 rounded-xl focus:border-apogee-red focus:ring-2 focus:ring-red-100 transition-all duration-300"
                    placeholder="Иванов"
                  >
                </div>
                <div>
                  <label class="block text-sm font-semibold text-gray-700 mb-2">Имя *</label>
                  <input 
                    v-model="applicationForm.firstName"
                    type="text" 
                    required
                    class="w-full p-3 border-2 border-gray-300 rounded-xl focus:border-apogee-red focus:ring-2 focus:ring-red-100 transition-all duration-300"
                    placeholder="Иван"
                  >
                </div>
              </div>

              <div class="grid md:grid-cols-2 gap-4 mb-4">
                <div>
                  <label class="block text-sm font-semibold text-gray-700 mb-2">Отчество</label>
                  <input 
                    v-model="applicationForm.middleName"
                    type="text" 
                    class="w-full p-3 border-2 border-gray-300 rounded-xl focus:border-apogee-red focus:ring-2 focus:ring-red-100 transition-all duration-300"
                    placeholder="Иванович"
                  >
                </div>
                <div>
                  <label class="block text-sm font-semibold text-gray-700 mb-2">Email *</label>
                  <input 
                    v-model="applicationForm.email"
                    type="email" 
                    required
                    class="w-full p-3 border-2 border-gray-300 rounded-xl focus:border-apogee-red focus:ring-2 focus:ring-red-100 transition-all duration-300"
                    placeholder="ivanov@example.com"
                  >
                </div>
              </div>

              <div class="grid md:grid-cols-2 gap-4">
                <div>
                  <label class="block text-sm font-semibold text-gray-700 mb-2">Телефон *</label>
                  <input 
                    v-model="applicationForm.phone"
                    type="tel" 
                    required
                    class="w-full p-3 border-2 border-gray-300 rounded-xl focus:border-apogee-red focus:ring-2 focus:ring-red-100 transition-all duration-300"
                    placeholder="+7 (999) 999-99-99"
                  >
                </div>
                <div>
                  <label class="block text-sm font-semibold text-gray-700 mb-2">Город *</label>
                  <input 
                    v-model="applicationForm.city"
                    type="text" 
                    required
                    class="w-full p-3 border-2 border-gray-300 rounded-xl focus:border-apogee-red focus:ring-2 focus:ring-red-100 transition-all duration-300"
                    placeholder="Красноярск"
                  >
                </div>
              </div>
            </div>

            <!-- Образование -->
            <div class="mb-6 p-4 bg-green-50 border border-green-200 rounded-xl">
              <h3 class="font-semibold text-green-800 mb-3 flex items-center space-x-2">
                <span>📚</span>
                <span>Образовательная информация</span>
              </h3>

              <div class="mb-4">
                <label class="block text-sm font-semibold text-gray-700 mb-2">Учебное заведение *</label>
                <input 
                  v-model="applicationForm.education"
                  type="text" 
                  required
                  class="w-full p-3 border-2 border-gray-300 rounded-xl focus:border-apogee-red focus:ring-2 focus:ring-red-100 transition-all duration-300"
                  placeholder="Сибирский федеральный университет"
                >
              </div>

              <div class="grid md:grid-cols-2 gap-4 mb-4">
                <div>
                  <label class="block text-sm font-semibold text-gray-700 mb-2">Факультет *</label>
                  <input 
                    v-model="applicationForm.faculty"
                    type="text" 
                    required
                    class="w-full p-3 border-2 border-gray-300 rounded-xl focus:border-apogee-red focus:ring-2 focus:ring-red-100 transition-all duration-300"
                    placeholder="Институт информатики"
                  >
                </div>
                <div>
                  <label class="block text-sm font-semibold text-gray-700 mb-2">Курс *</label>
                  <select 
                    v-model="applicationForm.course"
                    required
                    class="w-full p-3 border-2 border-gray-300 rounded-xl focus:border-apogee-red focus:ring-2 focus:ring-red-100 transition-all duration-300"
                  >
                    <option value="">Выберите курс</option>
                    <option value="1">1 курс</option>
                    <option value="2">2 курс</option>
                    <option value="3">3 курс</option>
                    <option value="4">4 курс</option>
                    <option value="5">5 курс</option>
                    <option value="6">Магистратура</option>
                  </select>
                </div>
              </div>

              <!-- Период практики -->
              <div>
                <label class="block text-sm font-semibold text-gray-700 mb-2">Предпочтительный период практики *</label>
                <select 
                  v-model="applicationForm.preferred_period"
                  required
                  class="w-full p-3 border-2 border-gray-300 rounded-xl focus:border-apogee-red focus:ring-2 focus:ring-red-100 transition-all duration-300"
                >
                  <option value="">Выберите период</option>
                  <option v-for="period in internshipPeriods" 
                          :key="period.id" 
                          :value="period.id">
                    {{ period.name }} ({{ formatDate(period.start_date) }} - {{ formatDate(period.end_date) }})
                  </option>
                </select>
              </div>
            </div>

            <!-- Дополнительная информация -->
            <div class="mb-6">
              <label class="block text-sm font-semibold text-gray-700 mb-2">Опыт работы/учебные проекты</label>
              <textarea 
                v-model="applicationForm.experience"
                rows="4"
                class="w-full p-3 border-2 border-gray-300 rounded-xl focus:border-apogee-red focus:ring-2 focus:ring-red-100 transition-all duration-300 resize-none"
                placeholder="Опишите ваш опыт работы, учебные проекты, участие в хакатонах, курсовые работы..."
              ></textarea>
            </div>

            <div class="mb-6">
              <label class="block text-sm font-semibold text-gray-700 mb-2">Почему вы хотите пройти практику в Апогее? *</label>
              <textarea 
                v-model="applicationForm.motivation"
                rows="3"
                required
                class="w-full p-3 border-2 border-gray-300 rounded-xl focus:border-apogee-red focus:ring-2 focus:ring-red-100 transition-all duration-300 resize-none"
                placeholder="Расскажите о вашей мотивации пройти практику, какие навыки хотите получить..."
              ></textarea>
            </div>

            <!-- Кнопки -->
            <div class="flex flex-col sm:flex-row gap-4 pt-6 border-t border-gray-200">
              <button 
                type="submit"
                class="flex-1 bg-gradient-to-r from-green-500 to-green-600 text-white py-4 rounded-xl font-semibold hover:from-green-600 hover:to-green-700 transition-all duration-300 shadow-lg hover:shadow-xl flex items-center justify-center space-x-2"
                :disabled="isSubmitting"
              >
                <span v-if="isSubmitting" class="animate-spin">⏳</span>
                <span v-else>🎓</span>
                <span>{{ isSubmitting ? 'Отправка...' : 'Подать заявку на практику' }}</span>
              </button>
              <button 
                type="button"
                @click="closeApplicationModal"
                class="flex-1 border-2 border-gray-400 text-gray-600 py-4 rounded-xl font-semibold hover:bg-gray-400 hover:text-white transition-all duration-300"
              >
                Отмена
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>

    <!-- Модальное окно ОТКЛИКА на вакансию -->
    <div v-if="showApplicationModal && applicationType === 'regular'" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
      <div class="bg-white rounded-2xl max-w-2xl w-full max-h-[90vh] overflow-y-auto">
        <div class="sticky top-0 bg-white border-b border-gray-200 p-6 rounded-t-2xl flex justify-between items-center">
          <div>
            <h2 class="text-2xl font-bold text-apogee-dark">Отклик на вакансию</h2>
            <p class="text-gray-600 mt-1">{{ selectedVacancy?.title }}</p>
          </div>
          <button @click="closeApplicationModal" class="text-gray-400 hover:text-gray-600 text-2xl">
            ×
          </button>
        </div>

        <div class="p-6">
          <form @submit.prevent="submitApplication">
          <!-- В форме ОТКЛИКА на вакансию (applicationType === 'regular') -->
          <div class="mb-6 p-4 bg-blue-50 border border-blue-200 rounded-xl">
            <h3 class="font-semibold text-blue-800 mb-3 flex items-center space-x-2">
              <span>👤</span>
              <span>Персональные данные</span>
            </h3>
            
            <div class="grid md:grid-cols-2 gap-4 mb-4">
              <div>
                <label class="block text-sm font-semibold text-gray-700 mb-2">Фамилия *</label>
                <input 
                  v-model="applicationForm.lastName"
                  type="text" 
                  required
                  class="w-full p-3 border-2 border-gray-300 rounded-xl focus:border-apogee-red focus:ring-2 focus:ring-red-100 transition-all duration-300"
                  placeholder="Иванов"
                >
              </div>
              <div>
                <label class="block text-sm font-semibold text-gray-700 mb-2">Имя *</label>
                <input 
                  v-model="applicationForm.firstName"
                  type="text" 
                  required
                  class="w-full p-3 border-2 border-gray-300 rounded-xl focus:border-apogee-red focus:ring-2 focus:ring-red-100 transition-all duration-300"
                  placeholder="Иван"
                >
              </div>
            </div>

            <div class="grid md:grid-cols-2 gap-4 mb-4">
              <div>
                <label class="block text-sm font-semibold text-gray-700 mb-2">Email *</label>
                <input 
                  v-model="applicationForm.email"
                  type="email" 
                  required
                  class="w-full p-3 border-2 border-gray-300 rounded-xl focus:border-apogee-red focus:ring-2 focus:ring-red-100 transition-all duration-300"
                  placeholder="ivanov@example.com"
                >
              </div>
              <div>
                <label class="block text-sm font-semibold text-gray-700 mb-2">Телефон *</label>
                <input 
                  v-model="applicationForm.phone"
                  type="tel" 
                  required
                  class="w-full p-3 border-2 border-gray-300 rounded-xl focus:border-apogee-red focus:ring-2 focus:ring-red-100 transition-all duration-300"
                  placeholder="+7 (999) 999-99-99"
                >
              </div>
            </div>

            <!-- ✅ ДОБАВЛЕНО ПОЛЕ ГОРОДА -->
            <div>
              <label class="block text-sm font-semibold text-gray-700 mb-2">Город *</label>
              <input 
                v-model="applicationForm.city"
                type="text" 
                required
                class="w-full p-3 border-2 border-gray-300 rounded-xl focus:border-apogee-red focus:ring-2 focus:ring-red-100 transition-all duration-300"
                placeholder="Москва"
              >
            </div>
          </div>

            <!-- Профессиональная информация -->
            <div class="mb-6">
              <label class="block text-sm font-semibold text-gray-700 mb-2">Опыт работы *</label>
              <textarea 
                v-model="applicationForm.experience"
                rows="4"
                required
                class="w-full p-3 border-2 border-gray-300 rounded-xl focus:border-apogee-red focus:ring-2 focus:ring-red-100 transition-all duration-300 resize-none"
                placeholder="Опишите ваш профессиональный опыт, ключевые проекты, достижения..."
              ></textarea>
            </div>

            <div class="mb-6">
              <label class="block text-sm font-semibold text-gray-700 mb-2">Почему вы хотите работать в Апогее? *</label>
              <textarea 
                v-model="applicationForm.motivation"
                rows="3"
                required
                class="w-full p-3 border-2 border-gray-300 rounded-xl focus:border-apogee-red focus:ring-2 focus:ring-red-100 transition-all duration-300 resize-none"
                placeholder="Расскажите о вашей мотивации, почему выбрали нашу компанию..."
              ></textarea>
            </div>

            <!-- Резюме -->
            <div class="mb-6">
              <label class="block text-sm font-semibold text-gray-700 mb-2">Ссылка на резюме (опционально)</label>
              <input 
                v-model="applicationForm.resume_url"
                type="url"
                class="w-full p-3 border-2 border-gray-300 rounded-xl focus:border-apogee-red focus:ring-2 focus:ring-red-100 transition-all duration-300"
                placeholder="https://hh.ru/resume/..."
              >
            </div>

            <!-- Кнопки -->
            <div class="flex flex-col sm:flex-row gap-4 pt-6 border-t border-gray-200">
              <button 
                type="submit"
                class="flex-1 bg-apogee-red text-white py-4 rounded-xl font-semibold hover:bg-apogee-darkRed transition-all duration-300 shadow-lg hover:shadow-xl flex items-center justify-center space-x-2"
                :disabled="isSubmitting"
              >
                <span v-if="isSubmitting" class="animate-spin">⏳</span>
                <span v-else>💼</span>
                <span>{{ isSubmitting ? 'Отправка...' : 'Отправить отклик' }}</span>
              </button>
              <button 
                type="button"
                @click="closeApplicationModal"
                class="flex-1 border-2 border-gray-400 text-gray-600 py-4 rounded-xl font-semibold hover:bg-gray-400 hover:text-white transition-all duration-300"
              >
                Отмена
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>

    <!-- Модальное окно ПОДРОБНЕЕ О ВАКАНСИИ -->
    <div v-if="showVacancyDetailsModal" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
      <div class="bg-white rounded-2xl max-w-4xl w-full max-h-[90vh] overflow-y-auto">
        <div class="sticky top-0 bg-white border-b border-gray-200 p-6 rounded-t-2xl flex justify-between items-center">
          <div>
            <h2 class="text-2xl font-bold text-apogee-dark">Подробнее о вакансии</h2>
            <p class="text-gray-600 mt-1">{{ selectedVacancy?.title }}</p>
          </div>
          <button @click="closeVacancyDetails" class="text-gray-400 hover:text-gray-600 text-2xl">
            ×
          </button>
        </div>

        <div class="p-6">
          <div v-if="selectedVacancy" class="space-y-6">
            <!-- Основная информация -->
            <div class="grid md:grid-cols-2 gap-6">
              <div>
                <h3 class="text-lg font-semibold text-gray-800 mb-3">Общая информация</h3>
                <div class="space-y-2">
                  <div class="flex justify-between">
                    <span class="text-gray-600">Уровень:</span>
                    <span class="font-semibold">{{ getLevelDisplay(selectedVacancy.level) }}</span>
                  </div>
                  <div class="flex justify-between">
                    <span class="text-gray-600">Тип работы:</span>
                    <span class="font-semibold">{{ getTypeDisplay(selectedVacancy.type) }}</span>
                  </div>
                  <div class="flex justify-between">
                    <span class="text-gray-600">Город:</span>
                    <span class="font-semibold">{{ selectedVacancy.city }}</span>
                  </div>
                  <div class="flex justify-between">
                    <span class="text-gray-600">Зарплата:</span>
                    <span class="font-semibold text-apogee-red">{{ getSalaryDisplay(selectedVacancy) }}</span>
                  </div>
                </div>
              </div>
              
              <div>
                <h3 class="text-lg font-semibold text-gray-800 mb-3">Статистика</h3>
                <div class="space-y-2">
                  <div class="flex justify-between">
                    <span class="text-gray-600">Откликов сегодня:</span>
                    <span class="font-semibold">{{ selectedVacancy.applications_today || 0 }}</span>
                  </div>
                  <div class="flex justify-between">
                    <span class="text-gray-600">Всего откликов:</span>
                    <span class="font-semibold">{{ selectedVacancy.application_count || 0 }}</span>
                  </div>
                  <div v-if="selectedVacancy.is_internship" class="flex justify-between">
                    <span class="text-gray-600">Свободных мест:</span>
                    <span class="font-semibold text-green-600">{{ getAvailableSlots(selectedVacancy) }}</span>
                  </div>
                </div>
              </div>
            </div>

            <!-- Полное описание -->
            <div>
              <h3 class="text-lg font-semibold text-gray-800 mb-3">Описание вакансии</h3>
              <p class="text-gray-700 leading-relaxed">{{ selectedVacancy.full_description || selectedVacancy.description }}</p>
            </div>

            <!-- Обязанности -->
            <div v-if="selectedVacancy.responsibilities && selectedVacancy.responsibilities.length > 0">
              <h3 class="text-lg font-semibold text-gray-800 mb-3">Обязанности</h3>
              <ul class="space-y-2">
                <li v-for="(responsibility, index) in selectedVacancy.responsibilities" :key="index"
                    class="flex items-start text-gray-700">
                  <span class="w-1.5 h-1.5 bg-apogee-red rounded-full mt-2 mr-3 flex-shrink-0"></span>
                  <span>{{ responsibility }}</span>
                </li>
              </ul>
            </div>

            <!-- Условия работы -->
            <div v-if="selectedVacancy.work_conditions && selectedVacancy.work_conditions.length > 0">
              <h3 class="text-lg font-semibold text-gray-800 mb-3">Условия работы</h3>
              <div class="grid md:grid-cols-2 gap-4">
                <div v-for="condition in selectedVacancy.work_conditions" :key="condition"
                     class="flex items-center space-x-2 text-gray-700">
                  <span class="text-green-500">✓</span>
                  <span>{{ condition }}</span>
                </div>
              </div>
            </div>

            <!-- Процесс отбора -->
            <div v-if="selectedVacancy.selection_process && selectedVacancy.selection_process.length > 0">
              <h3 class="text-lg font-semibold text-gray-800 mb-3">Процесс отбора</h3>
              <div class="space-y-3">
                <div v-for="(stage, index) in selectedVacancy.selection_process" :key="index"
                     class="flex items-center space-x-4 p-3 bg-gray-50 rounded-lg">
                  <div class="w-8 h-8 bg-apogee-red rounded-full flex items-center justify-center text-white text-sm font-semibold">
                    {{ index + 1 }}
                  </div>
                  <div>
                    <div class="font-semibold text-gray-800">{{ stage.title || `Этап ${index + 1}` }}</div>
                    <div class="text-sm text-gray-600">{{ stage.description || stage }}</div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Кнопки действий -->
            <div class="flex flex-col sm:flex-row gap-4 pt-6 border-t border-gray-200">
              <button 
                v-if="selectedVacancy.is_internship && hasActiveInternshipPeriod(selectedVacancy)"
                @click="openApplicationModal(selectedVacancy, 'internship')"
                class="flex-1 bg-gradient-to-r from-green-500 to-green-600 text-white py-4 rounded-xl font-semibold hover:from-green-600 hover:to-green-700 transition-all duration-300 shadow-lg hover:shadow-xl flex items-center justify-center space-x-2"
              >
                <span>🎓</span>
                <span>Записаться на практику</span>
              </button>
              <button 
                @click="openApplicationModal(selectedVacancy, 'regular')"
                class="flex-1 bg-apogee-red text-white py-4 rounded-xl font-semibold hover:bg-apogee-darkRed transition-all duration-300 shadow-lg hover:shadow-xl flex items-center justify-center space-x-2"
              >
                <span>💼</span>
                <span>Откликнуться на вакансию</span>
              </button>
              <button 
                @click="closeVacancyDetails"
                class="flex-1 border-2 border-gray-400 text-gray-600 py-4 rounded-xl font-semibold hover:bg-gray-400 hover:text-white transition-all duration-300"
              >
                Закрыть
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import AppHeader from '@/components/Header.vue'
import TrainAnimation from '@/components/TrainAnimation.vue'
import { vacanciesAPI, internshipAPI } from '@/services/api'
export default {
  name: 'CareersPage',
  components: {
    AppHeader,
    TrainAnimation
  },
  data() {
    return {
      activeFilter: 'all',
      showApplicationModal: false,
      showVacancyDetailsModal: false,
      selectedVacancy: null,
      applicationType: 'regular',
      isSubmitting: false,
      isLoading: false,
      
      applicationForm: {
        lastName: '',
        firstName: '',
        middleName: '',
        email: '',
        phone: '',
        city: '',
        education: '',
        faculty: '',
        course: '',
        preferred_period: '',
        experience: '',
        motivation: '',
        resume_url: ''
      },
      
      vacancyIds: {
      programmer_internship: null,
      programmer_regular: null,
      consultant_internship: null,
      consultant_regular: null
      },

      filters: [
        { id: 'all', name: 'Все вакансии' },
        { id: 'intern', name: 'Стажировки' },
        { id: 'junior', name: 'Junior' },
        { id: 'middle', name: 'Middle' },
        { id: 'senior', name: 'Senior' },
        { id: 'remote', name: 'Удаленная работа' }
      ],
      vacancies: [],
      benefits: [
        {
          icon: '🎓',
          title: 'Обучение и рост',
          description: 'Оплачиваемые сертификации и программы развития'
        },
        {
          icon: '💼',
          title: 'Карьера',
          description: 'Четкий карьерный путь от стажера до руководителя'
        },
        {
          icon: '🏠',
          title: 'Гибкий график',
          description: 'Возможность совмещать работу с учебой'
        },
        {
          icon: '🚀',
          title: 'Интересные задачи',
          description: 'Работа над проектами федерального масштаба'
        }
      ],
      internshipPeriods: [],
      availableFilters: {}
    }
  },
  computed: {
    filteredVacancies() {
      if (this.activeFilter === 'all') {
        return this.vacancies
      }
      return this.vacancies.filter(vacancy => {
        const levelMatch = vacancy.level.toLowerCase().includes(this.activeFilter)
        const typeMatch = vacancy.type.toLowerCase().includes(this.activeFilter)
        const internshipMatch = this.activeFilter === 'intern' && vacancy.is_internship
        
        return levelMatch || typeMatch || internshipMatch
      })
    },
    selectedInternshipPeriod() {
      if (this.applicationType === 'internship' && this.applicationForm.preferred_period) {
        return this.internshipPeriods.find(p => p.id === this.applicationForm.preferred_period)
      }
      return null
    }
  },
  async mounted() {
    await this.loadVacancies()
    await this.loadFilters()
    await this.loadInternshipPeriods()
  },
  methods: {
    async loadVacancies() {
      this.isLoading = true
      try {
        const response = await vacanciesAPI.getVacancies()
        this.vacancies = response.data.results || response.data
      } catch (error) {
        console.error('Ошибка загрузки вакансий:', error)
        this.vacancies = this.getMockVacancies()
      } finally {
        this.isLoading = false
      }
    },

    async loadFilters() {
      try {
        const response = await vacanciesAPI.getFilters()
        this.availableFilters = response.data
      } catch (error) {
        console.error('Ошибка загрузки фильтров:', error)
      }
    },

    async loadInternshipPeriods() {
      try {
        const response = await internshipAPI.getPeriods()
        this.internshipPeriods = response.data.results || response.data
      } catch (error) {
        console.error('Ошибка загрузки периодов практики:', error)
      }
    },

    setActiveFilter(filterId) {
      this.activeFilter = filterId
    },

    hasActiveInternshipPeriod(vacancy) {
      if (!vacancy.is_internship) return false
      return vacancy.internship_periods && vacancy.internship_periods.length > 0
    },

    getInternshipDeadline(vacancy) {
      const periods = vacancy.internship_periods || []
      if (periods.length > 0 && periods[0].internship_period) {
        return this.formatDate(periods[0].internship_period.application_deadline)
      }
      return 'скоро'
    },

    getInternshipPeriodInfo(vacancy) {
      const periods = vacancy.internship_periods || []
      if (periods.length > 0 && periods[0].internship_period) {
        const period = periods[0].internship_period
        return `${period.name} (до ${this.formatDate(period.application_deadline)})`
      }
      return 'Доступны периоды практики'
    },

    getAvailableSlots(vacancy) {
      if (!vacancy.is_internship) return 0
      const periods = vacancy.internship_periods || []
      if (periods.length > 0) {
        return periods[0].remaining_slots || 5
      }
      return 5
    },

    getLevelDisplay(level) {
      const levels = {
        'intern': 'Стажировка',
        'junior': 'Junior',
        'middle': 'Middle', 
        'senior': 'Senior',
        'lead': 'Team Lead'
      }
      return levels[level] || level
    },

    getTypeDisplay(type) {
      const types = {
        'onsite': 'Очная',
        'remote': 'Удаленная',
        'hybrid': 'Гибрид'
      }
      return types[type] || type
    },

    getSalaryDisplay(vacancy) {
      if (vacancy.salary_from && vacancy.salary_to) {
        return `от ${vacancy.salary_from} до ${vacancy.salary_to} ₽`
      } else if (vacancy.salary_from) {
        return `от ${vacancy.salary_from} ₽`
      } else if (vacancy.salary_to) {
        return `до ${vacancy.salary_to} ₽`
      } else {
        return 'по договоренности'
      }
    },

    formatDate(dateString) {
      try {
        return new Date(dateString).toLocaleDateString('ru-RU')
      } catch (error) {
        return 'скоро'
      }
    },

    openApplicationModal(vacancy, type) {
      this.selectedVacancy = vacancy
      this.applicationType = type
      this.showApplicationModal = true
      this.showVacancyDetailsModal = false
      
      if (type === 'internship') {
        const periods = this.internshipPeriods
        if (periods.length > 0) {
          this.applicationForm.preferred_period = periods[0].id
        }
      }
    },

    showVacancyDetails(vacancy) {
      this.selectedVacancy = vacancy
      this.showVacancyDetailsModal = true
      this.showApplicationModal = false
    },

    closeApplicationModal() {
      this.showApplicationModal = false
      this.selectedVacancy = null
      this.applicationType = 'regular'
      this.resetForm()
    },

    closeVacancyDetails() {
      this.showVacancyDetailsModal = false
      this.selectedVacancy = null
    },

    resetForm() {
      this.applicationForm = {
        lastName: '',
        firstName: '',
        middleName: '',
        email: '',
        phone: '',
        city: '',
        education: '',
        faculty: '',
        course: '',
        preferred_period: '',
        experience: '',
        motivation: '',
        resume_url: ''
      }
    },

async submitApplication() {
  this.isSubmitting = true
  try {
    const applicationData = {
      vacancy: this.selectedVacancy.id,
      application_type: this.applicationType === 'internship' ? 'internship' : 'regular',
      first_name: this.applicationForm.firstName,
      last_name: this.applicationForm.lastName,
      middle_name: this.applicationForm.middleName || '',
      email: this.applicationForm.email,
      phone: this.applicationForm.phone,
      city: this.applicationForm.city,
      experience_description: this.applicationForm.experience || '',
      motivation: this.applicationForm.motivation,
      resume_url: this.applicationForm.resume_url || ''
    }

    // Добавляем данные для практики
    if (this.applicationType === 'internship') {
      applicationData.internship_period = this.applicationForm.preferred_period
      applicationData.education_institution = this.applicationForm.education
      applicationData.faculty = this.applicationForm.faculty
      applicationData.course = this.applicationForm.course ? parseInt(this.applicationForm.course) : null
    }

    console.log('📤 Отправляем данные:', applicationData)

    const backendUrl = 'http://localhost:8000/api/applications/'
    const response = await this.$axios.post(backendUrl, applicationData, {
      headers: {
        'Content-Type': 'application/json',
      }
    })
    
    console.log('✅ Заявка сохранена в БД:', response.data)
    
    this.isSubmitting = false
    this.closeApplicationModal()
    alert('✅ Заявка отправлена! Мы свяжемся с вами в ближайшее время.')
    
    // Обновляем данные вакансий
    await this.loadVacancies()
    
  } catch (error) {
    console.error('❌ Ошибка отправки заявки:', error)
    
    if (error.response) {
      console.error('Статус ошибки:', error.response.status)
      console.error('Данные ошибки:', error.response.data)
      
      if (error.response.status === 400) {
        const errorDetails = error.response.data
        let errorMessage = 'Ошибка заполнения формы:\n'
        
        for (const field in errorDetails) {
          errorMessage += `• ${field}: ${errorDetails[field].join(', ')}\n`
        }
        
        alert(`❌ ${errorMessage}`)
      } else {
        alert(`❌ Ошибка сервера: ${error.response.status}`)
      }
    } else if (error.request) {
      console.error('Не получен ответ от сервера')
      alert('❌ Не удалось соединиться с сервером. Проверьте, запущен ли бэкенд на localhost:8000')
    } else {
      console.error('Ошибка настройки:', error.message)
      alert('❌ Ошибка: ' + error.message)
    }
    
    this.isSubmitting = false
  }
},

    getMockVacancies() {
      return [
        {
          id: 1,
          title: 'Стажер-разработчик 1С',
          level: 'intern',
          type: 'onsite',
          city: 'Красноярск',
          salary_from: 30000,
          salary_to: 40000,
          description: 'Приглашаем студентов технических специальностей для прохождения стажировки в отделе разработки.',
          is_internship: true,
          application_count: 12,
          applications_today: 3,
          requirements: ['Знание основ программирования', 'Базовое понимание SQL', 'Готовность обучаться'],
          responsibilities: ['Разработка и доработка конфигураций 1С', 'Участие в проектах автоматизации'],
          benefits: ['Обучение за счет компании', 'Гибкий график', 'Наставник'],
          internship_periods: []
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

.gradient-text {
  background: linear-gradient(135deg, #DC2626 0%, #991b1b 50%, #B91C1C 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
</style>