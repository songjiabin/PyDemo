from django.db import models


# Create your models here.


# 班级的模型 对应数据库中的 grades 表
class Grades(models.Model):
    # 定义字段 gname 班级名称
    # CharField 字符串类型的
    # max_length 最大长度是20
    gname = models.CharField(max_length=20)

    # 班级成立时间
    # DateTimeField 时间类型
    gdate = models.DateTimeField()

    # 班级的女生数量
    # IntegerField数字类型
    ggirlnum = models.IntegerField()

    # 班级的男生数量
    # IntegerField数字类型
    gboynum = models.IntegerField()

    # 是否删除
    isDelete = models.BooleanField()

    # 更改本表后 记录所有的 最后的一次时间
    lastTime = models.DateTimeField(auto_now=True)

    # 自动生成创建时间
    createTime = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.gname

    class Meta:
        # 数据库中的表 名字是 grades
        db_table = "grades"
        ordering = ['id']
        pass


# 学生模型管理器
class StudentManager(models.Manager):
    def get_queryset(self):
        return super(StudentManager, self).get_queryset().filter(isDelete=False)

    # 创建学生的对象
    def createStudent(self, name, gender, age, content,
                      grade, isDelete, lastTime, createTime):
        # 返回的事当前调用的对象
        student = self.model()
        student.sname = name
        student.sgender = gender
        student.sage = age
        student.scontent = content
        student.sGrades = grade
        student.isDelete = isDelete
        student.lastTime = lastTime
        student.createTime = createTime
        return student
        pass

    pass


# 学生的模型 对应数据库中的student
class Student(models.Model):
    # 生成自定义模型管理器
    # studentManager = models.Manager()

    studentManager = StudentManager()

    # 学生的姓名
    sname = models.CharField(max_length=20)
    # 学生的性别
    sgender = models.BooleanField()
    # 学生的年龄
    sage = models.IntegerField()
    # 学生的简介
    scontent = models.CharField(max_length=20)
    # 学生属于哪个班级  用外键关联
    sGrades = models.ForeignKey("Grades")
    # 是否删除
    isDelete = models.BooleanField(default=False)

    # 更改本表后 记录所有的 最后的一次时间
    lastTime = models.DateTimeField(auto_now=True)

    # 自动生成创建时间
    createTime = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.sname

    class Meta:
        # 数据库中的表 名字是 grades
        db_table = "student"
        # 按照 id 进行升序
        # ordering =['-id'] 降序
        ordering = ['id']
        pass

    # 定义类方法
    @classmethod
    def createStudent(cls, name, gender, age, content,
                      grade, isDelete, lastTime, createTime):
        # 新建学生 并 返回
        newStudent = cls(sname=name,
                         sgender=gender,
                         sage=age,
                         scontent=content,
                         sGrades=grade,
                         isDelete=isDelete,
                         lastTime=lastTime,
                         createTime=createTime)
        return newStudent
        pass

    pass
