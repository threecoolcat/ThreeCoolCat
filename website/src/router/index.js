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
        name: 'home',
        component: () => import('@/views/home'),
      },
      {
        path: 'hotNewList',
        title: '新闻列表',
        name: 'hotNewList',
        component: () => import('@/views/home/hotNewList'),
      },
      {
        path: 'hotNewDetail',
        title: '新闻详情',
        name: 'hotNewDetail',
        component: () => import('@/views/home/hotNewDetail'),
      },
      {
        path: 'schoolList',
        title: '课程列表',
        icon: '',
        name: 'schoolList',
        component: () => import('@/views/school/schoolList'),
      },
      {
        path: 'courseList',
        title: '课程列表',
        name: 'courseList',
        component: () => import('@/views/school/courseList'),
      },
      {
        path: 'courseDetail',
        title: '课程详情',
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
      },
      {
        path: 'bookList',
        title: '图书列列',
        name: 'bookList',
        component: () => import('@/views/shop/bookList'),
      },
      {
        path: 'bookDetail',
        title: '图书详情',
        name: 'bookDetail',
        component: () => import('@/views/shop/bookDetail'),
      },
      
    ]
  },
  
]
export default new Router({
  routes: constantRoutes
})
