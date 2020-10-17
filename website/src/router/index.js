import Vue from 'vue'
import Router from 'vue-router'
import Layout from '@/views/layout'
import Enroll from '@/components/enroll_h5'
Vue.use(Router)

export const constantRoutes = [
  {
    path: '/',
    component: Layout,
    children: [
      {
        path: '',
        name: 'home',
        component: () => import('@/views/home'),
        meta: {
          title: '首页',
        }
      },
      {
        path: 'articleList',
        name: 'articleList',
        component: () => import('@/views/home/articleList'),
        meta: {
          title: '文章列表',
        }
      },
      {
        path: 'article',
        name: 'article',
        component: () => import('@/views/home/article'),
        meta: {
          title: '文章详情',
        }
      },
      {
        path: 'schoolList',
        name: 'schoolList',
        component: () => import('@/views/school/schoolList'),
        meta: {
          title: '课程列表',
        }
      },
      {
        path: 'courseList',
        name: 'courseList',
        component: () => import('@/views/school/courseList'),
        meta: {
          title: '课程列表',
        }
      },
      {
        path: 'courseDetail',
        name: 'courseDetail',
        component: () => import('@/views/school/courseDetail'),
        meta: {
          title: '课程详情',
        }
        
      },
      {
        path: 'teacherList',
        name: 'teacherList',
        component: () => import('@/views/school/teacherList'),
        meta: {
          title: '教师列表',
        }
        
      },
      {
        path: 'teacherDetail',
        name: 'teacherDetail',
        component: () => import('@/views/school/teacherDetail'),
        meta: {
          title: '教师详情',
        }
      },
      {
        path: 'bookList',
        name: 'bookList',
        component: () => import('@/views/shop/bookList'),
        meta: {
          title: '图书列表',
        }
      },
      {
        path: 'bookDetail',
        name: 'bookDetail',
        component: () => import('@/views/shop/bookDetail'),
        meta: {
          title: '图书详情',
        }
      },
      {
        path: 'videoList',
        name: 'videoList',
        component: () => import('@/views/shop/videoList'),
        meta: {
          title: '视频列表',
        }
      },
      {
        path: 'videoDetail',
        name: 'videoDetail',
        component: () => import('@/views/shop/videoDetail'),
        meta: {
          title: '视频详情',
        }
      },
      
    ]
  },
  {
    path: '/Enroll',
    name: 'Enroll',
    component: Enroll,
    meta: {
      title: '微信报名页面',
    }
  },
]
export default new Router({
  routes: constantRoutes
})
