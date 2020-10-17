<template>
<el-container style="position:relative">
  <el-header height="62px">
    <main-header/>
  </el-header>
  
  <el-main>
    <el-row type="flex" justify="center" v-if="$route.path != '/'">
      <el-col style="width:1080px">
          <el-breadcrumb separator="/" style="padding: 10px;">
              <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
              <el-breadcrumb-item >{{ $route.meta.title }}</el-breadcrumb-item>
          </el-breadcrumb>
      </el-col>
    </el-row>
    <router-view></router-view>
    <main-bottom/>
  </el-main>
  <enroll />
</el-container>

</template>
<script>

import mainHeader from '@/components/mainHeader'
import mainBottom from '@/components/mainBottom'
import enroll from '@/components/enroll'

export default {
  name: 'Layout',
  components: {mainHeader,mainBottom, enroll},
  props: { },
  data () {
    return {
      
    }
  },
  // 过滤器
  filter: {},

  // 计算属性

  // 监听属性
  watch: {
    
  },

  // 组件创建属性绑定，DOM未生成
  created () {
  },

  // 模板编译挂载之后
  mounted () {
  },

  // 组件更新前
  beforeUpdate () {},

  // 组件更新后
  updated () {
  },

  // 组件销毁前
  beforeDestroy () {},

  // 组件销毁后
  destroyed () {},

  // 事件方法
  methods: {
    
  }

}
</script>

<style scoped lang="less">
.el-header {
  position: fixed;
  z-index: 999;
  width: 100%;

  background:rgba(255,255,255,1);
  box-shadow:0px 2px 14px 0px rgba(4,0,0,0.2);
}
.el-main {
  margin-top: 62px;
  padding:0px;
  background: #fdfdfd;
}
</style>
