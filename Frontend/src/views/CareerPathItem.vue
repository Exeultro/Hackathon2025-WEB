<template>
  <div class="min-h-screen bg-white pt-20 px-6 container mx-auto max-w-6xl">
    <h1 class="text-4xl font-bold text-apogee-dark mb-12 py-8">Карьерные пути: {{ careerPathTitle }}</h1>

    <section>
      <h2 class="text-3xl font-semibold mb-6 border-b border-apogee-red inline-block pb-2">{{ careerPathTitle }}</h2>

      <div class="flex flex-col lg:flex-row gap-12">
        <!-- Steps -->
        <div class="flex-1">
          <div v-for="(step, index) in careerPathData" :key="step.title" class="mb-8 last:mb-0">
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
            <li v-for="(step, index) in careerPathData" :key="'salary' + index" class="flex justify-between text-apogee-dark font-semibold">
              <span>{{ step.title }}</span>
              <span>{{ step.salary }}</span>
            </li>
          </ul>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'CareerPathItem',
  data() {
    return {
      careerPaths: {
        programmer: [
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
        consultant: [
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
    }
  },
  computed: {
    careerPathTitle() {
      const id = this.$route.params.id || 'programmer'
      if (id === 'programmer') return 'Карьерный путь программиста'
      if (id === 'consultant') return 'Карьерный путь консультанта'
      return 'Карьерный путь'
    },
    careerPathData() {
      const id = this.$route.params.id || 'programmer'
      return this.careerPaths[id] || []
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
