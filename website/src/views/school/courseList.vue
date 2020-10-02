<template>
    <div>
        <el-row v-for="course in courseList" :key="course.id" type="flex" class="grid-row course" justify="center">
            <el-col class="grid-block">
                <div style="padding:0 20px">
                    <img :src="course.cover" width="300px" height="320px" />
                </div>
                <div style="flex:1">
                    <div class="title">课程名称： {{course.name}}</div>
                    <div class="title"><div class="intro" v-html="course.intro"/> </div>
                    <div class="content">开课日期： {{course.start_date || '待定'}}</div>
                    <div class="content">类别： {{course.category | categroyLabel }}</div>
                    <div class="content">教师： {{course.teachers | teachersLabel}}</div>
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
import { getCourses} from '@/api/school'
export default {
    data() {
        return {
            courseList: [],
            currentPage: 1,
            total: 0,
            pageSize: 5
        }
    },
    created() {
        this.getCourses()
    },
    filters: {
        categroyLabel(v) {
            if (v === 1) {
                return '线下课程'
            }else {
                return '线上课程'
            }
        },
        teachersLabel(v) {
            return v.map(item=>{return item.name}).join(',')
        }
    },
    methods: {
        getCourses() {
            getCourses({page: this.currentPage, size: this.pageSize}).then(res=>{
                this.courseList = res.results;
                this.total = res.count
            })
        },
        handleSizeChange(v) {
            this.pageSize = v;
            this.currentPage = 1;
            this.getCourses()
        },
        handleCurrentChange(v) {
            this.currentPage = v;
            this.getCourses()
        }
    }
}
</script>
<style lang="less" scoped>
.grid-row {
    margin: 20px 0;
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
