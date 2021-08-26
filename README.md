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
|Teacher|foreign|Y|教师安装教程


## 启动项目
1.  git clone
2.  python3 manage.py runserver

## 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request
