<template>
    <div>
        <div class="banner">
            <div style="flex:1" />
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
                        <div style="font-size:12px">{{course.intro}}&nbsp;</div>
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
                        <router-link :to="{path: '/Detail', query: {teacherId: teacher.id}}">
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
import { getCourses, getTeachers} from '@/api/school'
export default {
    data() {
        return {
            bookList: [],
            courseList: [],
            teacherList: [],
            videoList: [],
        }
    },
    created() {
        
    },
    mounted() {
        this.getBookList()
        this.getCourseList()
        this.getTeacherList()
        this.getVideoList()
    },
    methods: {
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
            var schoolId = window.localStorage.getItem('active-school')
            getCourses({page: 1, size: 5, school: schoolId}).then(res=>{
                this.courseList = res.results
            })
        },
        getTeacherList() {
            /**
             * 当前页面展示最多5条数据， 最后一条是“更多”，跳转至课程列表页面
             */
            var schoolId = window.localStorage.getItem('active-school')
            getTeachers({page: 1, size: 5, school: schoolId}).then(res=>{
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

.banner {
    height: 320px;
    background:linear-gradient(135deg,rgba(15,67,255,1) 0%, rgba(35,173,255,1) 75%);
    position: relative;
    display: flex;
    .title1 {
        position: absolute;
        left: 240px;
        top: 40px;
        color: #fff;
        font-size: 36px;
        
    }
    .title2 {
        position: absolute;
        left: 400px;
        top: 110px;
        color: #fff;
        font-size: 32px;
        transform:rotate(30deg);
    }
    .title3 {
        position: absolute;
        left: 580px;
        top: 160px;
        color: #fff;
        font-size: 32px;
        transform:rotate(90deg);
    }
    .title4 {
        position: absolute;
        left: 900px;
        top: 210px;
        color: #fff;
        font-size: 36px;
        transform:rotate(45deg);
    }
    .title5 {
        position: absolute;
        left: 800px;
        top: 200px;
        color: #fff;
        font-size: 24px;
        transform:rotate(17deg);
    }
    .title6 {
        position: absolute;
        left: 840px;
        top: 32px;
        color: #fff;
        font-size: 36px;
        
    }
}
.grid-row {
    &.even {
        background-color: #fff;
    }
    &.odd {
        background-color: #f1f2f3;
    }
    .grid-block {
        width:1080px;display:flex;flex-wrap:wrap;justify-content:left;
        .grid-content {
            // background-color: red;

            width: 280px;
            height: 160px;
            margin: 20px;
        }
        .grid-book {
            background-color: #fff;
            border:1px solid #ddd;
            padding: 10px;
            border-radius: 4px;
            display:flex;
            // justify-content: center;
            a {
                font-size:14px;
                width: 100%;
            }
        }
    }
    
}

</style>
