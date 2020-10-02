<template>
    <div>
        <el-row type="flex" class="grid-row course" justify="center">
            <el-col class="grid-block">
                <div style="padding:20px 20px">
                    <img :src="course.cover" width="300px" height="320px" />
                </div>
                <div style="flex:1">
                    <div class="title">课程名称： {{course.name}}</div>
                    <div class="title"><div class="intro" v-html="course.intro"/> </div>
                    <div class="content">开课日期： {{course.start_date || '待定'}}</div>
                    <div class="content">授课形式： {{course.category | categroyLabel }}</div>
                    <div class="content">主讲教师： {{course.teachers | teachersLabel}}</div>
                </div>
            </el-col>
        </el-row>
        <el-row type="flex" class="grid-row" justify="center">
            <el-col class="grid-block">
                <div style="width:100%;text-align:center;font-size:18px;line-height:36px;border-bottom:1px solid #ddd">课程介绍</div>
                <div style="padding:10px" v-html="course.intro" />
            </el-col>
        </el-row>
        <el-row type="flex" class="grid-row" justify="center">
            <el-col class="grid-block">
                <div style="width:100%;text-align:center;font-size:18px;line-height:36px;border-bottom:1px solid #ddd">主讲教师</div>
                <div style="display:flex;width:100%">
                    <div v-for="teacher in course.teachers" :key="teacher.id" style="width:120px;height:140px; margin:10px 20px;border-right:1px solid #ddd">
                        <img :src="'/files/' + teacher.photo" width="120px" />
                        <router-link :to="{path: '/teacherDetail', query: {id: teacher.id}}"><div style="width:100%;text-align:center">{{teacher.name}}</div></router-link>
                    </div>
                </div>
            </el-col>
        </el-row>
    </div>
</template>
<script>
import { getCourses} from '@/api/school'
export default {
    data() {
        return {
            course: {teachers: []}
        }
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
    created() {
        this.getCourses()
    },
    methods: {
        getCourses() {
            getCourses({id: this.$route.query.id}).then(res=>{
                this.course = res.results[0]
            })
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
