<template>
    <div class="nav_menu scroll_box">
        <el-radio-group class="open_down" v-model="isCollapse">
            <!-- <el-radio-button v-show="isCollapse" :label="false" class="is_col"><img class="logoImg" src="@/assets/img/right.png" /></el-radio-button> -->
            <!-- <el-radio-button v-show="!isCollapse" :label="true" class="is_col"><img class="logoImg" src="@/assets/img/left.png" /></el-radio-button> -->
            <el-radio-button v-show="isCollapse" :label="false" class="is_col" :style="{right:isCollapse?'15px':'5px'}"><i class="el-icon-caret-right logoImg"></i></el-radio-button>
            <el-radio-button v-show="!isCollapse" :label="true" class="is_col"><i class="el-icon-caret-left logoImg"></i></el-radio-button>
        </el-radio-group>
        <el-menu :default-active="$route.meta.active" router class="el-menu-vertical-demo scroll_box" @open="handleOpen" @close="handleClose" :collapse="isCollapse" @select="handleSelect" active-text-color="#1c6f9e" text-color="rgb(191, 203, 217)">
            <template v-for="item in menuList">
                <el-menu-item v-if="!(item.children.length>0) && item.isShow" :index="item.code" :key="item.code" :class="{'qjts_border': item.name=='全局态势'?true:false}">
                    <i class="el_menu_i" :class="item.icon"></i>
                    <span slot="title">{{item.name}}</span>
                </el-menu-item>
                <el-submenu
                    v-if="item.children.length>0 && item.isShow"
                    :key="item.code"
                    :index="item.code"
                >
                    <template slot="title">
                        <i class="el_menu_i" :class="item.icon"></i>
                        <span slot="title">{{item.name}}</span>
                    </template>
                    <el-menu-item-group v-for="(subItem, subInd) in item.children" :key="subInd">
                        <template>
                            <el-menu-item :index="subItem.code" :key="subItem.code">{{subItem.name}}</el-menu-item>
                        </template>
                    </el-menu-item-group>
                </el-submenu>
            </template>

            <!-- <el-menu-item index="comSituation">
                <i class="el_menu_i el-icon-s-order"></i>
                <span slot="title">综合态势</span>
            </el-menu-item>
            <el-submenu index="7">
                <template slot="title">
                    <i class="el_menu_i el-icon-warning"></i>
                    <span slot="title">报警中心</span>
                </template>
                <el-menu-item-group>
                    <el-menu-item index="gjzx-ssgj">实时告警</el-menu-item>
                    <el-menu-item index="gjzx-sdgj">手动告警</el-menu-item>
                    <el-menu-item index="gjzx-lsgj">历史告警</el-menu-item>
                    <el-menu-item index="linkageManagement">联动管理</el-menu-item>
                    <el-menu-item index="taskManagement">任务管理</el-menu-item>
                </el-menu-item-group>
            </el-submenu>
            <el-submenu index="1">
                <template slot="title">
                    <i class="el_menu_i el-icon-video-camera-solid"></i>
                    <span slot="title">智慧安防</span>
                </template>
                <el-menu-item-group>
                    <el-menu-item index="monitor">实时监控</el-menu-item>
                    <el-menu-item index="personnelControl">人员布控</el-menu-item>
                    <el-menu-item index="videoPatrol">视频巡逻</el-menu-item>
                </el-menu-item-group>
            </el-submenu>
            <el-submenu index="2">
                <template slot="title">
                    <i class="el_menu_i el-icon-truck"></i>
                    <span slot="title">便捷通行</span>
                </template>
                <el-menu-item-group>
                    <el-menu-item index="personnelManage">人员管理</el-menu-item>
                    <el-menu-item index="vehicleManage">车辆管理</el-menu-item>
                </el-menu-item-group>
            </el-submenu>
            <el-menu-item index="energyConStatis">
                <i class="el_menu_i el-icon-s-opportunity"></i>
                <span slot="title">智慧能源</span>
            </el-menu-item>
            <el-menu-item index="smartDevice">
                <i class="el_menu_i el-icon-menu"></i>
                <span slot="title">设备智管</span>
            </el-menu-item>
            <el-menu-item index="manageDevice">
                <i class="el_menu_i el-icon-edit-outline"></i>
                <span slot="title">设备维护</span>
            </el-menu-item>
            <el-menu-item class="qjts_border" index="detailedSituation">
                <i class="el_menu_i el-icon-reading"></i>
                <span slot="title">全局态势</span>
            </el-menu-item>
            <el-menu-item index="businessCompare">
                <i class="el_menu_i el-icon-money"></i>
                <span slot="title">经营对比</span>
            </el-menu-item>
            <el-menu-item index="witConstruction">
                <i class="el_menu_i el-icon-school"> </i>
                <span slot="title">智慧工地</span>
            </el-menu-item>
            <el-submenu index="6">
                <template slot="title">
                    <i class="el_menu_i el-icon-s-operation"></i>
                    <span slot="title">系统管理</span>
                </template>
                <el-menu-item-group>
                    <el-menu-item index="systemManage">角色管理</el-menu-item>
                    <el-menu-item index="sysAuthorityManage">权限管理</el-menu-item>
                </el-menu-item-group>
            </el-submenu> -->
        </el-menu>
    </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
    name: 'navMenu',
    data() {
        return {
            isCollapse: false,
            menuList: [
                {
                    name: '综合态势',
                    code: 'comSituation',
                    icon: 'el-icon-s-order',
                    isShow: true,
                    children: []
                },
                {
                    name: '报警中心',
                    code: '1',
                    icon: 'el-icon-warning',
                    isShow: true,
                    children: [
                        {
                            name: '实时告警',
                            code: 'gjzx-ssgj',
                            isShow: true,
                        },
                        {
                            name: '手动告警',
                            code: 'gjzx-sdgj',
                            isShow: true,
                        },
                        {
                            name: '历史告警',
                            code: 'gjzx-lsgj',
                            isShow: true,
                        },
                        {
                            name: '联动管理',
                            code: 'linkageManagement',
                            isShow: true,
                        },
                        {
                            name: '任务管理',
                            code: 'taskManagement',
                            isShow: true,
                        }
                    ]
                },
                {
                    name: '智慧安防',
                    code: '2',
                    icon: 'el-icon-video-camera-solid',
                    isShow: true,
                    children: [
                        {
                            name: '实时监控',
                            code: 'monitor',
                            isShow: true,
                        },
                        {
                            name: '人员布控',
                            code: 'personnelControl',
                            isShow: true,
                        },
                        {
                            name: '视频巡逻',
                            code: 'videoPatrol',
                            isShow: true,
                        },
                    ]
                },
                {
                    name: '便捷通行',
                    code: '3',
                    icon: 'el-icon-truck',
                    isShow: true,
                    children: [
                        {
                            name: '人员管理',
                            code: 'personnelManage',
                            isShow: true,
                        },
                        {
                            name: '车辆管理',
                            code: 'vehicleManage',
                            isShow: true,
                        },
                    ]
                },
                {
                    name: '智慧能源',
                    code: 'energyConStatis',
                    icon: 'el-icon-s-opportunity',
                    isShow: true,
                    children: []
                },
                {
                    name: '设备智管',
                    code: 'smartDevice',
                    icon: 'el-icon-menu',
                    isShow: true,
                    children: []
                },
                {
                    name: '设备维护',
                    code: 'manageDevice',
                    icon: 'el-icon-edit-outline',
                    isShow: true,
                    children: []
                },
                {
                    name: '运营驾驶舱',
                    code: 'cockpitOperation',
                    icon: 'el-icon-set-up',
                    isShow: false,
                    children: []
                },
                {
                    name: '全局态势首页',
                    code: 'overallSituation',
                    icon: 'el-icon-reading',
                    isShow: false,
                    children: []
                },
                {
                    name: '全局态势',
                    code: 'detailedSituation',
                    icon: 'el-icon-reading',
                    isShow: true,
                    children: []
                },
                {
                    name: '经营对比',
                    code: 'businessCompare',
                    icon: 'el-icon-money',
                    isShow: true,
                    children: []
                },
                {
                    name: '智慧工地',
                    code: 'witConstruction',
                    icon: 'el-icon-school',
                    isShow: true,
                    children: []
                },
                 {
                    name: '系统管理',
                    code: '4',
                    icon: 'el-icon-s-operation',
                    isShow: true,
                    children: [
                        {
                            name: '角色管理',
                            code: 'systemManage',
                            isShow: true,
                        },
                        {
                            name: '权限管理',
                            code: 'sysAuthorityManage',
                            isShow: true
                        }
                    ]
                }
            ],
            userInfo: {},
            menu: [
                {

                }
            ],
        }
    },
    computed: {
        ...mapGetters([
            'permissioned_routes'
        ])
    },
    mounted() {
    },
    created() {
        console.log(this.$route);
        console.log(this.permissioned_routes);
        // this.menuList = this.permissioned_routes[0].children;
        console.log(this.menuList);
        if (localStorage.getItem('userInfo') !== undefined && localStorage.getItem('userInfo') !== '{}') {
            this.userInfo = JSON.parse(localStorage.getItem('userInfo'));
        }
    },
    methods: {
        changeMenu(val) {
            console.log(val);

            this.$router.push({ name: val })
        },
        handleOpen(key, keyPath) {
            console.log(key, keyPath);
        },
        handleClose(key, keyPath) {
            console.log(key, keyPath);
        },
        handleSelect(key, keyPath) {
            console.log(key, keyPath);
        },
    }
}
</script>

