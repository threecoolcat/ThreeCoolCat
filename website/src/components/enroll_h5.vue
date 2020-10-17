<template>
<div>
    <van-nav-bar
      title="三酷猫课堂"
      left-text=""
      right-text=""
      left-arrow
      @click-left="onClickLeft"
      @click-right="onClickRight"
    />
    <van-form @submit="submit" validate-first @failed="onFailed">
    <van-cell-group>
      <van-field :value="form.schoolName" label="学校" readonly clickable @click="showSchoolPicker = true" :rules="[{ required: true, message: '请选择学校' }]"/>
      <van-popup v-model="showSchoolPicker" position="bottom">
        <van-picker
          show-toolbar
          value-key="name"
          :columns="schools"
          @confirm="onConfirmSchool"
          @cancel="showSchoolPicker = false"
        />
      </van-popup>
      <van-field :value="form.courseName" label="课程" placeholder="请选择课程" readonly clickable @click="showCoursePicker = true"  :rules="[{ required: true, trigger: 'change', message: '请选择课程' }]"/>
      <van-popup v-model="showCoursePicker" position="bottom">
        <van-picker
          show-toolbar
          value-key="name"
          :columns="courses"
          @confirm="onConfirmCourse"
          @cancel="showCoursePicker = false"
        />
      </van-popup>
    </van-cell-group>  
    <van-cell-group>
      <van-field v-model="form.name" label="姓名" placeholder="请输入姓名" :rules="[{ required: true, message: '请填写姓名' }]"/>
      <van-field v-model="form.phone" label="手机号" placeholder="请输入手机号"  :rules="[{ required: true, message: '请填写手机号' }]"/>
      <van-field type="textarea" v-model="form.content" label="咨询内容" placeholder="请输入咨询内容" />
    </van-cell-group>
    <div style="margin: 16px;">
      <van-button round block type="info" native-type="submit">
        提交申请
      </van-button>
    </div>
    </van-form>
</div>
</template>
<script>
import { getSchools, getCourses, enroll } from '@/api/school'
export default {
  data() {
    return {
      schools: [],
      showSchoolPicker: false,
      courses: [],
      showCoursePicker: false,
      form: {
          name: '',
          phone: '',
          course: '',
          school: '',
          schoolName: '',
          content: ''
      },
    }
  },
  created() {
    this.getSchools()
  },
  methods: {
    onClickLeft() {},
    onClickRight() {},
    submit() {
      // 表单校验
      enroll(this.form).then(resp=>{
          if (resp.success === 1) {
              this.$dialog.alert({
                title: '申请成功',
                message: '添加报名咨询信息成功， 请等待老师联系您！',
              })
          }
      })
    },
    onFailed() { 

    },
    getCourses() {
        getCourses({school: this.form.school}).then(resp=>{
            this.courses = resp.results
            this.form.course = ''
        })
    },
    onConfirmSchool(v) {
      // this.form.school = v;
      this.form.school = v.id
      this.form.schoolName = v.name
      this.showSchoolPicker = false;
    },
    onConfirmCourse(v) {
      // this.form.school = v;
      this.form.course = v.id
      this.form.courseName = v.name
      this.showCoursePicker = false;
    },
    getSchools() {
        getSchools().then(resp=>{
            this.schools = resp.results
            this.form.school = this.schools[0].id
            this.form.schoolName = this.schools[0].name
            this.getCourses()
            
        })
    }
  }
}
</script>
<style lang="less" scoped>

</style>
