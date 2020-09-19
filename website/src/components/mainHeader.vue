<template>
    <div class="mainHeader">
        <el-row type="flex" align="middle">
            <div style="flex:1"/>
            <div style="width:1080px;display:flex;justify-content:space-around">
                <div class="title">
                    <span>三酷猫教育</span>
                </div>
                <el-menu :default-active="$route.path" 
                    mode="horizontal"
                    background-color="#fff"
                    router
                    style="padding-left:40px"
                    >
                    <el-menu-item index="home" :route="{path: '/'}">首页</el-menu-item>
                    <el-submenu index="2">
                        <template slot="title">{{ activeSchoolName }}</template>
                        <el-menu-item v-for="school in schoolList" :key="school.id" @click="handleChangeSchool(school)">{{ school.name}}</el-menu-item>
                    </el-submenu>
                    <el-menu-item index="3" :route="{path: '/teacherList'}">名师风采</el-menu-item>
                    <el-menu-item index="4" :route="{path: '/courseList'}">课程设置</el-menu-item>
                    <el-menu-item index="5" :route="{path: '/bookList'}">精品图书</el-menu-item>
                    <el-menu-item index="6" :route="{path: '/hotNewList'}">热点资讯</el-menu-item>
                </el-menu>
                <div style="">
                    <div><a style="color:#17BA7A" href="/dashboard/">登录</a></div>
                </div>
            </div>
            <div style="flex:1"></div>
        </el-row>
    </div>
</template>

<script>
import {getSchools} from '@/api/school'
export default {
    name: 'mainHeader',
    data() {
        return {
            activeMenu: 'home', // 默认校区
            activeSchool: 1,
            schoolList: []
        }
    },
    // 过滤器
    filter: {},

    // 计算属性
    computed: {
        activeSchoolName() {
            for (var idx in this.schoolList) {
                if (this.schoolList[idx].id === this.activeSchool) {
                    return this.schoolList[idx].name
                } 
            }
            return this.schoolList[0]
        }
    },

    // 监听属性
    watch: {
        
    },

    // 模板编译挂载之后
    created() {
        
    },
    mounted() {
        getSchools().then(res=>{
            this.schoolList = res.results;
            var schoolId = window.localStorage.getItem('active-school')
            if (schoolId) {
                this.activeSchool = Number(schoolId)
            } else {
                this.activeSchool = 1
            }
        })
    },
    // 事件方法
    methods: {
        //切换当前学校
        handleChangeSchool(val) {
            window.localStorage.setItem('active-school', val.id)
            this.activeSchool = val.id
            this.$router.replace('/')
        }
    }

}
</script>

<style lang="less" scoped>
@main-color: #d9001b;
.mainHeader {
    line-height: 60px;
    .title {
        font-size:20px;
        font-weight:800;
        color:rgba(75,106,226,1);
    }
}
</style>
