# coding=utf-8
from django.shortcuts import render, redirect
from django.http import *
import login_decorator
from models import *
from django.core.paginator import *
from django.core.files import File
from io import BytesIO
import time
import qrcode
from django.core.mail import send_mail, send_mass_mail, EmailMultiAlternatives
from email.header import make_header
import json


def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request,  'about.html')

def temporary_origin(request):
        return render(request, 'temporary_visitor.html')

@login_decorator.login
def console_index(request):
    return render(request, 'console_index.html')


def logout(request):
    request.session.flush()
    return redirect('/')


def login(request):
    return render(request, 'login.html')

def message_handle(request):
    post = request.POST
    phone = post.get('Phone')
    email = post.get('Email')
    name = post.get('Name')
    message = post.get('Message')
    fja = '%s, %s, %s       %s' % (name, phone, email, message)
    ret = send_mail('Message',fja , '2479759633@qq.com',
                ['1516412031@qq.com'], fail_silently=False)
    if ret:
        return HttpResponse(1)
    else:
        return HttpResponse('error')


def visit_handle(request):
    post = request.POST
    name = post.get('Name')
    phone = post.get('Phone')
    email = post.get('Email')
    code = str(post.get('Code'))
    if code == '1122':
        key = str(int(time.time()))
        qr = qrcode.QRCode(
            version=1,  # 二维码的格子矩阵大小
            error_correction=qrcode.constants.ERROR_CORRECT_Q,
            box_size=10,
            border=4,
        )

        qr.add_data(key)  # 向二维码添加数据
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")  # 更改QR的背景和绘画颜色
        img.save('/root/face/face_manage/face/QR.jpg')

        # email part
        subject = 'QR Code'
        text_content = '您的访问二维码'
        html_content = '<p>请保存<strong>附件</strong>里的二维码</p>'
        msg = EmailMultiAlternatives(subject, text_content, '2479759633@qq.com', [email])
        msg.attach_alternative(html_content, "text/html")
        # 发送附件
        text = open('/root/face/face_manage/face/QR.jpg', 'rb').read()
        file_name = 'QR.jpg'
        # 对文件进行编码处理
        b = make_header([(file_name, 'utf-8')]).encode('utf-8')
        msg.attach(b, text)
        # msg.attach_file(file_path)
        ret = msg.send()
        if ret:
            tt = temporary()
            tt.tname = name
            tt.tphone = phone
            tt.temail = email
            tt.tkey = key
            tt.is_delete = False
            tt.save()
            return HttpResponse(1)
        else:
            return HttpResponse(2)
    else:
        return HttpResponse(3)

def login_handle(request):
    post = request.POST
    uname = post.get('username')
    upwd = post.get('pwd')
    # print(upwd)
    # print(uname)
    if uname == 'whx':
        if upwd == '123':
            url = request.COOKIES.get('url', '/')
            red = HttpResponseRedirect(url)
            request.session['username'] = uname
            request.session.set_expiry(0)
            return red
        else:
            context = {'error_name': 0, 'error_pwd': 1, 'uname': uname, 'upwd': upwd}
            return render(request, 'login.html', context)
    else:
        context = {'error_name': 1, 'error_pwd': 0, 'uname': uname, 'upwd': upwd}
        return render(request, 'login.html', context)


@login_decorator.login
def dangerous_list(request, pindex):
    dangerous_info_list = visitor_info.objects.filter(vtemp__gt=37.3).order_by('-vtime')
    paginator = Paginator(dangerous_info_list, 20)
    page = paginator.page(pindex)
    context = {'page': page, 'paginator': paginator}

    return render(request, 'dangerous_list.html', context)


@login_decorator.login
def user_list(request, pindex):
    user_info_list = user_info.objects.filter(is_delete=False)
    paginator = Paginator(user_info_list, 20)
    page = paginator.page(pindex)
    context = {'page': page, 'paginator': paginator}
    return render(request, 'user_list.html', context)


@login_decorator.login
def visitor_list(request, pindex):
    visitor_info_list = visitor_info.objects.all().order_by('-vtime')
    paginator = Paginator(visitor_info_list, 20)
    page = paginator.page(pindex)
    context = {'page': page, 'paginator': paginator}

    return render(request, 'visitor_list.html', context)


def detail(request, uid):
    user = user_info.objects.get(pk=int(uid))
    visit_list = user.visitor_info_set.all().order_by('-vtime')
    context = {'user': user, 'visit_list': visit_list}
    return render(request, 'detail_info.html', context)


def upload_img(request):
    '''
    item = request.FILES.get('img')
    with open(str("/home/whx/" + item.name), 'wb') as f:
        for c in item.chunks():
            f.write(c)
    '''
    post = request.POST
    user = user_info()
    user.uname = post.get('uname')
    user.uphone = post.get('uphone')
    user.is_delete = False
    user.face_image = request.FILES.get('img')
    user.save()
    return HttpResponse('ok')
