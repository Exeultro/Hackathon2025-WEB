import axios from 'axios'

const API_BASE_URL = 'http://127.0.0.1:8000/api'

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  }
})

// Интерцепторы для обработки ошибок
apiClient.interceptors.response.use(
  (response) => response,
  (error) => {
    console.error('API Error:', error)
    return Promise.reject(error)
  }
)

export const vacanciesAPI = {
  // Получить все вакансии
  getVacancies(params = {}) {
    return apiClient.get('/vacancies/', { params })
  },
  
  // Получить вакансию по ID
  getVacancy(id) {
    return apiClient.get(`/vacancies/${id}/`)
  },
  
  // Получить только стажировки
  getInternships() {
    return apiClient.get('/vacancies/internships/')
  },
  
  // Популярные вакансии
  getFeatured() {
    return apiClient.get('/vacancies/featured/')
  },
  
  // Получить фильтры
  getFilters() {
    return apiClient.get('/vacancies/filters/')
  },
  
  // Поиск вакансий
  searchVacancies(query) {
    return apiClient.get('/vacancies/', { params: { search: query } })
  }
}

export const internshipAPI = {
  // Получить периоды практики
  getPeriods() {
    return apiClient.get('/internship-periods/')
  }
}

// ✅ ДОБАВЛЯЕМ API ДЛЯ НОВОСТЕЙ
export const newsAPI = {
  // Получить все новости
  getNews(params = {}) {
    return apiClient.get('/news/', { params })
  },
  
  // Получить новость по ID
  getNewsArticle(id) {
    return apiClient.get(`/news/${id}/`)
  },
  
  // Избранные новости (для главной страницы)
  getFeaturedNews() {
    return apiClient.get('/news/featured/')
  },
  
  // Поиск новостей
  searchNews(query) {
    return apiClient.get('/news/', { params: { search: query } })
  }
}

// ✅ ДОБАВЛЯЕМ API ДЛЯ КОМАНДЫ
export const teamAPI = {
  // Получить всех членов команды
  getTeamMembers() {
    return apiClient.get('/team-members/')
  },
  
  // Получить активных членов команды
  getActiveTeam() {
    return apiClient.get('/team-members/active/')
  }
}

// ✅ ДОБАВЛЯЕМ API ДЛЯ СИМУЛЯТОРА
export const simulatorAPI = {
  // Получить все задачи
  getTasks(params = {}) {
    return apiClient.get('/simulator-tasks/', { params })
  },
  
  // Получить задачи по профессии и уровню
  getTasksByProfession(profession, level = null) {
    const params = { profession_type: profession }
    if (level) params.level = level
    return apiClient.get('/simulator-tasks/', { params })
  },
  
  // Получить прогресс пользователя
  getUserProgress(userEmail) {
    return apiClient.get(`/simulator-progress/?user_email=${userEmail}`)
  },
  
  // Сохранить прогресс
  saveProgress(progressData) {
    return apiClient.post('/simulator-progress/', progressData)
  },
  
  // Обновить прогресс
  updateProgress(id, progressData) {
    return apiClient.patch(`/simulator-progress/${id}/`, progressData)
  }
}

// ✅ ДОБАВЛЯЕМ API ДЛЯ ЗАЯВОК
export const applicationsAPI = {
  // Создать заявку
  createApplication(applicationData) {
    return apiClient.post('/applications/', applicationData)
  },
  
  // Получить заявки (для админки)
  getApplications(params = {}) {
    return apiClient.get('/applications/', { params })
  },
  
  // Получить заявку по ID
  getApplication(id) {
    return apiClient.get(`/applications/${id}/`)
  },
  
  // Обновить статус заявки
  updateApplicationStatus(id, statusData) {
    return apiClient.patch(`/applications/${id}/`, statusData)
  }
}


export default apiClient