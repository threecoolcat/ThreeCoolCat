import request from '@/utils/request'
import Cookie from 'js-cookie'
/**
 * 友情链接后台接口
 */
export function friendLinks() {
    return request({
        url: '/home/api/friends/',
        method: 'get'
    })
}

/**
 * 文章接口
 */
export function getArticles(type, params) {
    return request({
        url: '/home/api/article/'+type,
        method: 'get',
        params
    })
}

/**
 * 操作日志
 */
export function log(data) {
    return request({
        url: '/home/api/log',
        method: 'post',
        data,
        headers: {'X-CSRFtoken': Cookie.get('csrftoken')}
    })
}
