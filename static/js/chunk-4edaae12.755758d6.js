(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-4edaae12"],{"69b5":function(t,e,a){},"97e1":function(t,e,a){"use strict";a.r(e);var i=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",[t._l(t.teacherList,(function(e){return a("el-row",{key:e.id,staticClass:"grid-row course",attrs:{type:"flex",justify:"center"}},[a("el-col",{staticClass:"grid-block"},[a("div",{staticStyle:{padding:"20px 20px"}},[a("router-link",{attrs:{to:{path:"/teacherDetail",query:{id:e.id}}}},[a("img",{attrs:{src:e.photo,width:"200px",height:"200px"}})])],1),a("div",{staticStyle:{flex:"1"}},[a("router-link",{attrs:{to:{path:"/teacherDetail",query:{id:e.id}}}},[a("div",{staticClass:"title"},[t._v("姓名： "+t._s(e.name))])]),a("div",{staticClass:"content"},[t._v("关键词： "+t._s(e.keyword||"无"))]),a("div",{staticClass:"content"},[t._v("学位： "+t._s(e.title))]),a("div",{staticClass:"content"},[t._v("职位： "+t._s(e.duty))])],1)])],1)})),a("el-row",{staticClass:"grid-row",attrs:{type:"flex",justify:"center"}},[a("el-pagination",{attrs:{"current-page":t.currentPage,"page-sizes":[5,10,20,50],"page-size":t.pageSize,layout:"total, sizes, prev, pager, next, jumper",total:t.total},on:{"size-change":t.handleSizeChange,"current-change":t.handleCurrentChange}})],1)],2)},s=[],r=a("36d5"),n={data:function(){return{teacherList:[],currentPage:1,total:0,pageSize:5}},created:function(){this.getTeachers()},filters:{},methods:{getTeachers:function(){var t=this;Object(r["c"])({page:this.currentPage,size:this.pageSize}).then((function(e){t.teacherList=e.results,t.total=e.count}))},handleSizeChange:function(t){this.pageSize=t,this.currentPage=1,this.getTeachers()},handleCurrentChange:function(t){this.currentPage=t,this.getTeachers()}}},c=n,l=(a("ee17"),a("0c7c")),o=Object(l["a"])(c,i,s,!1,null,"36d7c27a",null);e["default"]=o.exports},ee17:function(t,e,a){"use strict";var i=a("69b5"),s=a.n(i);s.a}}]);