### 三酷猫 

目录结构
```
ThreeCoolCat
|----home 新闻、日志、友情链接
|
|----portal vue前端打包生成的网站前端程序
|
|----school 学校、教师、课程
|
|----shop 图书、视频
|
|----static 静态资源文件
|
|----static_dev manage.py collectstatic结果文件，用于部署
|
|----templates 全局模板文件
|
|----ThreeCoolCat Django项目配置文件
|
|----vali django-admin-theme-vali皮肤插件，重写了默认的admin模板
```
运行方式
- 事先装好python解释器，版本要求为>=3.6或
- 安装 python包依赖，进入ThreeCoolCat目录，并执行：
```bash
pip install -r requirements.txt
```
- 修改 ThreeCoolcat/settings.py 中的数据库连接，并确认目标数据库存在
并执行：
```
python manage.py migrate
```
- 起动程序
```
python manage.py runserver
```
- 访问本地地址 http://localhost:8000/ 