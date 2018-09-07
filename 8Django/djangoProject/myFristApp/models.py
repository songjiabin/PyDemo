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

    def __str__(self):
       return self.gname


# 学生的模型 对应数据库中的student
class Student(models.Model):
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

    pass
