import json

from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets

# Create your views here.
from XingZhiServer import models
from XingZhiServer.models import Users, Projects, Labels, Tasks, TaskLabels
from XingZhiServer.serializers import UserSerializer, ProjectSerializer, LabelSerializer, TaskSerializer, \
    TaskLabelSerializer

'''
查询数据库中所有的用户
:param request
:return:
'''


class UserSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'userId'


'''
查询数据库中所有的项目
:param request
:return:
'''


class ProjectSet(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'projectId'


'''
查询数据库中所有的标签
:param request
:return:
'''


class LabelSet(viewsets.ModelViewSet):
    queryset = Labels.objects.all()
    serializer_class = LabelSerializer
    lookup_field = 'labelId'


'''
查询数据库中所有的任务
:param request
:return:
'''


class TaskSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'taskId'


'''
查询数据库中所有的任务标签关系
:param request
:return:
'''


class TaskLabelsSet(viewsets.ModelViewSet):
    queryset = TaskLabels.objects.all()
    serializer_class = TaskLabelSerializer
    lookup_field = 'taskLabelId'


@csrf_exempt
def register(request):
    if request.method == 'POST':
        # userId =request.POST.get('userId')#id无需创建
        email = request.POST.get('userEmail')  # 电子邮件
        name = request.POST.get('username')  # 用户名
        password = request.POST.get('userPassword')  # 密码
        phone = request.POST.get('userPhone')  # 电话
        identity = request.POST.get('userIdentity')  # 身份
        sex = request.POST.get('userSex')  # 性别
        avatar = request.FILES.get('userAvatar')  # 头像，通过127.0.0.1:8000/media/图片名访问头像
        signature = request.POST.get('userSignature')  # 个性签名

        user = models.Users.objects.create(username=name, userEmail=email,
                                           userPassword=password, userPhone=phone,
                                           userIdentity=identity, userSex=sex,
                                           userAvatar=avatar, userSignature=signature)
        user.save()
        resp = {'message': '注册成功', 'id': '0'}
        return HttpResponse(json.dumps(resp))
    else:
        resp = {'message': '用户已存在', 'id': '1'}
        return HttpResponse(json.dumps(resp))


@csrf_exempt
def login_email(request):
    if request.method == 'POST':
        email = request.POST.get('userEmail')  # 电子邮件
        password = request.POST.get('password')  # 密码
        # print(username,password)
        users = Users.objects.filter(userEmail=email, userPassword=password)
        # print(users)
        if users:
            resp = {'message': "登录成功", 'id': '1'}
            return HttpResponse(json.dumps(resp))
        else:
            resp = {'message': "登录失败", 'id': '0'}
            return HttpResponse(json.dumps(resp))


@csrf_exempt
def login(request):
    if request.method == 'POST':
        user = request.POST.get('userId')  # id
        password = request.POST.get('password')  # 密码
        # print(username,password)
        users = Users.objects.filter(userId=user, userPassword=password)
        # print(users)
        if users:
            resp = {'message': "登录成功", 'id': '1'}
            return HttpResponse(json.dumps(resp))
        else:
            resp = {'message': "登录失败", 'id': '0'}
            return HttpResponse(json.dumps(resp))


# @csrf_exempt
# def hqz(request):
#     user_id = request.GET.get('userId')
#     if request.method == 'POST':
#         avatar = request.FILES.get('avatar')  # 头像，通过39.105.110.19/media/media/图片名访问头像
#         user = models.Users.objects.create(Image=avatar)
#         user.save()
#
#         return HttpResponse('上传成功')
#     else:
#         return HttpResponse('上传失败')


@csrf_exempt
def user_task(request):
    user_id = request.GET.get('userId')
    if request.method == 'POST':
        tasks = Tasks.objects.filter(userId=user_id)
        tasks_result = []
        if tasks:
            for i in tasks:
                resp = {'taskId': i.taskId, 'taskTitles': i.taskTitles,
                        'taskComment': i.taskComment, 'taskDueDate': i.taskDueDate,
                        'taskPriority': i.taskPriority, 'taskProjectId': i.taskProjectId,
                        'taskUserId': user_id, 'taskStatus': i.taskStatus}
                tasks_result.append(resp)
                return HttpResponse(json.dumps(tasks_result))
            else:
                resp = {'taskId': '查询无结果', 'id': '0'}
                return HttpResponse(json.dumps(resp))


@csrf_exempt
def user_project(request):
    user_id = request.GET.get('userId')
    if request.method == 'POST':
        projects = Projects.objects.filter(userId=user_id)
        projects_result = []
        if projects:
            for i in projects:
                resp = {'projectsId': i.taskUserId, 'projectName': i.projectName,
                        'projectColorName': i.projectColorName,
                        'projectColorCode': i.projectColorCode, 'projectUser': user_id
                        }
                projects_result.append(resp)
                return HttpResponse(json.dumps(projects_result))
            else:
                resp = {'projectsId': '查询无结果','id': '0'}
                return HttpResponse(json.dumps(resp))


@csrf_exempt
def user_label(request):
    user_id = request.GET.get('userId')
    if request.method == 'POST':
        labels = Labels.objects.filter(userId=user_id)
        labels_result = []
        if labels:
            for i in labels:
                resp = {'labelId': i.labelId, 'labelName': i.labelName,
                        'labelColorName': i.labelColorName,
                        'labelColorCode': i.labelColorCode, 'labelUser': user_id
                        }
                labels_result.append(resp)
                return HttpResponse(json.dumps(labels_result))
            else:
                resp = {'projectsId': '查询无结果','id': '0'}
                return HttpResponse(json.dumps(resp))


@csrf_exempt
def task_label(request):
    task_id = request.GET.get('taskId')
    if request.method == 'POST':
        labels = TaskLabels.objects.filter(taskId=task_id)
        labels_result = []
        if labels:
            for i in labels:
                resp = {'taskLabelId': i.taskLabelId,
                        'taskId': task_id,
                        'labelId': i.labelId
                        }
                labels_result.append(resp)
                return HttpResponse(json.dumps(labels_result))
            else:
                resp = {'taskLabelId': '查询无结果','id': '0'}
                return HttpResponse(json.dumps(resp))


@csrf_exempt
def label_task(request):
    label_id = request.GET.get('labelId')
    if request.method == 'POST':
        tasks = TaskLabels.objects.filter(labelId=label_id)
        tasks_result = []
        if tasks:
            for i in tasks:
                resp = {'taskLabelId': i.taskLabelId,
                        'taskId': i.taskId,
                        'labelId': label_id
                        }
                tasks_result.append(resp)
                return HttpResponse(json.dumps(tasks_result))
            else:
                resp = {'taskLabelId': '查询无结果','id': '0'}
                return HttpResponse(json.dumps(resp))

@csrf_exempt
def add_project(request):
    if request.method == 'POST':
        user = request.POST.get('userId')  # 用户id
        project_name =request.POST.get('projectName')
        project_colorname =request.POST.get('projectColorName')
        project_colorcode =request.POST.get('projectColorCode')
        project = models.Projects.objects.create(projectName=project_name,
                                                 project_colorname=project_colorname,
                                                 projectColorCode=project_colorcode,
                                                 projectUser=user)
        project.save()
        resp = {'message': '添加项目成功', 'id': '0'}
        return HttpResponse(json.dumps(resp))
    else:
        resp = {'message': '添加项目失败', 'id': '1'}
        return HttpResponse(json.dumps(resp))
