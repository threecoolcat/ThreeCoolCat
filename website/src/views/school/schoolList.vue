<template>
    <div>
        <el-row v-for="school in schoolList" :key="school.id" type="flex" class="grid-row school" justify="center">
            <el-col class="grid-block">
                <div style="padding:0 20px">
                    <img :src="school.cover" width="300px" height="320px" />
                </div>
                <div style="flex:1">
                    <div class="title">学校名称： {{school.name}}</div>
                    <div class="title"><div class="intro" v-html="school.intro"/> </div>
                    <div class="content">学校地址： {{school.address}}</div>
                    <div class="content">联系人： {{school.linkman}}</div>
                    <div class="content">联系电话： {{school.phone}}</div>
                    
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
import {getSchools} from '@/api/school'
export default {
    data() {
        return {
            schoolList: [],
            currentPage: 1,
            total: 0,
            pageSize: 5
        }
    },
    created() {
        this.getSchools()
    },
    methods: {
        getSchools() {
            getSchools({page: this.currentPage, size: this.pageSize}).then(res=>{
                this.schoolList = res.results
                this.total = res.count
            })
        },
        handleSizeChange(v) {
            this.pageSize = v;
            this.currentPage = 1;
            this.getSchools()
        },
        handleCurrentChange(v) {
            this.currentPage = v;
            this.getSchools()
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
.school {
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
