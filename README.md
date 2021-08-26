# TutorialManagement

## 介绍
学生课业帮扶系统

## 软件架构
Python3/Django

## Teacher - 教师数据表

|字段|类型|必须|备注|
|---|---|---|---|
|ID*|int|Y|工号|
|Name|char|Y|姓名|
|Phone|char|N|手机|
|Email|char|N|邮箱|

## Course - 教师管理的课程
|字段|类型|必须|备注|
|---|---|---|---|
|ID*|int|Y|索引|
|Teacher|foreign|Y|教师|
|Name|char|Y|课程名称|
|Term|char|Y|学期|
|Limit|int|N|人数限制|

## Tutorial - 已发布的辅导
|字段|类型|必须|备注|
|---|---|---|---|
|ID*|int|Y|索引|
|Course|foreign|Y|课程|
|Teacher|foreign|Y|教师|
|StartTime|char|Y|开始时间|
|EndTime|char|Y|结束时间|
|Place|char|Y|地点|
|JoinedNum|int|Y|已加入人数|

## Student - 学生数据表
|字段|类型|必须|备注|
|---|---|---|---|
|ID*|int|Y|学号|
|Name|char|Y|姓名|
|Phone|char|Y|手机|
|Email|char|N|邮箱|
|AppendCourse|foreign|N|已参加课程|

## AppendCourse - 学生参加的课程
|字段|类型|必须|备注|
|---|---|---|---|
|ID*|int|Y|索引|
|Teacher|foreign|Y|教师|
|Course|foreign|Y|课程|

## JoinedTutorial - 已参加的辅导
|字段|类型|必须|备注|
|---|---|---|---|
|ID*|int|Y|索引|
|Student|foreign|Y|学生|
|Tutorial|foreign|Y|辅导|

## 启动项目
1.  git clone
2.  python3 manage.py runserver

## 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request
