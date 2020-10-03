<template>
    <div>
        <!-- <div class="banner">
            <div style="width:1080px;position: relative;">
                <div class="title1">
                    Python3.8
                </div>
                <div class="title2">
                    Django 3
                </div>
                <div class="title5">
                    Admin
                </div>
                <div class="title3">
                    View
                </div>
                <div class="title4">
                    Template
                </div>
                <div class="title6">
                    Vue
                </div>
            </div>
        </div> -->
        <el-row type="flex" justify="center" class="grid-row school">
            <el-col class="grid-block">
                <div style="padding:0 20px">
                    <img :src="school.cover" width="300px" height="320px" />
                </div>
                <div style="flex:1">
                    <div style="color:#eee;font-size:18px;line-height:32px;padding:10px">学校名称： {{school.name}}</div>
                    <div style="color:#eee;font-size:18px;line-height:32px;padding:10px;"><div class="intro" v-html="school.intro"/> </div>
                    <div style="color:#eee;font-size:14px;line-height:24px;padding:10px">学校地址： {{school.address}}</div>
                    <div style="color:#eee;font-size:14px;line-height:24px;padding:10px">联系人： {{school.linkman}}</div>
                    <div style="color:#eee;font-size:14px;line-height:24px;padding:10px">联系电话： {{school.phone}}</div>
                    
                </div>
            </el-col>
        </el-row>
        <el-row type="flex" justify="center" class="grid-row even">
            <el-col class="grid-block">
                <el-divider>推荐课程</el-divider>
                <div v-for="course in courseList" :key="course.id" class="grid-content grid-book">
                    <div style="line-height:160px">
                        <router-link :to="{path: '/courseDetail', query: {courseId: course.id}}">
                            <img :src="getCoverUrl(course.cover)" :alt="course.name" width="100px" />
                        </router-link>
                    </div>
                    <div>
                        <div style="font-size:12px">《{{course.name}}》</div>
                        <!-- <div style="font-size:12px">{{book.author?book.author:'无名'}}&nbsp;著</div> -->
                        <div class="course-intro" v-html="course.intro"></div>
                    </div>
                </div>
                
                <div class="grid-content grid-book" style="font-size:20px; line-height:160px;text-align:center;color:#666">
                    <router-link to="/CourseList">更多</router-link>
                </div>
            </el-col>
        </el-row>
       <el-row type="flex" justify="center" class="grid-row even">
            
            <el-col class="grid-block">
                <el-divider>名师风采</el-divider>
                <div v-for="teacher in teacherList" :key="teacher.id" class="grid-content grid-book">
                    <div style="line-height:160px">
                        <router-link :to="{path: '/teacherDetail', query: {teacherId: teacher.id}}">
                            <img :src="getCoverUrl(teacher.cover)" :alt="teacher.name" width="100px" />
                        </router-link>
                    </div>
                    <div>
                        <div style="font-size:12px">{{teacher.name}}</div>
                    </div>
                </div>
                
                <div class="grid-content grid-book" style="font-size:20px; line-height:160px;text-align:center;color:#666">
                    <router-link to="/teacherList">更多</router-link>
                </div>
            </el-col>
        </el-row>
        <el-row type="flex" justify="center" class="grid-row odd">
            <el-col class="grid-block">
                 <el-divider class="odd">精品图书</el-divider>
                <div v-for="book in bookList" :key="book.id" class="grid-content grid-book">
                    <div style="line-height:160px">
                        <router-link :to="{path: '/bookDetail', query: {bookId: book.id}}">
                            <img :src="getCoverUrl(book.cover)" :alt="book.name" width="100px" />
                        </router-link>
                    </div>
                    <div>
                        <div style="font-size:12px">《{{book.name}}》</div>
                        <div style="font-size:12px">{{book.author?book.author:'无名'}}&nbsp;著</div>
                        <div style="font-size:12px">{{book.sub_title}}&nbsp;</div>
                    </div>
                </div>
                
                <div class="grid-content grid-book" style="font-size:14px; line-height:160px;text-align:center;color:#666">
                    <router-link to="/bookList">更多</router-link>
                </div>
            </el-col>
        </el-row>
        <el-row type="flex" justify="center" class="grid-row even">
            
            <el-col class="grid-block">
                <el-divider>线上视频</el-divider>
                <div v-for="video in videoList" :key="video.id" class="grid-content grid-book">
                    <div style="line-height:160px">
                        <router-link :to="{path: '/Detail', query: {teacherId: video.id}}">
                            <img :src="getCoverUrl(video.cover)" :alt="video.name" width="100px" />
                        </router-link>
                    </div>
                    <div>
                        <div style="font-size:12px">{{video.name}}</div>
                    </div>
                </div>
                
                <div class="grid-content grid-book" style="font-size:20px; line-height:160px;text-align:center;color:#666">
                    <router-link to="/videoList">更多</router-link>
                </div>
            </el-col>
        </el-row>
        
    </div>
</template>
<script>
import { getBooks, getVideos } from '@/api/shop'
import { getSchools, getCourses, getTeachers} from '@/api/school'
import { mapGetters } from 'vuex'
export default {
    data() {
        return {
            schoolId: null,
            school: {},
            bookList: [],
            courseList: [],
            teacherList: [],
            videoList: [],
        }
    },
    created() {
        this.getSchools()
        this.getBookList()
        this.getCourseList()
        this.getTeacherList()
        this.getVideoList()
    },
    computed: {
        ...mapGetters([
            'activeSchoolId'
        ])
    },
    watch: {
        activeSchoolId(v) {
            // 切换学校以后，切换对应的课程和教师
            this.getSchools()
            this.getCourseList()
            this.getTeacherList()
        }
    },
    methods: {
        getSchools() {
            getSchools({page: 1, size: 1, id: this.activeSchoolId}).then(res=>{
                this.school = res.results[0]
            })
        },
        getBookList() {
            /**
             * 当前页面展示最多5条数据， 最后一条是“更多”，跳转至图书列表页面
             */
            getBooks({page: 1, size: 5}).then(res=>{
                this.bookList = res.results
            })
        },
        getCourseList() {
            /**
             * 当前页面展示最多5条数据， 最后一条是“更多”，跳转至课程列表页面
             */
            getCourses({page: 1, size: 5, school: this.activeSchoolId}).then(res=>{
                this.courseList = res.results
            })
        },
        getTeacherList() {
            /**
             * 当前页面展示最多5条数据， 最后一条是“更多”，跳转至课程列表页面
             */
            getTeachers({page: 1, size: 5, school: this.activeSchoolId}).then(res=>{
                this.teacherList = res.results
            })
        },
        getVideoList() {
            /**
             * 当前页面展示最多5条数据， 最后一条是“更多”，跳转至课程列表页面
             */
            getVideos({page: 1, size: 5}).then(res=>{
                this.videoList = res.results
            })
        },
        getCoverUrl(url) {
            return process.env.VUE_APP_BASE_API + url
        }
    }
}
</script>
<style lang="less" scoped>
.course-intro {
    font-size:12px; 
    margin:6px;
    height:140px;
    overflow: hidden;
}



</style>
