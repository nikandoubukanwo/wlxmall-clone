import axios from 'axios'

const api = axios.create({
  baseURL: '/api',
  timeout: 10000,
  headers: { 'Content-Type': 'application/json' },
})

api.interceptors.request.use(config => {
  const token = localStorage.getItem('token')
  if (token) config.headers.Authorization = `Bearer ${token}`
  return config
})

api.interceptors.response.use(
  res => res.data,
  err => Promise.reject(err.response?.data || err)
)

export default api

export const productAPI = {
  hotList: (params) => api.get('/products/hot', { params }),
  search: (params) => api.get('/products/search', { params }),
  detail: (id) => api.get(`/products/${id}`),
}

export const brandAPI = {
  list: (params) => api.get('/brands', { params }),
}

export const newsAPI = {
  list: (params) => api.get('/news', { params }),
}

export const userAPI = {
  login: (data) => api.post('/users/login', data),
  register: (data) => api.post('/users/register', data),
}

export const inquiryAPI = {
  submit: (data) => api.post('/inquiry', data),
}
