from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


# request 请求体
def index(request):
    return HttpResponse("我是基本密码")
    pass


# 当url中有数字的时候进行匹配
def details(request, num1, num2):
    return HttpResponse("匹配到两个数字%s和%s" % (num1, num2))
    pass


from .models import Grades, Student


# 视图： grades 班级的视图
def grades(request):
    # 去 models 中 取数据 也就是刚才创建表的那个 models中
    # 得到grades中所有的数据
    gradesList = Grades.objects.all()
    # 将数据传给 模板   模板渲染好后再传给浏览器
    return render(request, 'myFristApp/Grades.html', {'grades': gradesList})
    pass


# 视图： grades 学生的视图
def student(request):
    # 去 models  中 取数据 也就是刚才创建表的那个 models中
    # 得到 student 中所有的数据
    studentList = Student.objects.all()
    # 将数据传给 模板   模板渲染好后再传给浏览器
    return render(request, 'myFristApp/Student.html', {'student': studentList})
    pass


# 视图 当点开班级 查看班级详情
# num 为班级的id 根据班级的id  取出 班级内的学生信息
def gradesStudent(request, num):
    print(num)

    # 从班级表中找到 id=num的班级信息
    gradesInfo = Grades.objects.get(pk=num)
    # 从这个班级中得到下面所有的学生
    studentInfo = gradesInfo.student_set.all()
    return render(request, 'myFristApp/GradesStudent.html', {'studentInfo': studentInfo})
    pass
