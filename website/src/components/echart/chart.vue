<!-- 组件说明 -->
<template>
<!-- <bs-card class="chart-content margin-bottom-medium" shadow="hover" :body-style="cardStyle"> -->
    <div class="chart-content" :style="{background:bgColor}">
        <div class="margin-bottom-small padding-small chart-title-box" >
            <h4 class="chart-title" :style="{textAlign:textAlign}"
                v-show="title">{{title}}</h4>
            <!-- <div class="dateTime"
                v-show="dateTime">{{dateTime}}</div> -->
        </div>
        <div class="echartContent"
        :style="{height:chartHeight}"
            v-loading="loading">
            <chart class="echarts"
                :style="{height:chartHeight}"
                :options="optionsData"
                v-if="optionsData"
                autoresize
                theme="light"></chart>
            <div class="echartsNoData"
                v-if="showNoData">暂无数据</div>
        </div>

    </div>
<!-- </bs-card> -->
</template>

<script>
    //echarts图表
    import ECharts from "vue-echarts";
    import "echarts/lib/chart/line";
    import "echarts/lib/chart/bar";
    import "echarts/lib/chart/pie";
    import "echarts/lib/chart/gauge";
    import "echarts/lib/component/tooltip";
    import "echarts/lib/component/legend";
    import "echarts/lib/component/title";
    import "echarts/lib/component/angleAxis";
    import "echarts/lib/component/radiusAxis";
    import "echarts/lib/component/polar";
    export default {
        components: { "chart": ECharts },
        props: {
            optionsData: {
                type: Object,
                default: null
            },
            title: {
                type: String,
                default: ''
            },
            textAlign: {
                type: String,
                default: 'left',
            },
            bgColor: {
                type: String,
                default: 'rgba(0,0,0,0)',
            },
            loading: {
                type: Boolean,
                default: false,
            },
            chartHeight: {
                type: String,
                default:''
            }
        },
        data() {
            return {
                cardStyle:{
                    padding:'16px'
                }
            };
        },
        watch: {},
        computed: {
            showNoData() {
                return !this.optionsData && !this.loading
            },
        },
        mounted() {},
        methods: {}
    };
</script>

<style lang='scss'
    scoped>
    .chart-content {
        position:relative;
        height: 100%;
        
        .echartsNoData,
        .echartLoading {
            width: 100%;
            height: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
            color: #fff;
            background: rgba(0,0,0,0);
            margin: 0 auto;
        }

        .echartLoading {
            position: absolute;
            top: 0;
            right: 0;
            left: 0;
        }

        .chart-title-box{
            position: absolute;
            width: 100%
        }

        .dateTime,
        .chart-title {
            line-height: 20px;
            height: 20px;
            color: #999;
            font-size: 12px;
        }

        .chart-title {
            font-size: 14px;
            color: #333;
        }

        .echartContent {
            width: 100%;
            height: 100%;
            position: relative;

            .echarts {
                height: 100%;
                width: 100%;
            }
        }
    }
</style>