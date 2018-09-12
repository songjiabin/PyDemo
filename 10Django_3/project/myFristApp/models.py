from django.db import models


# Create your models here.


# 班级表
class Grades(models.Model):
    # 定义字段 gname 班级名称
    # CharField 字符串类型的
    # max_length 最大长度是20
    gname = models.CharField(max_length=20, db_column='gname', null=False)

    # 班级成立时间
    # DateTimeField 时间类型
    gdate = models.DateTimeField(db_column='gdate', null=True)

    # 班级的女生数量
    # IntegerField数字类型
    ggirlnum = models.IntegerField()

    # 班级的男生数量
    # IntegerField数字类型
    gboynum = models.IntegerField()

    # 是否删除
    isDelete = models.BooleanField(default=False)

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

    pass


# 学生表
class Students(models.Model):
    # 学生的姓名
    sname = models.CharField(max_length=20, null=False)
    # 学生的性别
    sgender = models.BooleanField()
    # 学生的年龄
    sage = models.IntegerField()
    # 学生的简介
    scontent = models.CharField(max_length=20, null=True)
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
        db_table = "students"
        # 按照 id 进行升序
        # ordering =['-id'] 降序
        ordering = ['id']
        pass

    pass
