<template>
  <div class="min-h-screen bg-white pt-20 px-6 container mx-auto max-w-6xl">
    <h1 class="text-4xl font-bold text-apogee-dark mb-12 py-8">Карьерные пути в 1С</h1>

    <!-- Toggle buttons for career paths -->
    <div class="inline-flex rounded-lg border border-gray-300 overflow-hidden mb-12">
      <button
        @click="selectedPath = 'programmer'"
        :class="[
          'px-6 py-3 font-semibold transition-colors focus:outline-none',
          selectedPath === 'programmer' 
            ? 'bg-apogee-red text-white shadow-md' 
            : 'bg-white text-gray-700 hover:bg-apogee-red hover:text-white'
        ]"
      >Программист 1С</button>
      <button
        @click="selectedPath = 'consultant'"
        :class="[
          'px-6 py-3 font-semibold transition-colors focus:outline-none',
          selectedPath === 'consultant' 
            ? 'bg-apogee-red text-white shadow-md' 
            : 'bg-white text-gray-700 hover:bg-apogee-red hover:text-white'
        ]"
      >Консультант 1С</button>
    </div>

    <section class="mb-16" v-if="selectedPath === 'programmer'">
      <h2 class="text-3xl font-semibold mb-6 border-b border-apogee-red inline-block pb-2">Карьерный путь программиста</h2>
      <div class="flex flex-col lg:flex-row gap-12">
        <!-- Steps -->
        <div class="flex-1">
          <div v-for="(step, index) in programmerPath" :key="step.title" class="mb-8 last:mb-0">
            <div class="flex items-center space-x-6">
              <div class="w-14 min-w-[3.5rem] h-14 flex items-center justify-center rounded-full bg-apogee-red text-white text-xl font-semibold text-center">
                {{ index + 1 }}
              </div>
              <div>
                <h3 class="text-xl font-semibold text-apogee-dark">{{ step.title }}</h3>
                <p class="text-gray-600 mt-1">{{ step.description }}</p>
              </div>
            </div>
          </div>
        </div>
        <!-- Salary -->
        <div class="flex-1 bg-apogee-red bg-opacity-10 p-6 rounded-lg">
          <h3 class="text-2xl font-semibold text-apogee-red mb-4">Рост зарплаты</h3>
          <ul class="space-y-4">
            <li v-for="(step, index) in programmerPath" :key="'salary' + index" class="flex justify-between text-apogee-dark font-semibold">
              <span>{{ step.title }}</span>
              <span>{{ step.salary }}</span>
            </li>
          </ul>
          
          <!-- Кнопки действий для программиста -->
          <div class="mt-8 space-y-4">
            <!-- Кнопка ЗАПИСЬ НА ПРАКТИКУ -->
            <button 
              @click="openApplicationModal('programmer', 'internship')"
              class="w-full bg-gradient-to-r from-green-500 to-green-600 text-white py-4 rounded-xl font-semibold hover:from-green-600 hover:to-green-700 transition-all duration-300 shadow-lg hover:shadow-xl flex items-center justify-center space-x-2"
            >
              <span>🎓</span>
              <span>Запись на практику</span>
            </button>
            
            <!-- Кнопка ОТКЛИКНУТЬСЯ -->
            <button 
              @click="openApplicationModal('programmer', 'regular')"
              class="w-full bg-apogee-red text-white py-4 rounded-xl font-semibold hover:bg-apogee-darkRed transition-all duration-300 shadow-lg hover:shadow-xl flex items-center justify-center space-x-2"
            >
              <span>💼</span>
              <span>Откликнуться</span>
            </button>
          </div>
        </div>
      </div>
    </section>

    <section class="mb-16" v-else-if="selectedPath === 'consultant'">
      <h2 class="text-3xl font-semibold mb-6 border-b border-apogee-red inline-block pb-2">Карьерный путь консультанта</h2>
      <div class="flex flex-col lg:flex-row gap-12">
        <!-- Steps -->
        <div class="flex-1">
          <div v-for="(step, index) in consultantPath" :key="step.title" class="mb-8 last:mb-0">
            <div class="flex items-center space-x-6">
              <div class="w-14 min-w-[3.5rem] h-14 flex items-center justify-center rounded-full bg-apogee-red text-white text-xl font-semibold text-center">
                {{ index + 1 }}
              </div>
              <div>
                <h3 class="text-xl font-semibold text-apogee-dark">{{ step.title }}</h3>
                <p class="text-gray-600 mt-1">{{ step.description }}</p>
              </div>
            </div>
          </div>
        </div>
        <!-- Salary -->
        <div class="flex-1 bg-apogee-red bg-opacity-10 p-6 rounded-lg">
          <h3 class="text-2xl font-semibold text-apogee-red mb-4">Рост зарплаты</h3>
          <ul class="space-y-4">
            <li v-for="(step, index) in consultantPath" :key="'salary-consultant' + index" class="flex justify-between text-apogee-dark font-semibold">
              <span>{{ step.title }}</span>
              <span>{{ step.salary }}</span>
            </li>
          </ul>
          
          <!-- Кнопки действий для консультанта -->
          <div class="mt-8 space-y-4">
            <!-- Кнопка ЗАПИСЬ НА ПРАКТИКУ -->
            <button 
              @click="openApplicationModal('consultant', 'internship')"
              class="w-full bg-gradient-to-r from-green-500 to-green-600 text-white py-4 rounded-xl font-semibold hover:from-green-600 hover:to-green-700 transition-all duration-300 shadow-lg hover:shadow-xl flex items-center justify-center space-x-2"
            >
              <span>🎓</span>
              <span>Запись на практику</span>
            </button>
            
            <!-- Кнопка ОТКЛИКНУТЬСЯ -->
            <button 
              @click="openApplicationModal('consultant', 'regular')"
              class="w-full bg-apogee-red text-white py-4 rounded-xl font-semibold hover:bg-apogee-darkRed transition-all duration-300 shadow-lg hover:shadow-xl flex items-center justify-center space-x-2"
            >
              <span>💼</span>
              <span>Откликнуться</span>
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- Модальное окно заявки на ПРАКТИКУ -->
    <div v-if="showApplicationModal && applicationType === 'internship'" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
      <div class="bg-white rounded-2xl max-w-2xl w-full max-h-[90vh] overflow-y-auto">
        <div class="sticky top-0 bg-white border-b border-gray-200 p-6 rounded-t-2xl flex justify-between items-center">
          <div>
            <h2 class="text-2xl font-bold text-apogee-dark">Заявка на практику</h2>
            <p class="text-gray-600 mt-1">{{ getSelectedPathTitle() }}</p>
          </div>
          <button @click="closeApplicationModal" class="text-gray-400 hover:text-gray-600 text-2xl">
            ×
          </button>
        </div>

        <div class="p-6">
          <!-- Информация о направлении -->
          <div class="mb-6 p-4 bg-blue-50 border border-blue-200 rounded-xl">
            <h3 class="font-semibold text-blue-800 mb-2">Направление:</h3>
            <p class="text-blue-700">{{ getSelectedPathTitle() }}</p>
            <p class="text-sm text-blue-600 mt-1">
              {{ getSelectedPathDescription() }}
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
                  <option value="summer_2024">Лето 2024 (Июнь - Август)</option>
                  <option value="autumn_2024">Осень 2024 (Сентябрь - Декабрь)</option>
                  <option value="winter_2025">Зима 2025 (Январь - Март)</option>
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
            <p class="text-gray-600 mt-1">{{ getSelectedPathTitle() }}</p>
          </div>
          <button @click="closeApplicationModal" class="text-gray-400 hover:text-gray-600 text-2xl">
            ×
          </button>
        </div>

        <div class="p-6">
          <!-- Информация о направлении -->
          <div class="mb-6 p-4 bg-blue-50 border border-blue-200 rounded-xl">
            <h3 class="font-semibold text-blue-800 mb-2">Направление:</h3>
            <p class="text-blue-700">{{ getSelectedPathTitle() }}</p>
            <p class="text-sm text-blue-600 mt-1">
              {{ getSelectedPathDescription() }}
            </p>
          </div>

          <form @submit.prevent="submitApplication">
            <!-- Персональные данные -->
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
  </div>
