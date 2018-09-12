from django.shortcuts import render

# Create your views here.  视图

from django.http import HttpResponse

from .models import Student, Grades

from datetime import date


# request 请求体
def index(request):
    # return HttpResponse("hellow i'm new python stuedent ! ")
    return render(request, 'myFristDemo/index.html')
    pass


# 查出  学生表中 isDelete = False的数据  并交给 html文件展示并传递给流量器
def student(request):
    studentInfo = Student.studentManager.all()
    return render(request, 'myFristDemo/Students.html', {'studentInfo': studentInfo})
    pass


def gradesInfo(request):
    gradesInfo = Grades.objects.all()
    return render(request, 'myFristDemo/Grades.html', {'gradesInfo': gradesInfo})
    pass




# 添加学生 方式 1
def addstudent(request):
    grade = Grades.objects.get(pk=1)

    student = Student.createStudent('基本密码',
                                    True,
                                    25,
                                    "我是基本密码",
                                    grade,
                                    False,
                                    "2018-05-25",
                                    "2018-09-25")
    student.save()

    return HttpResponse('添加成功')
    pass


# 添加学生 方式 2  使用自定义管理器
def addstudent2(request):
    grade = Grades.objects.get(pk=1)

    student = Student.studentManager.createStudent('鸣人',
                                                   True,
                                                   25,
                                                   "我是鸣人",
                                                   grade,
                                                   False,
                                                   "2018-01-25",
                                                   "2018-02-22")
    student.save()

    return HttpResponse('添加成功')
    pass


# 得到所有的数据
def allStudents(request):
    allStudents = Student.studentManager.all()
    return render(request, 'myFristDemo/allStudents.html', {'allStudents': allStudents})
    pass


# 得到唯一的一个数据
def getOneStudent(request):
    oneStudent = Student.studentManager.get(id=2)
    return render(request, 'myFristDemo/getOneStudent.html', {'oneStudent': oneStudent})
    pass


# exact 相等
def getExactStudent(request):
    # 返回的是一个集合 不是一个数据
    # 如果filter()里面没有参数 表示为全查
    exactStudent = Student.studentManager.filter(id=5)

    # id_exact = 5  和 id = 5  是等价的
    exactStudent = Student.studentManager.filter(id__exact=3)

    return render(request, 'myFristDemo/exactStudent.html', {'exactStudent': exactStudent})
    pass


# 模糊查询
def containsStudent(request):
    # 查询 Student 中 sname 包含 基本 的所有数据
    containStudents = Student.studentManager.filter(sname__contains='基本')
    return render(request, 'myFristDemo/containStudents.html', {'containStudents': containStudents})
    pass


def StarwithOrendWith(request):
    # 查询 Student 中 基本开头的数据
    startWithOrEndWithStudents = Student.studentManager.filter(sname__startswith='基本')

    startWithOrEndWithStudents = Student.studentManager.filter(sname__endswith='人')
    return render(request, 'myFristDemo/startWithOrEndWithStudents.html',
                  {'startWithOrEndWithStudents': startWithOrEndWithStudents})
    pass


# 某些字段不为 null 数据
def notnullstudent(request):
    # 查询学生表中 name 不是空的所有数据
    notnullStudents = Student.studentManager.filter(sname__isnull=True)
    return render(request, 'myFristDemo/notnullstudent.html',
                  {'notnullStudents': notnullStudents})
    pass


# 范围内的查询
def wherestudent(request):
    # 查询 id  是 1 2 3  的数据
    whereStudent = Student.studentManager.filter(id__in=[1, 2, 3])
    return render(request, 'myFristDemo/whereStudent.html',
                  {'whereStudent': whereStudent})
    pass


# 比较 > = <
# gt、gte、lt、lte：大于、大于等于、小于、小于等于
def comparestudent(request):
    # 查询 id > = 3数据
    compareStudent = Student.studentManager.filter(id__gte=3)
    return render(request, 'myFristDemo/compareStudent.html',
                  {'compareStudent': compareStudent})
    pass


