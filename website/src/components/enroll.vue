<template>
    <div>
        <div v-if="visible" class="pane fixed-pane">
            <el-row type="flex" justify="space-between" style="padding-right: 4px;padding-bottom:14px;border-bottom:1px solid #eeeeee">
                <div>我要报名</div>
                <div @click="visible = false" style="cursor:pointer" > x </div>
            </el-row>
            <el-form ref="form" :model="form" :rules="rules">
                <el-form-item label="学校" prop="school">
                    <el-select v-model="form.school" @change="getCourses()">
                        <el-option v-for="item in schools" :key="item.id" :label="item.name" :value="item.id" />
                    </el-select>
                </el-form-item>
                <el-form-item label="课程" prop="course">
                    <el-select v-model="form.course">
                        <el-option v-for="item in courses" :key="item.id" :label="item.name" :value="item.id" />
                    </el-select>
                </el-form-item>
                <el-form-item label="姓名" prop="name">
                    <el-input v-model="form.name" />
                </el-form-item>
                <el-form-item label="手机号" prop="phone">
                    <el-input v-model="form.phone" />
                </el-form-item>
                <el-form-item label="咨询内容">
                    <el-input v-model="form.content" type="textarea" />
                </el-form-item>

                <el-form-item style="text-align: center">
                    <el-button type="success" @click="submit" style="width: 120px;">提交申请</el-button>
                </el-form-item>
            </el-form>
        </div>
        <div v-else class="pane closed-pane" style="cursor:pointer" @click="visible = true;">
            我要报名
        </div>
    </div>

</template>
<script>
import { getSchools, getCourses, enroll } from '@/api/school'
// 右侧固定的报名页面
export default {
    name: 'enroll',
    data() {
        return {
            form: {
                name: '',
                phone: '',
                course: '',
                school: '',
                content: ''
            },
            visible: true,

            schools: [],
            courses: [],
            rules: {
                'school': [{required: true, trigger: 'change', message: '学校不能为空'}],
                'course': [{required: true, trigger: 'change', message: '课程不能为空'}],
                'name': [{required: true, trigger: 'blur', message: '姓名不能为空'}],
                'phone': [{required: true, trigger: 'blur', message: '手机号不能为空'}],
            }
        }
    },
    created() {
        this.getSchools()
    },
     methods: {
         submit() {
             // 表单校验
             this.$refs.form.validate((success)=>{
                 if (success) {
                     enroll(this.form).then(resp=>{
                         if (resp.success === 1) {
                             this.$alert('添加报名咨询信息成功， 请等待老师联系您！')
                         }
                     })
                 }
             })
         },
         getCourses() {
             getCourses({school: this.form.school}).then(resp=>{
                 this.courses = resp.results
                 this.form.course = ''
             })
         },
         getSchools() {
             getSchools().then(resp=>{
                 this.schools = resp.results
                 this.form.school = this.schools[0].id
                 this.getCourses()
             })
         }
     }
}
</script>
<style lang="less" scoped>
.pane {
    background-color: #ebfdec;
    padding: 16px;
}
.fixed-pane {
    position: fixed;
    right: 0px;
    top: 100px;
    width: 200px;
    height: 500px;
    
}
.closed-pane {
    position: fixed;
    right: 0px;
    top: 100px;
    width: 20px;
    height: 60px;
    cursor: pointer;
}
</style>
