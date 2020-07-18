from django.shortcuts import redirect
from django.http import HttpResponseRedirect


def login(func):
    def login_fun(request, *args, **kwargs):
        if request.session.has_key('username'):
            return func(request, *args, **kwargs)

        else:
            red = HttpResponseRedirect('/login/')
            red.set_cookie('url', request.get_full_path())
            return red
    return login_fun