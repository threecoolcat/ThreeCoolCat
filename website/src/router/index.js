import Vue from 'vue'
import Router from 'vue-router'
import Layout from '@/views/layout'
Vue.use(Router)

export const constantRoutes = [
  {
    path: '/',
    component: Layout,
    children: [
      {
        path: '',
        title: '首页',
        icon: '',
        name: 'home',
        component: () => import('@/views/home'),
        
      },
      {
        path: 'hotNewList',
        title: '新闻列表',
        icon: '',
        name: 'hotNewList',
        component: () => import('@/views/home/hotNewList'),
        hidden: false,
        
      },
      {
        path: 'hotNewDetail',
        title: '新闻详情',
        icon: '',
        name: 'hotNewDetail',
        component: () => import('@/views/home/hotNewDetail'),
        hidden: true,
        meta: {
        }
      },
      {
        path: 'schoolList',
        title: '课程列表',
        icon: '',
        name: 'schoolList',
        component: () => import('@/views/school/schoolList'),
        hidden: false,
        
      },
      {
        path: 'courseList',
        title: '课程列表',
        icon: '',
        name: 'courseList',
        component: () => import('@/views/school/courseList'),
        hidden: false,
        
      },
      {
        path: 'courseDetail',
        title: '课程详情',
        icon: '',
        name: 'courseDetail',
        component: () => import('@/views/school/courseDetail'),
        hidden: true,
        
      },
      {
        path: 'teacherList',
        title: '教师列表',
        icon: '',
        name: 'teacherList',
        component: () => import('@/views/school/teacherList'),
        hidden: false,
        
      },
      {
        path: 'teacherDetail',
        title: '教师详情',
        icon: '',
        name: 'teacherDetail',
        component: () => import('@/views/school/teacherDetail'),
        hidden: true,
        meta: {
        }
      },
      {
        path: 'bookList',
        title: '图书列列',
        icon: '',
        name: 'bookList',
        component: () => import('@/views/shop/bookList'),
        hidden: false,
        
      },
      {
        path: 'bookDetail',
        title: '图书详情',
        icon: '',
        name: 'bookDetail',
        component: () => import('@/views/shop/bookDetail'),
        hidden: true,
      },
      
    ]
  },
  
]
export default new Router({
  // mode: 'history',
  routes: constantRoutes
})
