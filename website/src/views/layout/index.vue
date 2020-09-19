<template>
<el-container style="position:relative">
  <el-header height="62">
    <main-header/>
  </el-header>
  <el-main>
    <router-view></router-view>
    <main-bottom/>
  </el-main>
  
</el-container>

</template>
<script>

import mainHeader from '@/components/mainHeader'
import mainBottom from '@/components/mainBottom'

export default {
  name: 'Layout',
  components: {mainHeader,mainBottom},
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
