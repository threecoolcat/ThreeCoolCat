<template>
    <div>
        <el-row v-for="video in videoList" :key="video.id" type="flex" class="grid-row course" justify="center">
            <el-col class="grid-block">
                <div style="padding:20px 20px">
                    <img :src="video.cover" width="160px" height="200px" />
                </div>
                <div style="flex:1">
                    <router-link :to="{path: '/videoDetail', query: {id: video.id}}">
                        <div class="title">视频名称：《{{video.name}}》</div>
                    </router-link>
                    <div class="content">作者： {{video.author}}</div>
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
import { getVideos } from '@/api/shop'
export default {
    data() {
        return {
            videoList: [],
            currentPage: 1,
            total: 0,
            pageSize: 5
        }
    },
    created() {
        this.getVideos()
    },
    methods: {
        getVideos() {
            getVideos({page: this.currentPage, size: this.pageSize}).then(res=>{
                this.videoList = res.results;
                this.total = res.count
            })
        },
        handleSizeChange(v) {
            this.pageSize = v;
            this.currentPage = 1;
            this.getVideos()
        },
        handleCurrentChange(v) {
            this.currentPage = v;
            this.getVideos()
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
