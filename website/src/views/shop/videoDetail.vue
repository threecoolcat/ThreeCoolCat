<template>
    <div>
        <el-row type="flex" class="grid-row course" justify="center">
            <el-col class="grid-block">
                <div style="padding:20px 20px">
                    <img :src="video.cover" width="160px" height="200px" />
                </div>
                <div style="flex:1">
                    <div class="title">视频名称： 《{{video.name}}》</div>
                    <div class="content">作者： {{video.author}}</div>
                </div>
            </el-col>
        </el-row>
        <el-row type="flex" class="grid-row" justify="center">
            <el-col class="grid-block">
                视频播放插件
            </el-col>
        </el-row>
    </div>
</template>
<script>
import { getVideos } from '@/api/shop'
export default {
    data() {
        return {
            video: {},
            activeName: 'first'
        }
    },
    created() {
        this.getVideos()
    },
    methods: {
        getVideos() {
            getVideos({id: this.$route.query.id}).then(res=>{
                this.video = res.results[0]
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
