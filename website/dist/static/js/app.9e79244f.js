(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["app"],{0:function(t,e,n){t.exports=n("56d7")},"034f":function(t,e,n){"use strict";var i=n("446e"),a=n.n(i);a.a},"0a35":function(t,e,n){"use strict";var i=n("ba9e"),a=n.n(i);a.a},"2f3b":function(t,e,n){"use strict";n.d(e,"a",(function(){return a})),n.d(e,"b",(function(){return o}));var i=n("b775");function a(){return Object(i["a"])({url:"/home/api/friends/",method:"get"})}function o(t,e){return Object(i["a"])({url:"/home/api/article/"+t,method:"get",params:e})}},"36d5":function(t,e,n){"use strict";n.d(e,"b",(function(){return a})),n.d(e,"a",(function(){return o})),n.d(e,"c",(function(){return r}));var i=n("b775");function a(t){return Object(i["a"])({url:"/school/api/schools/",method:"get",params:t})}function o(t){return Object(i["a"])({url:"/school/api/courses/",method:"get",params:t})}function r(t){return Object(i["a"])({url:"/school/api/teachers/",method:"get",params:t})}},"446e":function(t,e,n){},"48fc":function(t,e,n){},"56d7":function(t,e,n){"use strict";n.r(e);var i=n("2b0e"),a=n("2f62");i["default"].use(a["a"]);var o=new a["a"].Store({state:{activeSchoolId:window.localStorage.getItem("active-school")||1,activeSchoolName:window.localStorage.getItem("active-school-name")},getters:{activeSchoolId:function(t){return t.activeSchoolId},activeSchoolName:function(t){return t.activeSchoolName}},mutations:{CHANGE_SCHOOL:function(t,e){t.activeSchoolId=e,window.localStorage.setItem("active-school",e)}},actions:{changeSchool:function(t,e){var n=t.commit;n("CHANGE_SCHOOL",e)}},modules:{}}),r=o,c=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{attrs:{id:"app"}},[n("router-view")],1)},u=[],s={name:"App"},l=s,d=(n("034f"),n("0c7c")),p=Object(d["a"])(l,c,u,!1,null,null,null),h=p.exports,m=n("bc3a"),f=n.n(m),v=n("5c96"),b=n.n(v),x=(n("0fae"),n("6859"),n("8c4f")),y=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("el-container",{staticStyle:{position:"relative"}},[n("el-header",{attrs:{height:"62px"}},[n("main-header")],1),n("el-main",["/"!=t.$route.path?n("el-row",{attrs:{type:"flex",justify:"center"}},[n("el-col",{staticStyle:{width:"1080px"}},[n("el-breadcrumb",{staticStyle:{padding:"10px"},attrs:{separator:"/"}},[n("el-breadcrumb-item",{attrs:{to:{path:"/"}}},[t._v("首页")]),n("el-breadcrumb-item",[t._v(t._s(t.$route.meta.title))])],1)],1)],1):t._e(),n("router-view"),n("main-bottom")],1)],1)},g=[],S=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"mainHeader"},[n("el-row",{attrs:{type:"flex",justify:"center"}},[n("div",{staticStyle:{width:"1080px",display:"flex","justify-content":"space-around"}},[n("div",{staticClass:"title"},[n("span",[t._v("三酷猫教育")])]),n("el-menu",{staticStyle:{"padding-left":"40px"},attrs:{"default-active":t.$route.path,mode:"horizontal","background-color":"#fff",router:""}},[n("el-menu-item",{attrs:{index:"/",route:{path:"/"}}},[t._v("首页")]),n("el-submenu",{attrs:{index:""}},[n("template",{slot:"title"},[t._v(t._s(t.activeSchoolName))]),t._l(t.schoolList,(function(e){return n("el-menu-item",{key:e.id,on:{click:function(n){return t.handleChangeSchool(e)}}},[t._v(t._s(e.name))])})),n("router-link",{attrs:{to:"/schoolList"}},[n("el-menu-item",[t._v("更多...")])],1)],2),n("el-menu-item",{attrs:{index:"/teacherList",route:{path:"/teacherList"}}},[t._v("名师风采")]),n("el-menu-item",{attrs:{index:"/courseList",route:{path:"/courseList"}}},[t._v("课程设置")]),n("el-menu-item",{attrs:{index:"/bookList",route:{path:"/bookList"}}},[t._v("精品图书")]),n("el-submenu",{attrs:{index:"articleList"}},[n("template",{slot:"title"},[t._v("更多内容")]),n("el-menu-item",{attrs:{index:"articleList",route:{path:"/articleList",query:{type:"news"}}}},[t._v("新闻")]),n("el-menu-item",{attrs:{index:"articleList",route:{path:"/articleList",query:{type:"active"}}}},[t._v("活动")])],2)],1),n("div",{},[n("div",[n("a",{staticStyle:{color:"#17BA7A"},attrs:{href:"/dashboard/"}},[t._v("登录")])])])],1)])],1)},_=[],w=n("36d5");function L(t,e){var n=Object.keys(t);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(t);e&&(i=i.filter((function(e){return Object.getOwnPropertyDescriptor(t,e).enumerable}))),n.push.apply(n,i)}return n}function O(t){for(var e=1;e<arguments.length;e++){var n=null!=arguments[e]?arguments[e]:{};e%2?L(Object(n),!0).forEach((function(e){k(t,e,n[e])})):Object.getOwnPropertyDescriptors?Object.defineProperties(t,Object.getOwnPropertyDescriptors(n)):L(Object(n)).forEach((function(e){Object.defineProperty(t,e,Object.getOwnPropertyDescriptor(n,e))}))}return t}function k(t,e,n){return e in t?Object.defineProperty(t,e,{value:n,enumerable:!0,configurable:!0,writable:!0}):t[e]=n,t}var j={name:"mainHeader",data:function(){return{activeMenu:"home",schoolList:[],activeSchoolName:""}},filter:{},computed:O({},Object(a["b"])(["activeSchoolId"])),created:function(){var t=this;Object(w["b"])().then((function(e){t.schoolList=e.results,t.loadSchoolById(t.activeSchoolId)}))},mounted:function(){},methods:{handleChangeSchool:function(t){var e=this;this.$store.dispatch("changeSchool",t.id).then((function(){e.loadSchoolById(t.id),e.$router.replace("/")}))},loadSchoolById:function(t){for(var e in this.schoolList)if(this.schoolList[e].id==t)return void(this.activeSchoolName=this.schoolList[e].name)}}},I=j,C=(n("ed00"),Object(d["a"])(I,S,_,!1,null,"05d75c6a",null)),P=C.exports,D=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"mainBottom"},[n("div",{staticStyle:{width:"1080px"}},[n("el-row",[n("el-col",{attrs:{span:6}},[n("div",{staticStyle:{"margin-top":"10px"}},[t._v("友情链接")]),t._l(t.friendLinks,(function(e){return n("div",{key:e.id,staticStyle:{"margin-top":"10px"}},[n("a",{staticStyle:{color:"#fff"},attrs:{href:e.url,target:"_blank"}},[t._v(t._s(e.title))])])}))],2),n("el-col",{attrs:{span:6}},[n("div",{staticStyle:{"margin-top":"10px"}},[t._v("服务协议")]),n("div",{staticStyle:{"margin-top":"10px"}},[t._v("合作沟通")]),n("div",{staticStyle:{"margin-top":"10px"}},[t._v("关于我们")])]),n("el-col",{attrs:{span:6}},[n("div",{staticStyle:{"margin-top":"10px"}},[t._v("主页")]),n("div",{staticStyle:{"background-color":"#ccc",width:"130px",height:"130px","margin-top":"10px"}},[n("img",{attrs:{src:"static/ThreeCoolCat.png",width:"130px",height:"130px"}})])]),n("el-col",{attrs:{span:6}},[n("div",{staticStyle:{"margin-top":"10px"}},[t._v("咨询热线")]),n("div",{staticStyle:{"margin-top":"10px"}},[t._v(" 1xxx-xxxx-xxxx ")]),n("div",{staticStyle:{"margin-top":"10px"}},[t._v("联系邮箱")]),n("div",{staticStyle:{"margin-top":"10px"}},[t._v(" xxxxx@xxxx.xxx ")]),n("div",{staticStyle:{"margin-top":"10px"}},[t._v("公司地址")]),n("div",{staticStyle:{"margin-top":"10px"}},[t._v(" 北京市XX区XX路XX号 ")])])],1),n("el-row",{attrs:{type:"flex",justify:"center"}},[n("div",{staticStyle:{"margin-top":"20px"}},[t._v("ICP备案信息")])])],1)])},E=[],$=n("2f3b"),N={data:function(){return{friendLinks:[]}},mounted:function(){this.getFriendLinks()},methods:{getFriendLinks:function(){var t=this;Object($["a"])().then((function(e){t.friendLinks=e.results}))}}},H=N,B=(n("7af2"),Object(d["a"])(H,D,E,!1,null,"49e2603e",null)),X=B.exports,A={name:"Layout",components:{mainHeader:P,mainBottom:X},props:{},data:function(){return{}},filter:{},watch:{},created:function(){},mounted:function(){},beforeUpdate:function(){},updated:function(){},beforeDestroy:function(){},destroyed:function(){},methods:{}},q=A,U=(n("0a35"),Object(d["a"])(q,y,g,!1,null,"1f39b778",null)),z=U.exports;i["default"].use(x["a"]);var F=[{path:"/",component:z,children:[{path:"",name:"home",component:function(){return n.e("chunk-76385074").then(n.bind(null,"7abe"))},meta:{title:"首页"}},{path:"articleList",name:"articleList",component:function(){return n.e("chunk-2d0c4688").then(n.bind(null,"3b69"))},meta:{title:"文章列表"}},{path:"article",name:"article",component:function(){return n.e("chunk-2d21d493").then(n.bind(null,"d13c"))},meta:{title:"文章详情"}},{path:"schoolList",name:"schoolList",component:function(){return n.e("chunk-65269ca3").then(n.bind(null,"94d0"))},meta:{title:"课程列表"}},{path:"courseList",name:"courseList",component:function(){return n.e("chunk-1cb8ae40").then(n.bind(null,"746e"))},meta:{title:"课程列表"}},{path:"courseDetail",name:"courseDetail",component:function(){return n.e("chunk-32dac4d4").then(n.bind(null,"bc35"))},meta:{title:"课程详情"}},{path:"teacherList",name:"teacherList",component:function(){return n.e("chunk-4edaae12").then(n.bind(null,"97e1"))},meta:{title:"教师列表"}},{path:"teacherDetail",name:"teacherDetail",component:function(){return n.e("chunk-085343ae").then(n.bind(null,"e298"))},meta:{title:"教师详情"}},{path:"bookList",name:"bookList",component:function(){return n.e("chunk-dca24672").then(n.bind(null,"03df"))},meta:{title:"图书列表"}},{path:"bookDetail",name:"bookDetail",component:function(){return n.e("chunk-c6139146").then(n.bind(null,"52b2"))},meta:{title:"图书详情"}}]}],G=new x["a"]({routes:F});i["default"].use(b.a,{size:"small"}),i["default"].prototype.$http=f.a,i["default"].config.productionTip=!1,new i["default"]({el:"#app",router:G,store:r,render:function(t){return t(h)}})},6859:function(t,e,n){},"7af2":function(t,e,n){"use strict";var i=n("ae9f"),a=n.n(i);a.a},ae9f:function(t,e,n){},b775:function(t,e,n){"use strict";var i=n("bc3a"),a=n.n(i),o=(n("5c96"),a.a.create({baseURL:"",withCredentials:!0,timeout:5e3}));o.interceptors.request.use((function(t){return t}),(function(t){return console.log("request: ",t),Promise.reject(t)})),o.interceptors.response.use((function(t){var e=t.data,n=t.status;return 200!==n?Promise.reject(new Error(e.msg||e.message||"Error")):e}),(function(t){return Promise.reject(t)})),e["a"]=o},ba9e:function(t,e,n){},ed00:function(t,e,n){"use strict";var i=n("48fc"),a=n.n(i);a.a}},[[0,"runtime","chunk-elementUI","chunk-libs"]]]);