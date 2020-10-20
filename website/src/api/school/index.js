import request from '@/utils/request'
import Cookie from 'js-cookie'
/**
 * 校区后台接口
 */
export function getSchools(params) {
    return request({
        url: '/school/api/schools/',
        method: 'get',
        params
    })
}
/**
 * 校区栏目后台接口
 */
export function getCourses(params) {
    return request({
        url: '/school/api/courses/',
        method: 'get',
        params
    })
}

/**
 * 教师后台接口
 */
export function getTeachers(params) {
    return request({
        url: '/school/api/teachers/',
        method: 'get',
        params
    })
}

/**
 * 报名接口
 */
export function enroll(data) {
    return request({
        headers: {'X-CSRFtoken': Cookie.get('csrftoken')},
        url: '/school/api/enroll/',
        method: 'post',
        data
    })
}
