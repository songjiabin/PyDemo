from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, 'myFristApp/index.html')
    pass


from django.http import HttpResponse


# cookies 测试
def cookietest(request):
    # 返回的参数
    response = HttpResponse()

    # 设置cookies  当下次请求的时候 给带过来
    # response.set_cookie('cook', 'i am cook')

    # 得到cookies
    cookies = request.COOKIES
    # 返回给浏览器
    response.write('<h1>' + cookies['cook'] + '<h1/>')

    return response

    pass


from django.http import HttpResponseRedirect
from django.shortcuts import redirect


# 重定向
def redirect1(request):
    # HttpResponseRedirect 和 redirect 功能是一样的，
    # return HttpResponseRedirect("/redirect2")
    return redirect("/redirect2")


def redirect2(request):
    return HttpResponse("我是重定向后的界面")


# main 界面

def main(request):
    return render(request, 'myFristApp/main.html')
    pass


# login 界面

def login(request):
    return render(request, 'myFristApp/login.html')
    pass


# 登录完成后 重定向到  main界面上去

def loginRedirect(request):
    return redirect('/main')
    pass
