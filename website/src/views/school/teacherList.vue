<template>
    <div>
        <el-row v-for="teacher in teacherList" :key="teacher.id" type="flex" class="grid-row course" justify="center">
            <el-col class="grid-block">
                <div style="padding:20px 20px">
                    <router-link :to="{path: '/teacherDetail', query: {id: teacher.id}}">
                        <img :src="teacher.photo" width="200px" height="200px" />
                    </router-link>
                </div>
                <div style="flex:1">
                    <router-link :to="{path: '/teacherDetail', query: {id: teacher.id}}">
                        <div class="title">姓名： {{teacher.name}}</div>
                    </router-link>
                    <div class="content">关键词： {{teacher.keyword || '无'}}</div>
                    <div class="content">学位： {{teacher.title}}</div>
                    <div class="content">职位： {{teacher.duty}}</div>
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
import { getTeachers} from '@/api/school'
export default {
    data() {
        return {
            teacherList: [],
            currentPage: 1,
            total: 0,
            pageSize: 5
        }
    },
    created() {
        this.getTeachers()
    },
    filters: {
        
    },
    methods: {
        getTeachers() {
            getTeachers({page: this.currentPage, size: this.pageSize}).then(res=>{
                this.teacherList = res.results;
                this.total = res.count
            })
        },
        handleSizeChange(v) {
            this.pageSize = v;
            this.currentPage = 1;
            this.getTeachers()
        },
        handleCurrentChange(v) {
            this.currentPage = v;
            this.getTeachers()
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
