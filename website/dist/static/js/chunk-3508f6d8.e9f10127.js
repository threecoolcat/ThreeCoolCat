(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-3508f6d8"],{"52b2":function(t,e,a){"use strict";a.r(e);var o=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",[a("el-row",{attrs:{type:"flex",justify:"center"}},[a("el-col",{staticStyle:{width:"1080px"}},[a("el-breadcrumb",{staticStyle:{padding:"10px"},attrs:{separator:"/"}},[a("el-breadcrumb-item",{attrs:{to:{path:"/"}}},[t._v("首页")]),a("el-breadcrumb-item",[t._v("图书详情")])],1)],1)],1),a("el-row",{attrs:{type:"flex",justify:"center"}},[a("el-col",{staticStyle:{width:"1080px","background-color":"#fff",margin:"10px"}},[a("el-row",[a("el-col",{attrs:{span:18}},[a("el-card",[a("div",{staticStyle:{display:"flex"}},[a("img",{attrs:{src:t.getBookCoverUrl(t.book.cover),width:"120px"}}),a("div",[a("div",[t._v("《"+t._s(t.book.name)+"》")]),a("div",[t._v(t._s(t.book.author)+" 著")]),a("div",[t._v(t._s(t.book.sub_title))])])])])],1),a("el-col",{attrs:{span:6}})],1),a("el-row",{staticStyle:{"margin-top":"10px"}},[a("el-col",{attrs:{span:18}},[a("el-card",[a("el-tabs",{attrs:{type:"card"},model:{value:t.activeName,callback:function(e){t.activeName=e},expression:"activeName"}},[a("el-tab-pane",{attrs:{label:"目录",name:"first"}},[a("div",{staticStyle:{"min-height":"300px"}},[t._v(" "+t._s(t.book.menus_text)+" ")])]),a("el-tab-pane",{attrs:{label:"详情",name:"second"}},[a("div",{staticStyle:{"min-height":"300px"}},[t._v(" "+t._s(t.book.description)+" ")])])],1)],1)],1)],1)],1)],1)],1)},r=[],i=a("8dd4"),n={data:function(){return{book:{},activeName:"first"}},mounted:function(){this.getBook(this.$route.query.bookId)},methods:{getBook:function(t){var e=this;Object(i["a"])({id:t}).then((function(t){e.book=t[0]}))},getBookCoverUrl:function(t){return""+t}}},s=n,c=a("0c7c"),l=Object(c["a"])(s,o,r,!1,null,"645629c2",null);e["default"]=l.exports},"8dd4":function(t,e,a){"use strict";a.d(e,"a",(function(){return r})),a.d(e,"b",(function(){return i}));var o=a("b775");function r(t){return Object(o["a"])({url:"/shop/api/books/",method:"get",params:t})}function i(t){return Object(o["a"])({url:"/shop/api/videos/",method:"get",params:t})}}}]);