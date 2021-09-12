# TutorialManagement

## 介绍
##### 学生课业帮扶系统

- 教师端
  - 可以导入课程和学生列表
  - 根据课程发起群体辅导邀约，可以看到接受邀约的学生列表和具体信息
  - 可以看到教师帮扶的人数，以及每门课帮扶的人数
  - （待完成）可以接受学生单独邀约

- 学生端
  - 可以看到参加课程的群体辅导邀约，并决定是否确认
  - （待完成）可以对某课程单独向教师发起单独辅导邀约



## 软件架构
##### 前端 Vue3 / Vue-Cli / VueX / Vue-Router

##### 后端 Django / Rest Framework

##### 数据库mysql



## 数据库模型

### BaseModel - 基类
|字段|类型|必须|备注|
|---|---|---|---|
|CreatTime|date|N|创建时间|
|UpdateTime|date|N|修改时间|
|IsDelete|bool|N|删除标记|

### Teacher - 教师数据表
|字段|类型|必须|备注|
|---|---|---|---|
|ID*|int|Y|索引|
|UID|int|Y|工号|
|Name|char|Y|姓名|
|Avatar|img|N|头像|
|WechatID|char|N|微信标识|
|Phone|char|N|手机|
|Email|char|N|邮箱|
|Location|char|N|工作地点|

### Course - 教师管理的课程
|字段|类型|必须|备注|
|---|---|---|---|
|ID*|int|Y|索引|
|Teacher|foreign|Y|教师|
|Name|char|Y|课程名称|
|Wallpaper|img|N|背景|
|Describe|char|N|描述|
|Term|char|Y|学期|
|Limit|int|N|人数限制|

### Tutorial - 已发布的辅导
|字段|类型|必须|备注|
|---|---|---|---|
|ID*|int|Y|索引|
|Course|foreign|Y|课程|
|Teacher|foreign|Y|教师|
|Describe|char|Y|备注|
|StartTime|char|Y|开始时间|
|EndTime|char|Y|结束时间|
|Place|char|Y|地点|
|JoinedNum|int|Y|已加入人数|
|- IsDone|bool|Y|是否完成|

### Student - 学生数据表
|字段|类型|必须|备注|
|---|---|---|---|
|ID*|int|Y|索引|
|UID|int|Y|学号|
|Name|char|Y|姓名|
|Avatar|img|N|头像|
|WechatID|char|N|微信标识|
|Phone|char|Y|手机|
|Email|char|N|邮箱|

### AppendCourse - 学生参加的课程
|字段|类型|必须|备注|
|---|---|---|---|
|ID*|int|Y|索引|
|Teacher|foreign|Y|教师|
|Course|foreign|Y|课程|

### JoinedTutorial - 已参加的辅导
|字段|类型|必须|备注|
|---|---|---|---|
|ID*|int|Y|索引|
|Student|foreign|Y|学生|
|Tutorial|foreign|Y|辅导|
|- IsDone|bool|Y|是否完成|

### （待完成）TutorialQuest - 已发起的辅导请求
|字段|类型|必须|备注|
|---|---|---|---|
|ID*|int|Y|索引|
|Student|foreign|Y|学生|
|Course|foreign|Y|课程|
|Teacher|foreign|Y|教师|
|Describe|char|N|备注|
|ExpectTime|char|Y|期望时间|
|ConfirmTime|char|Y|确认时间|
|ExpectPlace|char|Y|期望地点|
|ConfirmPlace|char|Y|确认地点|

## 启动项目
1.  git clone
2.  python3 manage.py runserver

## 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request
