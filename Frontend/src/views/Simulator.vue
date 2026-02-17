<template>
  <div class="min-h-screen bg-gray-50 pt-20">
    <div class="container mx-auto px-6 py-12">

      <!-- Заголовок симулятора -->
      <div class="text-center mb-8">
        <h1 class="text-4xl md:text-5xl font-bold text-apogee-dark mb-4 font-display">
          Симулятор задач 1С
        </h1>
        <p class="text-xl text-gray-600 max-w-2xl mx-auto mb-6">
          Попробуйте себя в роли специалиста 1С. Решите реальные задачи, с которыми сталкиваются наши сотрудники
        </p>

        <!-- Профессия селектор -->
        <div class="inline-flex rounded-lg border border-gray-300 overflow-hidden">
          <button 
            v-for="profession in professions" 
            :key="profession.id" 
            @click="selectProfession(profession.id)"
            :class="[
              'px-6 py-2 font-semibold transition-colors focus:outline-none',
              selectedProfession === profession.id 
                ? 'bg-apogee-red text-white shadow-md' 
                : 'bg-white text-gray-700 hover:bg-apogee-red hover:text-white'
            ]"
          >
            {{ profession.name }}
          </button>
        </div>
      </div>

      <!-- Email для сохранения прогресса -->
      <div v-if="!userEmail" class="max-w-md mx-auto mb-8 p-6 bg-white rounded-2xl shadow-lg">
        <h3 class="text-lg font-semibold text-gray-800 mb-3">Сохраните свой прогресс</h3>
        <p class="text-gray-600 mb-4 text-sm">Введите email чтобы сохранять результаты выполнения задач</p>
        <div class="flex gap-3">
          <input 
            v-model="emailInput"
            type="email" 
            placeholder="your@email.com"
            class="flex-1 p-3 border-2 border-gray-300 rounded-xl focus:border-apogee-red focus:ring-2 focus:ring-red-100"
          >
          <button 
            @click="setUserEmail"
            class="bg-apogee-red text-white px-6 py-3 rounded-xl font-semibold hover:bg-apogee-darkRed transition-colors"
          >
            Сохранить
          </button>
        </div>
      </div>

      <!-- Основной контейнер симулятора -->
      <div class="grid lg:grid-cols-3 gap-8 mb-12">

        <!-- Левая панель - выбор задачи -->
        <div class="lg:col-span-1">
          <div class="bg-white rounded-2xl shadow-lg p-6 sticky top-24">
            <h2 class="text-2xl font-bold text-apogee-dark mb-6">Выберите задачу</h2>
            
            <!-- Индикатор загрузки -->
            <div v-if="isLoading" class="text-center py-8">
              <div class="animate-spin rounded-full h-8 w-8 border-b-2 border-apogee-red mx-auto"></div>
              <p class="text-gray-600 mt-2">Загружаем задачи...</p>
            </div>

            <div v-else class="space-y-4">
              <button 
                v-for="task in currentTasks" 
                :key="task.id"
                @click="selectTask(task)"
                :class="[
                  'w-full text-left p-4 rounded-xl border-2 transition-all duration-300',
                  selectedTask?.id === task.id 
                    ? 'border-apogee-red bg-red-50 shadow-md' 
                    : taskProgress[task.id]?.completed
                    ? 'border-green-500 bg-green-50'
                    : 'border-gray-200 hover:border-apogee-red hover:bg-red-50'
                ]"
              >
                <div class="flex items-center space-x-3">
                  <div 
                    :class="[
                      'w-10 h-10 rounded-lg flex items-center justify-center text-white font-bold',
                      taskProgress[task.id]?.completed 
                        ? 'bg-green-500' 
                        : 'bg-apogee-red'
                    ]"
                  >
                    {{ task.level }}
                  </div>
                  <div class="flex-1">
                    <h3 class="font-semibold text-gray-800">{{ task.title }}</h3>
                    <p class="text-sm text-gray-600">{{ getDifficultyDisplay(task.difficulty) }}</p>
                    <p class="text-xs text-gray-500">{{ task.estimated_time }} мин</p>
                  </div>
                  <div v-if="taskProgress[task.id]?.completed" class="text-green-500">
                    ✓
                  </div>
                </div>
              </button>
            </div>

            <!-- Прогресс -->
            <div class="mt-8 p-4 bg-gray-50 rounded-xl">
              <h3 class="font-semibold text-gray-800 mb-3">Ваш прогресс</h3>
              <div class="flex items-center justify-between text-sm mb-2">
                <span>Решено задач:</span>
                <span class="font-bold text-apogee-red">{{ completedTasksCount }}/{{ currentTasks.length }}</span>
              </div>
              <div class="w-full bg-gray-200 rounded-full h-2">
                <div 
                  class="bg-apogee-red h-2 rounded-full transition-all duration-500"
                  :style="`width: ${progressPercentage}%`"
                ></div>
              </div>
              <div v-if="userEmail" class="mt-2 text-xs text-gray-500">
                Прогресс сохранен для: {{ userEmail }}
              </div>
            </div>
          </div>
        </div>

        <!-- Правая панель - область решения -->
        <div class="lg:col-span-2">
          <div v-if="selectedTask" class="bg-white rounded-2xl shadow-lg p-8">

            <!-- Заголовок задачи -->
            <div class="flex items-center justify-between mb-6">
              <div>
                <h2 class="text-2xl font-bold text-apogee-dark">{{ selectedTask.title }}</h2>
                <p class="text-gray-600">{{ selectedTask.description }}</p>
              </div>
              <div class="flex items-center space-x-2">
                <span class="px-3 py-1 bg-red-100 text-apogee-red rounded-full text-sm font-semibold">
                  {{ getDifficultyDisplay(selectedTask.difficulty) }}
                </span>
                <span class="px-3 py-1 bg-blue-100 text-blue-600 rounded-full text-sm font-semibold">
                  {{ selectedTask.estimated_time }} мин
                </span>
                <span v-if="taskProgress[selectedTask.id]?.completed" 
                      class="px-3 py-1 bg-green-100 text-green-600 rounded-full text-sm font-semibold">
                  ✓ Выполнено
                </span>
              </div>
            </div>

            <!-- Условие задачи -->
            <div class="mb-6">
              <h3 class="text-lg font-semibold text-gray-800 mb-4">Условие задачи:</h3>
              <div class="bg-gray-50 rounded-xl p-6 mb-6">
                <p class="text-gray-700 whitespace-pre-line">{{ selectedTask.problem }}</p>
              </div>

              <!-- Поле решения -->
              <div class="mb-6">
                <label class="block text-lg font-semibold text-gray-800 mb-3">Ваше решение:</label>
                <textarea 
                  v-model="userSolution"
                  placeholder="Опишите ваше решение здесь..."
                  class="w-full h-40 p-4 border-2 border-gray-300 rounded-xl focus:border-apogee-red focus:ring-2 focus:ring-red-100 resize-none transition-all duration-300"
                ></textarea>
              </div>

              <!-- Кнопки действия -->
              <div class="flex flex-wrap gap-4">
                <button 
                  @click="checkSolution"
                  :disabled="!userSolution.trim() || isChecking"
                  :class="[
                    'px-6 py-3 rounded-lg font-semibold transition-all duration-300 flex items-center space-x-2',
                    userSolution.trim() && !isChecking
                      ? 'bg-apogee-red text-white hover:bg-apogee-darkRed shadow-lg hover:shadow-xl' 
                      : 'bg-gray-300 text-gray-500 cursor-not-allowed'
                  ]"
                >
                  <span v-if="isChecking" class="animate-spin">⏳</span>
                  <span v-else>✅</span>
                  <span>{{ isChecking ? 'Проверяем...' : 'Проверить решение' }}</span>
                </button>
                
                <button 
                  @click="showHint"
                  class="px-6 py-3 border-2 border-apogee-red text-apogee-red rounded-lg font-semibold hover:bg-apogee-red hover:text-white transition-all duration-300 flex items-center space-x-2"
                >
                  <span>💡</span>
                  <span>Подсказка</span>
                </button>

                <button 
                  @click="resetTask"
                  class="px-6 py-3 border-2 border-gray-400 text-gray-600 rounded-lg font-semibold hover:bg-gray-400 hover:text-white transition-all duration-300"
                >
                  Сбросить
                </button>

                <button
                  @click="showSolution"
                  class="px-6 py-3 border-2 border-blue-500 text-blue-600 rounded-lg font-semibold hover:bg-blue-600 hover:text-white transition-all duration-300 flex items-center space-x-2"
                >
                  <span>📖</span>
                  <span>Показать решение</span>
                </button>
              </div>
            </div>

            <!-- Показать решение -->
            <div v-if="showSolutionArea" class="mt-6 p-6 bg-blue-50 border border-blue-300 rounded-xl">
              <div class="flex items-center justify-between mb-3">
                <h3 class="text-lg font-semibold text-blue-800">Правильное решение:</h3>
                <button
                  @click="hideSolution"
                  class="text-blue-600 hover:text-blue-800 font-semibold"
                >
                  Скрыть
                </button>
              </div>
              <p class="text-blue-700 whitespace-pre-line">{{ selectedTask.correct_answer }}</p>
            </div>

            <!-- Результат проверки -->
            <div v-if="showResult" class="mt-6 p-6 rounded-xl" :class="resultClass">
              <div class="flex items-center space-x-3">
                <span class="text-2xl">{{ resultIcon }}</span>
                <div>
                  <h3 class="font-semibold text-lg">{{ resultTitle }}</h3>
                  <p class="mt-1">{{ resultMessage }}</p>
                  <button 
                    v-if="resultType === 'success' && userEmail"
                    @click="saveProgress"
                    class="mt-3 px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 transition-colors text-sm"
                  >
                    💾 Сохранить прогресс
                  </button>
                </div>
              </div>
            </div>

            <!-- Подсказка -->
            <div v-if="showHintModal" class="mt-6 p-6 bg-yellow-50 border border-yellow-200 rounded-xl">
              <div class="flex items-center justify-between mb-3">
                <h3 class="font-semibold text-yellow-800 flex items-center space-x-2">
                  <span>💡</span>
                  <span>Подсказка</span>
                </h3>
                <button @click="showHintModal = false" class="text-yellow-600 hover:text-yellow-800">
                  ✕
                </button>
              </div>
              <p class="text-yellow-700 whitespace-pre-line">{{ selectedTask.hint }}</p>
            </div>

          </div>

          <!-- Состояние при выборе задачи -->
          <div v-else class="bg-white rounded-2xl shadow-lg p-12 text-center">
            <div class="w-24 h-24 mx-auto mb-6 bg-gray-100 rounded-full flex items-center justify-center">
              <span class="text-3xl">🎯</span>
            </div>
            <h3 class="text-2xl font-bold text-gray-600 mb-4">Выберите задачу для начала</h3>
            <p class="text-gray-500 max-w-md mx-auto">
              Выберите задачу из списка слева, чтобы начать решать и проверить свои навыки работы с 1С
            </p>
          </div>
        </div>
      </div>

      <!-- Информация о симуляторе -->
      <div class="bg-white rounded-2xl shadow-lg p-8">
        <h2 class="text-2xl font-bold text-apogee-dark mb-6">Как это работает?</h2>
        <div class="grid md:grid-cols-3 gap-6">
          <div v-for="step in howItWorks" :key="step.title" class="text-center">
            <div class="w-16 h-16 mx-auto mb-4 bg-apogee-red rounded-full flex items-center justify-center text-white text-xl font-bold">
              {{ step.number }}
            </div>
            <h3 class="font-semibold text-gray-800 mb-2">{{ step.title }}</h3>
            <p class="text-gray-600 text-sm">{{ step.description }}</p>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
