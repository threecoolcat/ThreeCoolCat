import request from '@/utils/request'

/**
 * 精品图书后台接口
 */
export function getBooks(params) {
    return request({
        url: '/shop/api/books/',
        method: 'get',
        params
    })
}

/**
 * 视频后台接口
 */
export function getVideos(params) {
    return request({
        url: '/shop/api/videos/',
        method: 'get',
        params
    })
}
