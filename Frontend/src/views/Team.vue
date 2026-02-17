<template>
  <div class="min-h-screen bg-gray-50 pt-20">
    <div class="container mx-auto px-6 py-12">
      <h1 class="text-4xl md:text-5xl font-bold text-apogee-red mb-8 font-display">Таланты нашей компании</h1>
      <div class="grid gap-10 grid-cols-1 sm:grid-cols-2 lg:grid-cols-3">
        <TeamItem
          v-for="member in team"
          :key="member.id"
          :name="member.name"
          :position="member.position"
          :city="member.city"
          :education="member.education"
          :bio="member.bio"
          :photo="member.photo"
        />
      </div>
    </div>
  </div>
</template>

<script>
import TeamItem from '../components/TeamItem.vue'

export default {
  name: 'TeamPage',
  components: {
    TeamItem
  },
  data() {
    return {
      team: [
        {
          id: 1,
          name: 'Александр Петров',
          position: 'Генеральный директор',
          city: 'Москва',
          education: 'МГУ',
          bio: 'В 24 года достиг доложности генерального директора компании.',
          photo: 'https://randomuser.me/api/portraits/men/32.jpg'
        },
        {
          id: 2,
          name: 'Елена Смирнова',
          position: 'Технический директор',
          city: 'Санкт-Петербург',
          education: 'МФТИ',
          bio: 'За 5 лет поднялась с Junior-разработчика до технического директора.',
          photo: 'https://randomuser.me/api/portraits/women/44.jpg'
        },
        {
          id: 3,
          name: 'Дмитрий Иванов',
          position: 'Директор по развитию',
          city: 'Новосибирск',
          education: 'ВШЭ',
          bio: 'За 3 года вырос с Аналитика до Директора по развитию',
          photo: 'https://randomuser.me/api/portraits/men/65.jpg'
        },
        {
          id: 4,
          name: 'Ольга Кузнецова',
          position: 'Менеджер проектов',
          city: 'Екатеринбург',
          education: 'СПбГУ',
          bio: 'Эксперт в управлении проектами с 10-летним опытом.',
          photo: 'https://randomuser.me/api/portraits/women/68.jpg'
        }
      ]
    }
  }
}
</script>