<style scoped lang="less">
.el-menu-vertical-demo:not(.el-menu--collapse) {
    // width: 200px;
    min-height: 400px;
}
.nav_menu {
    height:100%;
    overflow-y: auto;
    overflow-x: hidden;
    transition: width 1s;
    background: url("../assets/img/leftMenuBack.png") no-repeat;
    background-size: 100% 100%;
    .el_menu_i {
        // font-size: 15px;
        margin-right: 10px;
        color: rgb(191, 203, 217);
    }
    .qjts_border {
        border-top: 1px solid rgba(96, 136, 146, 0.48);
        box-shadow: 0px -5px 5px rgba(0,0,0,0.2);
    }
}
.el-menu {
    border-right: none;
    overflow-x: hidden;
    background: initial;
}
.open_down {
    position: absolute;
    z-index: 1;
    bottom: 10px;
    right: 5px;
    .logoImg {
      width: 30px;
      height: 30px;
      color: #fff;
      font-size: 30px;
    }
}
/deep/.el-menu-item,
.el-submenu__title {
    padding: 0 80px;
}
/deep/.el-submenu .el-menu-item {
    padding: 0px;
    min-width: 160px;
}
/deep/.is_col {
    span {
        background-color: #2a2f56 !important;
        border: none !important;
        padding: 0;
        box-shadow: none !important;
        &:hover {
            box-shadow: none !important;
        }
        &:active {
            box-shadow: none !important;
        }
    }
}
</style>