import { simulatorAPI } from '@/services/api'

export default {
  name: 'SimulatorPage',
  data() {
    return {
      selectedProfession: 'programmer',
      professions: [
        { id: 'programmer', name: 'Программист 1С' },
        { id: 'consultant', name: 'Консультант 1С' },
        { id: 'service', name: 'Сервис-инженер 1С' }
      ],
      selectedTask: null,
      userSolution: '',
      showResult: false,
      showHintModal: false,
      showSolutionArea: false,
      resultType: '',
      isLoading: false,
      isChecking: false,
      userEmail: localStorage.getItem('simulator_user_email') || '',
      emailInput: '',
      tasks: [],
      userProgress: [],
      taskProgress: {},
      
      howItWorks: [
        {
          number: 1,
          title: 'Выберите профессию',
          description: 'Сначала выберите профессию, которая вас интересует'
        },
        {
          number: 2,
          title: 'Выберите задачу',
          description: 'Затем выберите одну из задач по уровню сложности'
        },
        {
          number: 3,
          title: 'Решите задачу',
          description: 'Опишите своё решение и проверьте его'
        }
      ]
    }
  },
  computed: {
  currentTasks() {
    return this.tasks.filter(task => task.profession_type === this.selectedProfession)
  },
  completedTasksCount() {
    // Считаем только выполненные задачи для текущей профессии
    return this.currentTasks.filter(task => 
      this.taskProgress[task.id]?.completed
    ).length
  },
  progressPercentage() {
    if (this.currentTasks.length === 0) return 0
    return (this.completedTasksCount / this.currentTasks.length) * 100
  },
    resultClass() {
      return this.resultType === 'success' 
        ? 'bg-green-50 border border-green-200' 
        : 'bg-red-50 border border-red-200'
    },
    resultIcon() {
      return this.resultType === 'success' ? '🎉' : '❌'
    },
    resultTitle() {
      return this.resultType === 'success' ? 'Отлично!' : 'Есть ошибки'
    },
    resultMessage() {
      return this.resultType === 'success' 
        ? 'Ваше решение верное! Вы хорошо справились с задачей.'
        : 'Попробуйте еще раз. Используйте подсказку если нужно.'
    }
  },
  async mounted() {
    await this.loadTasks()
    if (this.userEmail) {
      await this.loadUserProgress()
    }
  },
  methods: {
    async loadTasks() {
      this.isLoading = true
      try {
        const response = await simulatorAPI.getTasks()
        this.tasks = response.data.results || response.data
      } catch (error) {
        console.error('Ошибка загрузки задач:', error)
        // Fallback на локальные данные если API недоступно
        this.tasks = this.getFallbackTasks()
      } finally {
        this.isLoading = false
      }
    },

    async loadUserProgress() {
      try {
        const response = await simulatorAPI.getUserProgress(this.userEmail)
        this.userProgress = response.data.results || response.data
        // Создаем объект для быстрого доступа к прогрессу по task_id
        this.taskProgress = {}
        this.userProgress.forEach(progress => {
          this.taskProgress[progress.task_id] = progress
        })
      } catch (error) {
        console.error('Ошибка загрузки прогресса:', error)
      }
    },

    setUserEmail() {
      if (this.emailInput && this.validateEmail(this.emailInput)) {
        this.userEmail = this.emailInput
        localStorage.setItem('simulator_user_email', this.userEmail)
        this.loadUserProgress()
      } else {
        alert('Пожалуйста, введите корректный email')
      }
    },

    validateEmail(email) {
      const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
      return re.test(email)
    },

    selectProfession(professionId) {
      this.selectedProfession = professionId
      this.selectedTask = null
      this.resetTaskState()
    },

    selectTask(task) {
      this.selectedTask = task
      this.resetTaskState()
      // Загружаем сохраненное решение если есть
      if (this.taskProgress[task.id]?.user_solution) {
        this.userSolution = this.taskProgress[task.id].user_solution
      }
    },

    async checkSolution() {
      if (!this.userSolution.trim()) return
      
      this.isChecking = true
      this.showResult = false
      
      try {
        // Имитация проверки решения (в реальном приложении здесь был бы AI или сложная логика)
        await new Promise(resolve => setTimeout(resolve, 1000))
        
        // Простая проверка - решение считается верным если оно не пустое
        // В реальном приложении здесь была бы сложная логика проверки
        const isSuccess = this.userSolution.trim().length > 10
        
        this.resultType = isSuccess ? 'success' : 'error'
        this.showResult = true
        
        if (isSuccess && this.userEmail) {
          await this.saveProgress(true)
        }
      } catch (error) {
        console.error('Ошибка проверки решения:', error)
        this.resultType = 'error'
        this.showResult = true
      } finally {
        this.isChecking = false
      }
    },

    async saveProgress(isCorrect = null) {
      if (!this.userEmail || !this.selectedTask) return
      
      try {
        const progressData = {
          user_email: this.userEmail,
          task_id: this.selectedTask.id,
          user_solution: this.userSolution,
          completed: true,
          is_correct: isCorrect !== null ? isCorrect : this.resultType === 'success',
          completed_at: new Date().toISOString()
        }

        // Проверяем есть ли уже прогресс для этой задачи
        const existingProgress = this.taskProgress[this.selectedTask.id]
        
        if (existingProgress) {
          // Обновляем существующий прогресс
          await simulatorAPI.updateProgress(existingProgress.id, progressData)
        } else {
          // Создаем новый прогресс
          const response = await simulatorAPI.saveProgress(progressData)
          this.taskProgress[this.selectedTask.id] = { ...progressData, id: response.data.id }
        }
        
        // Обновляем локальное состояние
        this.taskProgress[this.selectedTask.id] = {
          ...this.taskProgress[this.selectedTask.id],
          ...progressData
        }
        
        console.log('Прогресс сохранен')
      } catch (error) {
        console.error('Ошибка сохранения прогресса:', error)
      }
    },

    showHint() {
      this.showHintModal = true
    },

    showSolution() {
      this.showSolutionArea = true
    },

    hideSolution() {
      this.showSolutionArea = false
    },

    resetTask() {
      this.userSolution = ''
      this.showResult = false
      this.showHintModal = false
      this.showSolutionArea = false
    },

    resetTaskState() {
      this.userSolution = ''
      this.showResult = false
      this.showHintModal = false
      this.showSolutionArea = false
      this.isChecking = false
    },

    getDifficultyDisplay(difficulty) {
      const difficulties = {
        'beginner': 'Начинающий',
        'intermediate': 'Средний', 
        'advanced': 'Продвинутый'
      }
      return difficulties[difficulty] || difficulty
    },

    getFallbackTasks() {
      // Fallback задачи если API недоступно
      return [
        {
          id: 1,
          profession_type: 'programmer',
          level: 1,
          title: 'Исправление ошибок в коде',
          difficulty: 'beginner',
          estimated_time: 15,
          description: 'Исправьте синтаксические ошибки в представленном коде 1С',
          problem: `В представленном коде 1С есть несколько синтаксических ошибок. Найдите и исправьте их:\n\nПроцедура Пример()\n    Перем А, Б, В;\n    А = 10\n    Б = 20\n    В = А + Б\n    Сообщить("Результат: " + В);\nКонецПроцедуры`,
          hint: 'Проверьте правильность объявления переменных и завершения операторов.',
          correct_answer: 'Процедура Пример()\n    Перем А, Б, В;\n    А = 10;\n    Б = 20;\n    В = А + Б;\n    Сообщить("Результат: " + В);\nКонецПроцедуры;',
          is_active: true
        },
        {
          id: 2,
          profession_type: 'programmer', 
          level: 2,
          title: 'Оптимизация запроса',
          difficulty: 'intermediate',
          estimated_time: 25,
          description: 'Оптимизируйте следующий запрос для повышения производительности',
          problem: `Дан неоптимальный запрос к базе данных. Перепишите его для улучшения производительности:\n\nВЫБРАТЬ\n    Товары.Наименование,\n    Товары.Цена\nИЗ\n    Справочник.Товары КАК Товары\nГДЕ\n    Товары.Наименование ПОДОБНО "%компьютер%"`,
          hint: 'Используйте индексы и избегайте оператора ПОДОБНО с начальным символом %.',
          correct_answer: 'ВЫБРАТЬ\n    Товары.Наименование,\n    Товары.Цена\nИЗ\n    Справочник.Товары КАК Товары\nГДЕ\n    Товары.Наименование ПОДОБНО "компьютер%"',
          is_active: true
        }
      ]
    }
  }
}
</script>