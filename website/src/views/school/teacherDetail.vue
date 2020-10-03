<template>
    <div>
        <el-row type="flex" class="grid-row course" justify="center">
            <el-col class="grid-block">
                <div style="padding:20px 20px">
                    <img :src="teacher.photo" width="200px" height="200px" />
                </div>
                <div style="flex:1">
                    <div class="title">姓名： {{teacher.name}}</div>
                    <div class="content">关键词： {{teacher.keyword || '无'}}</div>
                    <div class="content">学位： {{teacher.title}}</div>
                    <div class="content">职位： {{teacher.duty}}</div>
                </div>
            </el-col>
        </el-row>
        <el-row type="flex" class="grid-row" justify="center">
            <el-col class="grid-block">
                <div class="block-title">教师简介</div>
                <div style="padding:10px" v-html="teacher.intro" />
            </el-col>
        </el-row>
        <el-row type="flex" class="grid-row" justify="center">
            <el-col class="grid-block">
                <div class="block-title">任教课程</div>
                <div style="display:flex;width:100%">
                    <div v-for="course in teacher.courses" :key="course.id" style="width:120px;height:140px; margin:10px 20px;border-right:1px solid #ddd">
                        <img :src="'/files/' + course.cover" width="120px" />
                        <router-link :to="{path: '/courseDetail', query: {id: course.id}}"><div style="width:100%;text-align:center">{{course.name}}</div></router-link>
                    </div>
                </div>
            </el-col>
        </el-row>
    </div>
</template>
<script>
import { getTeachers} from '@/api/school'
export default {
    data() {
        return {
            teacher: {courses: []}
        }
    },
    filters: {
        
    },
    created() {
        this.getTeachers()
    },
    methods: {
        getTeachers() {
            getTeachers({id: this.$route.query.id}).then(res=>{
                this.teacher = res.results[0]
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
