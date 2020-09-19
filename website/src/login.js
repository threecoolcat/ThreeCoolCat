import router from './router'
const whiteList = ['/home']// 不重定向白名单
router.beforeEach(async(to, from, next) => {
  // var userInfo = localStorage.getItem('userInfo')
  // if (!userInfo) {
  //   try {
  //   var data = await logOnUser()
  //   localStorage.setItem('userInfo', JSON.stringify(data.data))
  //   } catch (e ) {
  //     window.location.href = process.env.VUE_APP_UC_LOGIN_URL
  //   }
  // }
  next()
  
})
