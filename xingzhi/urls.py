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
    ################################################################
    # 管理员和其他
    url('admin/', admin.site.urls),
    url(r'', include('XingZhiServer.urls', namespace='XingZhiServer')),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    ################################################################
    # 用户登录注册方法
    url(r'loginE/$', views.login_email),  # 邮箱登录
    url(r'login/$', views.login),
    url(r'register/$', views.register),
    ################################################################
    # 增加方法
    url(r'addTask/', views.add_task),
    url(r'addRelation/$', views.add_relation_task_label),
    url(r'addLabel/$', views.add_label),
    url(r'addProject/$', views.add_project),
    ################################################################
    # 删除方法
    url(r'deleteProject/$', views.delete_project),
    url(r'deleteTask/$', views.delete_task),
    ################################################################
    # 修改方法
    url(r'updateUser/$', views.update_user),
    url(r'updateTaskStatus/$', views.update_task_status),
    url(r'updateTask/$', views.update_task),
    ################################################################
    # 查找方法
    url(r'findProject/$', views.user_project),
    url(r'findLabel/$', views.user_label),
    url(r'findTask/$', views.user_task),
    url(r'findTaskLabel/$', views.task_label),
    url(r'findLabelTask/$', views.label_task),
    url(r'getTaskByProject/$', views.get_tasks_by_project),
    url(r'getTaskByLabel/$', views.get_tasks_by_label),
    ################################################################
    # 新追加。暂不分类
    url(r'getUserInfo/$', views.get_user_info),
    url(r'updatePassword/$', views.update_password),
    url(r'findEmailRepeat/$', views.find_email_repeat),

]
