from django.conf.urls import url, include
from .views import index, student, addstudent, addstudent2, allStudents
from .views import getOneStudent, getExactStudent, containsStudent, StarwithOrendWith
from .views import notnullstudent, wherestudent, comparestudent, datestudent, afterDatestudent
from .views import rangeDatestudent, excludeStudent, FStudent, QStudent ,orderByStudent,countStudent
from .views import sumStudent ,count2Student,existsStudent
from .views import gradesInfo , getGradesOfNames ,getGradesOfAllStudent

urlpatterns = [
    url(r'^$', view=index),

    # 匹配学生的 页面 ../../Student
    url(r'^student/$', view=student),

    # 匹配添加学生的 页面 ../../addstudent
    url(r'^addstudent/$', view=addstudent),

    # 匹配添加学生的 页面 ../../addstudent2
    url(r'^addstudent2/$', view=addstudent2),

    #################################################

    # 匹配所有的数据 没有任何的条件限制  类似于 select * from student
    url(r'^allStudents/$', view=allStudents),

    # 匹配表中唯一的一个数据
    url(r'^getOneStudent/$', view=getOneStudent),

    # 判等 exact。
    url(r'^exactStudent/$', view=getExactStudent),

    # contains 查询 模糊查询
    url(r'^contains/$', view=containsStudent),

    # starwiths 以什么开头   endwiths 以什么结尾
    url(r'^StarwithOrendWith/$', view=StarwithOrendWith),

    # 查询  某 sname 不为空的数据
    url(r'^notnullstudent/$', view=notnullstudent),

    # 查询  在什么范围之内的数据
    url(r'^wherestudent/$', view=wherestudent),

    # 查询   比较 > < =
    url(r'^comparestudent/$', view=comparestudent),

    # 查询   日期查询
    url(r'^datestudent/$', view=datestudent),

    # 查询   某个日期后的数据
    url(r'^afterDatestudent/$', view=afterDatestudent),

    # 查询   某个日期范围内的数据
    url(r'^rangeDatestudent/$', view=rangeDatestudent),

    # 查询   某个日期范围内的数据
    url(r'^excludeStudent/$', view=excludeStudent),

    # 查询 学生信息中 age>id 的数据
    # 每个学生中 age > id 的数据
    url(r'^FStudent/$', view=FStudent),

    # 查询 Student 中 age> 10 且 id> 4的数据
    url(r'^QStudent/$', view=QStudent),

    # 查询 Student 的信息 ，并按照 id 从小到大排序
    url(r'^orderByStudent/$', view=orderByStudent),


    # 查询 Student 的个数
    url(r'^countStudent/$',view=countStudent),

    # 查询 Student 的 总和
    url(r'^sumStudent/$', view=sumStudent),

    # count的使用
    url(r'^count2Student',view=count2Student),

    # 判断是否有数据
    url(r'^existsStudent',view=existsStudent),


    # 所有班级的信息
    url(r'^gradesInfo',view=gradesInfo),

    # 查询学生表中 学生 名字为 基本密码 的班级信息
    url(r'^getGradesOfNames',view=getGradesOfNames),


    # 查询 班级表中  gname ='班级1' 所有的学生信息
    url(r'^getGradesOfAllStudent',view=getGradesOfAllStudent)
]
