<template>
    <div>
        <el-row type="flex" justify="center" style="min-height: 500px">
            <el-col style="width:1080px">
                <!-- 标题 -->
                <div style="width:100%;text-align:center;font-size:28px">{{ article.title }}</div>
                <!-- 副标题 -->
                <div style="width:100%;text-align:right;font-size:16px">{{ article.subtitle }}</div>
                <!-- 分割线 -->
                <div style="border-bottom:1px solid #ddd;margin: 10px 0" />
                <!-- 内容 -->
                <div v-html="article.content" style="min-height:300px"/>
                <!-- 分割线 -->
                <div style="border-bottom:1px solid #ddd;margin: 10px 0" />
                
                <div style="width:100%;display:flex;justify-content: space-between">
                    <!-- 原文链接 -->
                    <div><a :href="article.link_url">原文链接</a></div>
                    <div>作者：{{article.author}}</div>
                </div>
            </el-col>
        </el-row>
    </div>
</template>
<script>
import { getArticles } from '@/api/home'
export default {
    data() {
        return {
            id: this.$route.query.id,
            type: this.$route.query.type,
            article: {},
        }
    },
    created() {
        this.getArticle()
    },
    methods: {
        getArticle() {
            getArticles(this.type, {id: this.id}).then(res=>{
                this.article = res.results[0]
                console.log(this.article)
            })
        }
    }
}
</script>
<style lang="less" scoped>

</style>
