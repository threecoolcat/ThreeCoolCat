<template>
    <div>
        <el-row type="flex" justify="center" style="min-height: 500px">
            <el-col style="width:1080px">
            <el-row>
                <el-col :span="6">
                    <el-menu
                        :default-active="activeMenu" style="min-height:500px"
                    >
                        <el-menu-item index="news" @click="handleClick('news')">新闻</el-menu-item>
                        <el-menu-item index="active" @click="handleClick('active')">活动</el-menu-item>
                        <!-- <el-menu-item index="tech" @click="handleClick('tech')">技术文章</el-menu-item> -->
                    </el-menu>
                </el-col>
                <el-col :span="18">
                    <div v-if="articleList.length > 0">
                        <div v-for="article in articleList" :key="article.id" style="padding:10px">    
                            <router-link :to="{path: '/article', query: {id: article.id, type: activeMenu}}">{{article.title}}</router-link>
                        </div>
                    </div>
                    <div v-else style="padding:10px">
                        暂无
                    </div>
                </el-col>
            </el-row>
            </el-col>
        </el-row>
        <el-row type="flex" class="grid-row" justify="center">
            
            <el-pagination
            @size-change="handleSizeChange"
            @current-change="handleCurrentChange"
            :current-page="currentPage"
            :page-sizes="[5, 10, 20, 50]"
            :page-size="pageSize"
            layout="total, sizes, prev, pager, next, jumper"
            :total="total">
            </el-pagination>
            
        </el-row>
    </div>
</template>
<script>
import { getArticles } from '@/api/home'
export default {
    data() {
        return {
            activeMenu: this.$route.query.type,
            articleList: [],
            currentPage: 1,
            pageSize: 5,
            total: 0
        }
    },
    created() {
        this.getArticles()
    },
    watch: {
        '$route.query.type' (v) {
            this.activeMenu = v;
            this.getArticles()
        }
    },
    methods: {
        getArticles() {
            console.log(this.activeMenu)
            getArticles(this.activeMenu, {page: this.currentPage, size: this.pageSize}).then(res=>{
                this.articleList = res.results;
                this.total = res.count;
            })
        },
        handleClick(type) {
            // 使用代码方式切换路由
            this.activeMenu = type
            
            this.$router.push({path: 'articleList', query: {type}})
        },
        handleSizeChange(v) {
            this.pageSize = v;
            this.currentPage = 1;
            this.getArticles()
        },
        handleCurrentChange(v) {
            this.currentPage = v;
            this.getArticles()
        }
    }
}
</script>
<style lang="less" scoped>

</style>
