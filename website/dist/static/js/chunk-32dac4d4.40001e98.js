(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-32dac4d4"],{1950:function(t,e,s){},bc35:function(t,e,s){"use strict";s.r(e);var i=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",[s("el-row",{staticClass:"grid-row course",attrs:{type:"flex",justify:"center"}},[s("el-col",{staticClass:"grid-block"},[s("div",{staticStyle:{padding:"20px 20px"}},[s("img",{attrs:{src:t.course.cover,width:"300px",height:"320px"}})]),s("div",{staticStyle:{flex:"1"}},[s("div",{staticClass:"title"},[t._v("课程名称： "+t._s(t.course.name))]),s("div",{staticClass:"title"},[s("div",{staticClass:"intro",domProps:{innerHTML:t._s(t.course.intro)}})]),s("div",{staticClass:"content"},[t._v("开课日期： "+t._s(t.course.start_date||"待定"))]),s("div",{staticClass:"content"},[t._v("授课形式： "+t._s(t._f("categroyLabel")(t.course.category)))]),s("div",{staticClass:"content"},[t._v("主讲教师： "+t._s(t._f("teachersLabel")(t.course.teachers)))])])])],1),s("el-row",{staticClass:"grid-row",attrs:{type:"flex",justify:"center"}},[s("el-col",{staticClass:"grid-block"},[s("div",{staticClass:"block-title"},[t._v("课程介绍")]),s("div",{staticStyle:{padding:"10px"},domProps:{innerHTML:t._s(t.course.intro)}})])],1),s("el-row",{staticClass:"grid-row",attrs:{type:"flex",justify:"center"}},[s("el-col",{staticClass:"grid-block"},[s("div",{staticClass:"block-title"},[t._v("主讲教师")]),s("div",{staticStyle:{display:"flex",width:"100%"}},t._l(t.course.teachers,(function(e){return s("div",{key:e.id,staticStyle:{width:"120px",height:"140px",margin:"10px 20px","border-right":"1px solid #ddd"}},[s("img",{attrs:{src:"/files/"+e.photo,width:"120px"}}),s("router-link",{attrs:{to:{path:"/teacherDetail",query:{id:e.id}}}},[s("div",{staticStyle:{width:"100%","text-align":"center"}},[t._v(t._s(e.name))])])],1)})),0)])],1)],1)},r=[],c=s("36d5"),a={data:function(){return{course:{teachers:[]}}},filters:{categroyLabel:function(t){return 1===t?"线下课程":"线上课程"},teachersLabel:function(t){return t.map((function(t){return t.name})).join(",")}},created:function(){this.getCourses()},methods:{getCourses:function(){var t=this;Object(c["a"])({id:this.$route.query.id}).then((function(e){t.course=e.results[0]}))}}},o=a,n=(s("dff7"),s("0c7c")),l=Object(n["a"])(o,i,r,!1,null,"558ba52c",null);e["default"]=l.exports},dff7:function(t,e,s){"use strict";var i=s("1950"),r=s.n(i);r.a}}]);