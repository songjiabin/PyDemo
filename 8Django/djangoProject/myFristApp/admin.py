from django.contrib import admin

# Register your models here.

# 引入建立的 魔板 也就是 表
from .models import Grades, Student


# 创建班级的时候默认加两个学生
class StudentInfo(admin.TabularInline):
    model = Student
    extra = 2
    pass


# 自定义 网页显示的样式
@admin.register(Grades)
class GradesAdmin(admin.ModelAdmin):
    #  创建班级的时候默认加两个学生
    inlines = [StudentInfo]

    # 列表页属性
    # 显示字段 列表中的字段 想显示啥 写啥
    list_display = ['pk', 'gname', 'gdate', 'ggirlnum', 'gboynum', 'isDelete']
    # 过滤器 过滤的字段
    list_filter = ['gname']
    # 搜索的条件
    search_fields = ['gname']
    # 添加分页 每5条分一页
    list_per_page = 5

    # 添加 修改属性 是 另一个界面
    # 规定属性的先后顺序
    # fields = ['gdate', 'ggirlnum', 'gboynum', 'isDelete', 'gname']

    # 添加分组   fields和 fieldsets 不能同时使用
    fieldsets = [
        # num 为 一组
        ('num', {"fields": ['gdate', 'ggirlnum', 'gname']}),
        # other 为 一组
        ('other', {"fields": ['gboynum', 'isDelete']})
    ]

    pass

@admin.register(Student)
class StudentAdmain(admin.ModelAdmin):

    # 修改默认内容
    def gender(self):
        if self.sgender:
            return '男'
        else:
            return '女'
        pass

    # 设置页面列的表名称
    gender.short_description = '性别'

    # 列表页属性

    # 显示字段 列表中的字段 想显示啥 写啥
    list_display = ['pk', 'sname', gender, 'sage', 'scontent', 'sGrades', 'isDelete']
    # 过滤器 过滤的字段
    list_filter = ['scontent']
    # 搜索的条件
    search_fields = ['scontent']
    # 添加分页 每5条分一页
    list_per_page = 5

    # 添加 修改属性 是 另一个界面
    # 规定属性的先后顺序
    # fields = ['gdate', 'ggirlnum', 'gboynum', 'isDelete', 'gname']

    # 添加分组   fields和 fieldsets 不能同时使用
    fieldsets = [
        # num 为 一组
        ('num', {"fields": ['sname', 'sGrades', 'sage', 'isDelete']}),
        # other 为 一组
        ('other', {"fields": ['sgender', 'scontent']})
    ]

    pass


# 注册 班级表
# admin.site.register(Grades, GradesAdmin) 可以使用装饰器来进行注册

# 注册 学生表
# admin.site.register(Student, StudentAdmain) 可以使用装饰器来进行注册
