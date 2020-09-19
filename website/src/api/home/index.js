import request from '@/utils/request'

/**
 * 友情链接后台接口
 */
export function friendLinks() {
    return request({
        url: '/home/api/friends/',
        method: 'get'
    })
}
