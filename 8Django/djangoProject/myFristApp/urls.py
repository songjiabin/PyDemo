from django.conf.urls import url, include
from .views import index, details, grades, student, gradesStudent

urlpatterns = [

    # 当主页匹配到 什么地址也没有的时候  显示的是 index 界面
    url(r'^$', index),

    # 匹配 ../../数字/数字 格式的 url
    url(r'^(\d+)/(\d+)$', details),

    # 匹配班级的 页面 ../../grades  grades 是视图中
    url(r'^grades/$', view=grades),

    # 匹配学生的 页面 ../../Student
    url(r'^student/$', view=student),

    # 匹配 ../../grades/1  当点击班级查看班级详情
    url(r'^grades/(\d+)$', view=gradesStudent)
]
