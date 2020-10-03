<template>
    <div class="mainHeader">
        <el-row type="flex" justify="center">
            <!-- <div style="flex:1"/> -->
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
                    <el-menu-item index="/" :route="{path: '/'}">首页</el-menu-item>
                    <el-submenu index="">
                        <template slot="title">{{ activeSchoolName }}</template>
                        <el-menu-item v-for="school in schoolList" :key="school.id" @click="handleChangeSchool(school)">{{ school.name}}</el-menu-item>
                        <router-link to="/schoolList"><el-menu-item>更多...</el-menu-item></router-link>
                    </el-submenu>
                    <el-menu-item index="/teacherList" :route="{path: '/teacherList'}">名师风采</el-menu-item>
                    <el-menu-item index="/courseList" :route="{path: '/courseList'}">课程设置</el-menu-item>
                    <el-submenu index="/shop">
                    <template slot="title">商品</template>
                        <el-menu-item index="/bookList" :route="{path: '/bookList'}">图书</el-menu-item>
                        <el-menu-item index="/videoList" :route="{path: '/videoList'}">视频</el-menu-item>
                    </el-submenu>
                    
                    <el-submenu index="articleList">
                        <template slot="title">更多内容</template>
                        <el-menu-item index="articleList" :route="{path: '/articleList', query: {type: 'news'}}">新闻</el-menu-item>
                        <el-menu-item index="articleList" :route="{path: '/articleList', query: {type: 'active'}}">活动</el-menu-item>
                        <!-- <el-menu-item index="articleList" :route="{path: '/articleList', query: {type: 'tech'}}">技术文章</el-menu-item> -->
                    </el-submenu>
                </el-menu>
                <div style="">
                    <div><a style="color:#17BA7A" href="/dashboard/">登录</a></div>
                </div>
            </div>
        </el-row>
    </div>
</template>

<script>
import {getSchools} from '@/api/school'
import { mapGetters } from 'vuex'
export default {
    name: 'mainHeader',
    data() {
        return {
            activeMenu: 'home', // 默认校区
            schoolList: [],
            activeSchoolName: ''
        }
    },
    // 过滤器
    filter: {},
    // 计算属性
    computed: {
        ...mapGetters([
            'activeSchoolId',
        ]),
    },
    // 模板编译挂载之后
    created() {
        getSchools().then(res=>{
            this.schoolList = res.results;
            this.loadSchoolById(this.activeSchoolId)
        })
    },
    mounted() {
        
    },
    // 事件方法
    methods: {
        //切换当前学校
        handleChangeSchool(val) {
            this.$store.dispatch('changeSchool', val.id).then(()=>{
                this.loadSchoolById(val.id)
                this.$router.replace('/')
            })
        },
        loadSchoolById(schoolId) {
            for (var idx in this.schoolList) {
                if (this.schoolList[idx].id == schoolId) {
                    this.activeSchoolName = this.schoolList[idx].name
                    return;
                } 
            }
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