def datestudent(request):
    # 查询  年 是 2010 年的数据 (createTime字段中年 是 2010 年的数据)
    dateStudent = Student.studentManager.filter(createTime__year=2010)
    return render(request, 'myFristDemo/dateStudent.html',
                  {'dateStudent': dateStudent})
    pass


def afterDatestudent(request):
    # 查询 2010 10.1 后的数据
    # filter(bpub_date__gt = date(1980,1,1))
    dateStudent = Student.studentManager.filter(createTime__gt=date(2010, 10, 1))
    return render(request, 'myFristDemo/dateStudent.html',
                  {'dateStudent': dateStudent})
    pass


def rangeDatestudent(request):
    # 查询 2010 10.1 后的数据
    # filter(bpub_date__gt = date(1980,1,1))
    rangeStudent = Student.studentManager.filter(createTime__range=(date(2010, 9, 24), date(2018, 2, 23)))
    return render(request, 'myFristDemo/dateStudent.html',
                  {'dateStudent': rangeStudent})
    pass


def excludeStudent(request):
    # 查询 不包含 id = 2  的数据
    rangeStudent = Student.studentManager.exclude(id=2)
    return render(request, 'myFristDemo/dateStudent.html',
                  {'dateStudent': rangeStudent})
    pass


from django.db.models import F


# 每个学生中 age > id 的数据
# bread__gt = F('bcomment'))
def FStudent(request):
    # 每个学生中 age > id 的数据
    # dateStudent = Student.studentManager.filter(sage__gt = F('id'))

    # 每个学生中 aqe>id*2的数据
    dateStudent = Student.studentManager.filter(sage__gt=F('id') * 2)
    return render(request, 'myFristDemo/dateStudent.html',
                  {'dateStudent': dateStudent})
    pass


# 查询 Student 中 age> 10 且 id> 4的数据


from django.db.models import Q


def QStudent(request):
    dateStudent = Student.studentManager.filter(((Q(id__gt=4) & Q(sage__gt=10))))
    return render(request, 'myFristDemo/dateStudent.html',
                  {'dateStudent': dateStudent})
    pass


# 排序  查询 Student 的信息 ，并按照 id 从小到大排序
def orderByStudent(request):
    # dateStudent = Student.studentManager.all().order_by("-id")
    # return render(request, 'myFristDemo/dateStudent.html',
    #               {'dateStudent': dateStudent})

    # 将 id > 3 的数据 。从大到小排序

    dateStudent = Student.studentManager.filter(id__gt=3).order_by("-id")
    return render(request, 'myFristDemo/dateStudent.html',
                  {'dateStudent': dateStudent})
    pass


from django.db.models import Sum, Count, Max, Min


# 查询所有学生的个数
def countStudent(request):
    dateStudent = Student.studentManager.all().aggregate(Count("id"))
    print(dateStudent)
    return HttpResponse(dateStudent.get('id__count'))
    pass

# 查询所有学生年龄的总和
def sumStudent(request):
    dateStudent = Student.studentManager.all().aggregate(Sum("sage"))
    print(dateStudent)
    return HttpResponse(dateStudent.get('sage__sum'))
    pass


def count2Student(request):
    dateStudent = Student.studentManager.all().count()
    print(dateStudent)
    return HttpResponse(str(dateStudent))
    pass


def existsStudent(request):
    dateStudent = Student.studentManager.all().exists()
    print(dateStudent)
    return HttpResponse(dateStudent)
    pass


# 查询学生表中  名字 为 基本密码 的学生 班级信息
def getGradesOfNames(request):
    gradesInfo  = Grades.objects.filter(student__sname__contains= ('基本密码'))
    return render(request, 'myFristDemo/Grades.html', {'gradesInfo': gradesInfo})
    pass


# 查询 班级表中名字 为'班级1'的班级中所有的学生信息
def getGradesOfAllStudent(request):
    dateStudent= Student.studentManager.filter(sGrades__gname='班级1')
    return render(request, 'myFristDemo/dateStudent.html',
                  {'dateStudent': dateStudent})
    pass