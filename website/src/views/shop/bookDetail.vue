<template>
    <div>
        <el-row type="flex" justify="center">
            <el-col style="width:1080px">
                <el-breadcrumb separator="/" style="padding: 10px;">
                    <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
                    <el-breadcrumb-item>图书详情</el-breadcrumb-item>
                </el-breadcrumb>
            </el-col>
        </el-row>
        <el-row type="flex" justify="center">
            <el-col style="width:1080px;background-color:#fff;margin:10px">
                <el-row>
                    <el-col :span="18">
                        <el-card>
                            <div style="display:flex">
                                <img :src="getBookCoverUrl(book.cover)" width="120px" />
                                <div>
                                    <div>《{{ book.name }}》</div>

                                    <div>{{ book.author }}&nbsp;著</div>
                                    <div>{{ book.sub_title }}</div>
                                </div>
                            </div>
                        </el-card>
                        
                    </el-col>
                    <el-col :span="6">

                    </el-col>
                </el-row>
                    
                <el-row style="margin-top:10px">
                    <el-col :span="18">
                        <el-card>
                            <el-tabs v-model="activeName" type="card">
                                <el-tab-pane label="目录" name="first">
                                    <div style="min-height:300px">
                                        {{ book.menus_text }}
                                    </div>
                                </el-tab-pane>
                                <el-tab-pane label="详情" name="second">
                                    <div style="min-height:300px">
                                        {{ book.description}}
                                    </div>
                                </el-tab-pane>
                            </el-tabs>
                        </el-card>
                    </el-col>
                </el-row>
            </el-col>
        </el-row>
    </div>
</template>
<script>
import { getBooks } from '@/api/shop'
export default {
    data() {
        return {
            book: {},
            activeName: 'first'
        }
    },
    mounted() {
        this.getBook(this.$route.query.bookId)
    },
    methods: {
        getBook(id) {
            getBooks({id: id}).then(res=>{
                this.book = res[0]
            })
        },
        getBookCoverUrl(url) {
            return process.env.VUE_APP_BASE_API + url
        }
    }
}
</script>
<style lang="less" scoped>

</style>
