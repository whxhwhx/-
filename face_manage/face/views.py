from django.shortcuts import render, redirect
from django.http import *
import login_decorator
from models import *
from django.core.paginator import *
from django.core.files import File
from io import BytesIO


def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request,  'about.html')


@login_decorator.login
def console_index(request):
    return render(request, 'console_index.html')


def logout(request):
    request.session.flush()
    return redirect('/')


def login(request):
    return render(request, 'login.html')


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
def dangerous_list(request):
    return render(request, 'dangerous_list.html')


@login_decorator.login
def user_list(request, pindex):
    user_info_list = user_info.objects.filter(is_delete=False)
    paginator = Paginator(user_info_list, 10)
    page = paginator.page(pindex)
    context = {'page': page, 'paginator': paginator}
    return render(request, 'user_list.html', context)


@login_decorator.login
def visitor_list(request):
    visitor_info_list = visitor_info.objects.all().order_by('-vtime')
    dangerous_list = visitor_info.objects.filter(vtemp__gt=37.3).order_by('-vtime')

    context = {'list': visitor_info_list, 'dlist': dangerous_list}
    return render(request, 'visitor_list.html', context)


def detail(request, uid):
    print('uid = ', uid)
    user = user_info.objects.get(pk=int(uid))
    print(user)
    visit_list = user.visitor_info_set.all()
    context = {'user': user, 'visit_list': visit_list}
    print(visit_list)
    return render(request, 'detail.html', context)


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
