import axios from 'axios'
import { MessageBox, Message } from 'element-ui'
// create an axios instance
const service = axios.create({
    baseURL: process.env.VUE_APP_BASE_API, // url = base url + request url
    withCredentials: true, // send cookies when cross-domain requests
    timeout: 5000 // request timeout
})

// request interceptor
service.interceptors.request.use(
    config => {
        // do something before request is sent
        // config.headers['x-token'] = getToken()
        return config
    },
    error => {
    // do something with request error
        console.log('request: ', error) // for debug
        return Promise.reject(error)
    }
)

// response interceptor
service.interceptors.response.use(
    /**
   * If you want to get http information such as headers or status
   * Please return  response => response
  */

    /**
   * Determine the request status by custom code
   * Here is just an example
   * You can also judge the status by HTTP Status Code
   */
    response => {
        const res = response.data
        const status = response.status
        // if the custom code is not 20000, it is judged as an error.

            // 50008: ;; 50012: Other clients logged in; 50014: Token expired;
            if (status !== 200) {
                return Promise.reject(new Error(res.msg || res.message || 'Error'))
            }
            return res
    },
    error => {
        if (process.env.NODE_ENV === 'development') {
            // console.log('response:', error) // for debug
        }
        // window.location.href = process.env.VUE_APP_UC_LOGIN_URL
        // Message({
        //     message: error.message,
        //     type: 'error',
        //     duration: 5 * 1000
        // })
        // store.dispatch('user/resetToken').then(() => {
        //     //location.reload()
        //     if (location.href.indexOf('#/login') < 0) {
        //         location.reload()
        //     }
        // })
        return Promise.reject(error)
    }
)

export default service
