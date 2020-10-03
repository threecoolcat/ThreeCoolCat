<template>
    <div>
        <el-row v-for="book in bookList" :key="book.id" type="flex" class="grid-row course" justify="center">
            <el-col class="grid-block">
                <div style="padding:20px 20px">
                    <img :src="book.cover" width="160px" height="200px" />
                </div>
                <div style="flex:1">
                    <router-link :to="{path: '/bookDetail', query: {id: book.id}}">
                        <div class="title">图书名称： 《{{book.name}}》</div>
                    </router-link>
                    <div class="title">副标题： {{book.sub_title}}</div>
                    <div class="content">作者： {{book.author}}</div>
                </div>
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
import { getBooks } from '@/api/shop'
export default {
    data() {
        return {
            bookList: [],
            currentPage: 1,
            total: 0,
            pageSize: 5
        }
    },
    created() {
        this.getBooks()
    },
    methods: {
        getBooks() {
            getBooks({page: this.currentPage, size: this.pageSize}).then(res=>{
                this.bookList = res.results;
                this.total = res.count
            })
        },
        handleSizeChange(v) {
            this.pageSize = v;
            this.currentPage = 1;
            this.getBooks()
        },
        handleCurrentChange(v) {
            this.currentPage = v;
            this.getBooks()
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
