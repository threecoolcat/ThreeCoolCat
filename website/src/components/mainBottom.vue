<template>
    <div class="mainBottom">
        <div style="width:1080px">
            <el-row>
                <el-col :span="6">
                    <div style="margin-top: 10px">友情链接</div>
                    <div v-for="item in friendLinks" :key="item.id" style="margin-top: 10px">
                        <a :href="item.url" style="color:#fff" target="_blank">{{ item.title}}</a></div>
                </el-col>
                <el-col :span="6">
                    <div style="margin-top: 10px">服务协议</div>
                    <div style="margin-top: 10px">合作沟通</div>
                    <div style="margin-top: 10px">关于我们</div>
                </el-col>
                <el-col :span="6">
                    <div style="margin-top: 10px">微信公众号</div>
                    <div style="background-color:#ccc;width:120px;height:120px;margin-top:10px"></div>
                </el-col>
                <el-col :span="6">
                    <div style="margin-top: 10px">咨询热线</div>
                    <div style="margin-top: 10px">
                        13x-xxxx-xxxx
                    </div>
                    <div style="margin-top: 10px">联系邮箱</div>
                    <div style="margin-top: 10px">
                        cnanyi@gmail.com
                    </div>
                    <div style="margin-top: 10px">公司地址</div>
                    <div style="margin-top: 10px">
                        天津市XX区XX路XX号
                    </div>
                </el-col>
            </el-row>
            <el-row type="flex" justify="center">
                <div style="margin-top:20px">ICP备案信息</div>
            </el-row>
        </div>
    </div>
</template>
<script>
import {friendLinks} from '@/api/home'
export default {
    data() {
        return {
            friendLinks: []
        }
    },
    mounted() {
        this.getFriendLinks()
    },
    methods: {
        getFriendLinks() {
            friendLinks().then(res=>{
                this.friendLinks = res.results;
            })
        }
    }
}
</script>
<style lang="less" scoped>
.mainBottom {
    height:240px;
    padding: 10px;
    color: #fff;
    background-color: #000;
    display:flex;
    justify-content: center;
}
</style>
