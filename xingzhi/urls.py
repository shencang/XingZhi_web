"""xingzhi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import include
from django.views.static import serve

from XingZhiServer import views
from xingzhi import settings

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'', include('XingZhiServer.urls', namespace='XingZhiServer')),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'loginE/$', views.login_email),  # 邮箱登录
    url(r'login/$', views.login),
    url(r'register/$', views.register),
    url(r'findProject/$', views.user_project),
    url(r'findLabel/$', views.user_label),
    url(r'findTask/$', views.user_task),
    url(r'findTaskLabels/$', views.task_label),
    url(r'findTaskLabels/$', views.label_task),
    url(r'addtask/',views.add_task),
    url(r'addrelation/$',views.add_relation_task_label),
    url(r'addlabel/$',views.add_label),
    url(r'addproject/$',views.add_project),

]
