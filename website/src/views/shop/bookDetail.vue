<template>
    <div>
        <el-row type="flex" class="grid-row course" justify="center">
            <el-col class="grid-block">
                <div style="padding:20px 20px">
                    <img :src="book.cover" width="160px" height="200px" />
                </div>
                <div style="flex:1">
                    <div class="title">图书名称： 《{{book.name}}》</div>
                    <div class="title">副标题： {{book.sub_title}}</div>
                    <div class="content">作者： {{book.author}}</div>
                </div>
            </el-col>
        </el-row>
        <el-row type="flex" class="grid-row" justify="center">
            <el-col class="grid-block">
                <el-tabs v-model="activeName" type="border-card" style="width:100%">
                    <el-tab-pane label="详情" name="first">
                        <div style="padding:20px" v-html="book.description"/>
                    </el-tab-pane>
                    <el-tab-pane label="目录" name="second">
                        <div style="padding:20px" v-html="book.menus_text" />
                    </el-tab-pane>
                </el-tabs>
            </el-col>
        </el-row>
    </div>
</template>
<script>
import { getBooks} from '@/api/shop'
export default {
    data() {
        return {
            book: {},
            activeName: 'first'
        }
    },
    created() {
        this.getBooks()
    },
    methods: {
        getBooks() {
            getBooks({id: this.$route.query.id}).then(res=>{
                this.book = res.results[0]
            })
        }
    }
}
</script>
<style lang="less" scoped>
.grid-row {
    margin: 0 0 20px 0;
    .grid-block {
    background-color: #eee;
    }
}
.course {
    background: none;
    .title {
        color:#333;
        font-size:20px;
        line-height:32px;
        padding:10px;
    }
    .content {
        color:#333;
        font-size:16px;
        line-height:24px;
        padding:10px;
    }
}
</style>