</template>

<script>
export default {
  name: 'CareerPaths',
  data() {
    return {
      selectedPath: 'programmer',
      showApplicationModal: false,
      applicationType: 'regular',
      isSubmitting: false,
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
      programmerPath: [
        {
          title: 'Стажер',
          description: 'Начинающий специалист, обучается основам и участвует в простых задачах.',
          salary: '30 000 ₽'
        },
        {
          title: 'Младший программист',
          description: 'Осваивает базовые разработки и поддержку, действует под руководством старших коллег.',
          salary: '50 000 ₽'
        },
        {
          title: 'Программист',
          description: 'Выполняет задачи самостоятельно, участвует в проектировании решений и оптимизации процессов.',
          salary: '80 000 ₽'
        },
        {
          title: 'Старший программист',
          description: 'Руководит небольшими проектами, разрабатывает сложные решения и обучает младших.',
          salary: '120 000 ₽'
        },
        {
          title: 'Тимлид',
          description: 'Управляет командой программистов, контролирует качество и сроки разработки.',
          salary: '160 000 ₽'
        },
        {
          title: 'Руководитель проектов',
          description: 'Отвечает за координацию проектов, коммуникации с заказчиками и успешное выполнение задач.',
          salary: '200 000 ₽'
        }
      ],
      consultantPath: [
        {
          title: 'Начинающий консультант',
          description: 'Изучает основы работы с клиентами и функционал 1С.',
          salary: '35 000 ₽'
        },
        {
          title: 'Консультант',
          description: 'Проводит анализ требований, внедряет стандартные решения и поддерживает клиентов.',
          salary: '60 000 ₽'
        },
        {
          title: 'Ведущий консультант',
          description: 'Разрабатывает сложные бизнес-процессы, координирует команду консультантов.',
          salary: '90 000 ₽'
        },
        {
          title: 'Аналитик ERP',
          description: 'Управляет архитектурой ERP-систем, формирует требования и рекомендации для оптимизации.',
          salary: '130 000 ₽'
        }
      ]
    }
  },
  methods: {
    openApplicationModal(path, type) {
      this.selectedPath = path
      this.applicationType = type
      this.showApplicationModal = true
    },

    closeApplicationModal() {
      this.showApplicationModal = false
      this.resetForm()
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

    getSelectedPathTitle() {
      return this.selectedPath === 'programmer' ? 'Программист 1С' : 'Консультант 1С'
    },

    getSelectedPathDescription() {
      return this.selectedPath === 'programmer' 
        ? 'Разработка и сопровождение систем на платформе 1С' 
        : 'Консультации и внедрение бизнес-решений на платформе 1С'
    },

    async submitApplication() {
      this.isSubmitting = true
      try {
        // Здесь будет логика отправки заявки
        console.log('Отправка заявки:', {
          path: this.selectedPath,
          type: this.applicationType,
          form: this.applicationForm
        })
        
        // Имитация отправки
        await new Promise(resolve => setTimeout(resolve, 2000))
        
        this.isSubmitting = false
        this.closeApplicationModal()
        alert('✅ Заявка отправлена! Мы свяжемся с вами в ближайшее время.')
        
      } catch (error) {
        console.error('Ошибка отправки заявки:', error)
        this.isSubmitting = false
        alert('❌ Произошла ошибка при отправке заявки. Попробуйте еще раз.')
      }
    }
  }
}
</script>

<style scoped>
/* Add some spacing for mobile and desktop */
@media (min-width: 1024px) {
  section > div {
    display: flex;
  }
}
</style>