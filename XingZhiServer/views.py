import json

from django.contrib import auth
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets

# Create your views here.
from XingZhiServer import models
from XingZhiServer.models import Users, Projects, Labels, Tasks, TaskLabels
from XingZhiServer.serializers import UserSerializer, ProjectSerializer, LabelSerializer, TaskSerializer, \
    TaskLabelSerializer
from xingzhi import settings

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
        print(email, password)
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


@csrf_exempt
def user_task(request):
    if request.method == 'POST':
        user_id = request.POST.get('userId')
        tasks = Tasks.objects.filter(taskUserId=user_id)
        tasks_result = []
        if tasks:
            for i in tasks:
                resp = {'taskId': i.taskId, 'taskTitles': i.taskTitles,
                        'taskComment': i.taskComment, 'taskDueDate': i.taskDueDate,
                        'taskPriority': i.taskPriority, 'taskProjectId': i.taskProjectId.projectId,
                        'taskUserId': user_id, 'taskStatus': i.taskStatus}
                tasks_result.append(resp)
            print(tasks_result)
            return HttpResponse(json.dumps(tasks_result))
        else:
            resp = {'taskId': '查询无结果', 'id': '1'}
            return HttpResponse(json.dumps(resp))


@csrf_exempt
def user_project(request):
    if request.method == 'POST':
        user_id = request.POST.get('userId')
        projects = Projects.objects.filter(projectUser=user_id)
        print(projects)
        projects_result = []
        if projects:
            for i in projects:
                resp = {'projectId': i.projectId, 'projectName': i.projectName,
                        'projectColorName': i.projectColorName,
                        'projectColorCode': i.projectColorCode, 'projectUser': user_id
                        }
                projects_result.append(resp)
            print(projects_result)
            return HttpResponse(json.dumps(projects_result))
        else:
            resp = {'projectsId': '查询无结果', 'id': '1'}
            return HttpResponse(json.dumps(resp))


@csrf_exempt
def user_label(request):
    if request.method == 'POST':
        user_id = request.POST.get('userId')
        labels = Labels.objects.filter(labelUser=user_id)
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
            resp = {'projectsId': '查询无结果', 'id': '1'}
            return HttpResponse(json.dumps(resp))


@csrf_exempt
def task_label(request):
    if request.method == 'POST':
        task_id = request.POST.get('taskId')
        labels = TaskLabels.objects.filter(taskId=task_id)
        print(labels)
        labels_result = []
        if labels:
            for i in labels:
                resp = {'taskLabelId': i.taskLabelId,
                        'taskId': task_id,
                        'labelId': i.labelId.labelId
                        }
                labels_result.append(resp)
            return HttpResponse(json.dumps(labels_result))
        else:
            resp = {'taskLabelId': '查询无结果', 'id': '1'}
            return HttpResponse(json.dumps(resp))


@csrf_exempt
def label_task(request):
    if request.method == 'POST':
        label_id = request.POST.get('labelId')
        tasks = TaskLabels.objects.filter(labelId=label_id)
        tasks_result = []
        if tasks:
            for i in tasks:
                resp = {'taskLabelId': i.taskLabelId,
                        'taskId': i.taskId.taskId,
                        'labelId': label_id
                        }
                tasks_result.append(resp)
            return HttpResponse(json.dumps(tasks_result))
        else:
            resp = {'taskLabelId': '查询无结果', 'id': '1'}
            return HttpResponse(json.dumps(resp))


@csrf_exempt
def add_project(request):
    if request.method == 'POST':
        user = request.POST.get('userId')  # 用户id
        user_f = Users.objects.get(userId=user)
        project_name = request.POST.get('projectName')
        project_colorname = request.POST.get('projectColorName')
        project_colorcode = request.POST.get('projectColorCode')
        project = models.Projects.objects.create(projectName=project_name,
                                                 projectColorName=project_colorname,
                                                 projectColorCode=project_colorcode,
                                                 projectUser=user_f)
        project.save()
        resp = {'message': '添加项目成功', 'id': '0'}
        return HttpResponse(json.dumps(resp))
    else:
        resp = {'message': '添加项目失败', 'id': '1'}
        return HttpResponse(json.dumps(resp))


@csrf_exempt
def add_label(request):
    if request.method == 'POST':
        user = int(request.POST.get('userId'))  # 用户id
        user_f = Users.objects.get(userId=user)
        label_name = request.POST.get('labelName')
        label_colorname = request.POST.get('labelColorName')
        label_colorcode = request.POST.get('labelColorCode')
        label = models.Labels.objects.create(labelName=label_name,
                                             labelColorName=label_colorname,
                                             labelColorCode=label_colorcode,
                                             labelUser=user_f)
        label.save()
        resp = {'message': '添加标签成功', 'id': '0'}
        return HttpResponse(json.dumps(resp))
    else:
        resp = {'message': '添加标签失败', 'id': '1'}
        return HttpResponse(json.dumps(resp))


@csrf_exempt
def add_task(request):
    if request.method == 'POST':
        user = request.POST.get('userId')  # 用户id
        user_f = Users.objects.get(userId=user)
        task_title = request.POST.get('taskTitle')
        task_comment = request.POST.get('taskComment')
        task_duedate = request.POST.get('taskDueDate')
        task_priority = request.POST.get('taskPriority')
        task_prjojectid = request.POST.get('taskProjectId')
        # task_user = request.POST.get('taskUserId')
        task_status = request.POST.get('taskStatus')
        task = models.Tasks.objects.create(
            taskTitle=task_title, taskComment=task_comment, task_DueDate=task_duedate,
            taskPriority=task_priority, taskPrjojectId=task_prjojectid, taskUserId=user_f,
            taskStatus=task_status)
        task.save()
        resp = {'message': '添加任务成功', 'id': '0'}
        return HttpResponse(json.dumps(resp))
    else:
        resp = {'message': '添加任务失败', 'id': '1'}
        return HttpResponse(json.dumps(resp))


@csrf_exempt
def add_relation_task_label(request):
    if request.method == 'POST':
        user = request.POST.get('userId')  # 用户id
        taskid = request.POST.get('taskId')
        labelid = request.POST.get('labelId')
        task = Tasks.objects.filter(taskId=taskid, taskUserId=user)
        label = Labels.objects.filter(labelId=labelid, labelUser=user)
        if task:
            if label:
                task = Tasks.objects.get(taskId=taskid)
                label = Labels.objects.get(labelId=labelid)
                task_label_add = models.TaskLabels.objects.create(
                    taskId=task, labelId=label)
                task_label_add.save()
                resp = {'message': '添加关系成功', 'id': '0'}
                return HttpResponse(json.dumps(resp))
            else:
                resp = {'message': '添加关系失败-不存在label', 'id': '2'}
                return HttpResponse(json.dumps(resp))
        else:
            resp = {'message': '添加关系失败-不存在task', 'id': '3'}
            return HttpResponse(json.dumps(resp))
    else:
        resp = {'message': '添加关系失败', 'id': '1'}
        return HttpResponse(json.dumps(resp))


@csrf_exempt
def update_user(request):
    if request.method == 'POST':
        result = []
        user_id = request.POST.get('userId')  # id无需创建
        email = request.POST.get('userEmail')  # 电子邮件
        name = request.POST.get('username')  # 用户名
        password = request.POST.get('userPassword')  # 密码
        phone = request.POST.get('userPhone')  # 电话
        identity = request.POST.get('userIdentity')  # 身份
        sex = request.POST.get('userSex')  # 性别
        avatar = request.FILES.get('userAvatar')  # 头像，通过127.0.0.1:8000/media/图片名访问头像
        signature = request.POST.get('userSignature')  # 个性签名

        if email:
            Users.objects.filter(userId=user_id).update(userEmail=email)
            result.append('email')
        if name:
            Users.objects.filter(userId=user_id).update(username=name)
            result.append('name')
        if password:
            Users.objects.filter(userId=user_id).update(userPassword=password)
            result.append('password')
        if phone:
            Users.objects.filter(userId=user_id).update(userPhone=phone)
            result.append('phone')
        if identity:
            Users.objects.filter(userId=user_id).update(userIdentity=identity)
            result.append('identity')
        if sex:
            Users.objects.filter(userId=user_id).update(userSex=sex)
            result.append('sex')
        if avatar:
            save_path = '{}/media/{}'.format(settings.MEDIA_ROOT, avatar.name)
            print(avatar)
            with open(save_path, 'wb+') as f:
                for content in avatar.chunks():  # pic.chunks文件内容
                    f.write(content)

            file = Users.objects.get(userId=user_id).userAvatar.save(avatar.name, avatar, save=True)
            print('file!')
            print(file)
            result.append('avatar')
        if signature:
            Users.objects.filter(userId=user_id).update(userSignature=signature)
            result.append('signature')

        if len(result) < 1:
            resp = {'message': '未修改数据', 'id': '2'}
        else:
            temp = '修改('
            for i in result:
                temp += i
                temp += ','
            temp += ')成功'
            resp = {'message': temp, 'id': '0'}

        return HttpResponse(json.dumps(resp))
    else:
        resp = {'message': '修改失败', 'id': '1'}
        return HttpResponse(json.dumps(resp))


@csrf_exempt
def delete_project(request):
    if request.method == 'POST':
        project_id = request.POST.get('projectId')
        Projects.objects.filter(projectId=project_id).delete()
        find = Projects.objects.filter(projectId=project_id)
        if find:
            resp = {'message': '删除失败', 'id': '1'}
        else:
            resp = {'message': '删除成功', 'id': '0'}
        return HttpResponse(json.dumps(resp))
    else:
        resp = {'message': '删除失败', 'id': '1'}
        return HttpResponse(json.dumps(resp))


# @csrf_exempt
# def update_project(request):
#


@csrf_exempt
def get_tasks_by_project(request):
    if request.method == 'POST':
        project_id = request.POST.get('projectId')
        task_status = request.POST.get('taskStatus')
        if task_status:
            tasks = Tasks.objects.filter(taskProjectId=project_id, taskStatus=task_status)
        else:
            tasks = Tasks.objects.filter(taskProjectId=project_id)
        print(tasks)
        tasks_result = []
        if tasks:
            for i in tasks:
                resp = {'taskId': i.taskId, 'taskTitles': i.taskTitles,
                        'taskComment': i.taskComment, 'taskDueDate': i.taskDueDate,
                        'taskPriority': i.taskPriority, 'taskProjectId': i.taskProjectId.projectId,
                        'taskUserId': i.taskUserId.userId, 'taskStatus': i.taskStatus}
                tasks_result.append(resp)
            return HttpResponse(json.dumps(tasks_result))
        else:
            resp = {'taskId': '查询无结果', 'id': '0'}
            return HttpResponse(json.dumps(resp))


@csrf_exempt
def update_task_status(request):
    if request.method == 'POST':
        task_id = request.POST.get('taskId')
        task_status = request.POST.get('taskStatus')
        if task_id:
            if task_status:
                Tasks.objects.filter(taskId=task_id).update(taskStatus=task_status)
                resp = {'message': '修改成功', 'id': '0'}
                return HttpResponse(json.dumps(resp))
            else:
                resp = {'message': '修改失败,请上传修改的状态参数', 'id': '1'}
                return HttpResponse(json.dumps(resp))
        else:
            resp = {'message': '修改失败，请确认修改id正确', 'id': '2'}
            return HttpResponse(json.dumps(resp))
    else:
        resp = {'message': '修改失败', 'id': '3'}
        return HttpResponse(json.dumps(resp))


@csrf_exempt
def delete_task(request):
    if request.method == 'POST':
        task_id = request.POST.get('taskId')
        Tasks.objects.filter(taskId=task_id).delete()
        find = Tasks.objects.filter(taskId=task_id)
        if find:
            resp = {'message': '删除失败', 'id': '1'}
        else:
            resp = {'message': '删除成功', 'id': '0'}
        return HttpResponse(json.dumps(resp))
    else:
        resp = {'message': '删除失败', 'id': '1'}
        return HttpResponse(json.dumps(resp))


@csrf_exempt
def get_tasks_by_label(request):
    if request.method == 'POST':
        user_id = request.POST.get('UserId')
        label_id = request.POST.get('labelId')

        task_status = request.POST.get('taskStatus')
        if task_status:
            task_labels = TaskLabels.objects.filter(labelId=label_id)
        else:
            task_labels = TaskLabels.objects.filter(labelId=label_id)
        print(task_labels)
        tasks_result_out = []
        if task_labels:
            for y in task_labels:
                print(y.taskId.taskId)
                print(type(y.taskId.taskId))
                task = Tasks.objects.get(taskId=y.taskId.taskId)
                resp = {'taskId': task.taskId, 'taskTitles': task.taskTitles,
                        'taskComment': task.taskComment, 'taskDueDate': task.taskDueDate,
                        'taskPriority': task.taskPriority, 'taskProjectId': task.taskProjectId.projectId,
                        'taskUserId': task.taskUserId.userId, 'taskStatus': task.taskStatus}
                tasks_result_out.append(resp)
            return HttpResponse(json.dumps(tasks_result_out))
        else:
            resp = {'taskId': '查询无结果', 'id': '0'}
            return HttpResponse(json.dumps(resp))


@csrf_exempt
def update_task(request):
    if request.method == 'POST':
        result = []
        task_id = request.POST.get('taskId')  # 任务ID
        task_titles = request.POST.get('taskTitles')  # 任务标题
        task_comment = request.POST.get('taskComment')  # 任务评论
        task_duedate = request.POST.get('taskDueDate')  # 任务截止时间
        task_priority = request.POST.get('taskProjectId')  # 任务优先级
        task_projectId = request.POST.get('userIdentity')  # 任务所属项目ID,外键
        task_userId = request.POST.get('taskUserId')  # 任务所属用户ID,外键
        task_status = request.POST.get('taskStatus')  # 任务状态

        if task_titles:
            Tasks.objects.filter(taskId=task_id).update(taskTitles=task_titles)
            result.append('titles')
        if task_comment:
            Tasks.objects.filter(taskId=task_id).update(taskComment=task_comment)
            result.append('comment')
        if task_duedate:
            Tasks.objects.filter(taskId=task_id).update(taskDueDate=task_duedate)
            result.append('duedate')
        if task_priority:
            Tasks.objects.filter(taskId=task_id).update(userPhone=task_priority)
            result.append('priority')
        if task_projectId:
            project = Projects.objects.get(projectUser=task_projectId)
            Tasks.objects.filter(taskId=task_id).update(userIdentity=project)
            result.append('projectId')
        if task_userId:
            user = Users.objects.get(userId=task_userId)
            Tasks.objects.filter(taskId=task_id).update(taskUserId=user)
            result.append('userId')
        if task_status:
            Users.objects.filter(taskId=task_id).update(taskStatus=task_status)
            result.append('status')

        if len(result) < 1:
            resp = {'message': '未修改数据', 'id': '2'}
        else:
            temp = '修改('
            for i in result:
                temp += i
                temp += ','
            temp += ')成功'
            resp = {'message': temp, 'id': '0'}

        return HttpResponse(json.dumps(resp))
    else:
        resp = {'message': '修改失败', 'id': '1'}
        return HttpResponse(json.dumps(resp))


@csrf_exempt
def get_user_info(request):
    if request.method == 'POST':
        user_id = request.POST.get('userId')
        user_email = request.POST.get('userEmail')
        print(user_id, ' ', user_email)
        user = None
        if user_id is not None:
            user_f = Users.objects.filter(userId=user_id)
            if user_f:
                user = Users.objects.get(userId=user_f[0].userId)
        if user_email is not None:
            user_f = Users.objects.filter(userEmail=user_email)
            if user_f:
                user = Users.objects.get(userEmail=user_f[0].userEmail)
        if user:
            print(user.userAvatar.url)
            resp = {'userId': user.userId,
                    'userEmail': user.userEmail,
                    'username': user.username,
                    'userPassword': '',
                    'userPhone': user.userPhone,
                    'userIdentity': user.userIdentity,
                    'userSex': user.userSex,
                    'userAvatar': user.userAvatar.url,
                    'userSignature': user.userSignature,
                    }
            return HttpResponse(json.dumps(resp))
        else:
            resp = {'taskId': '查询无结果', 'id': '1'}
            return HttpResponse(json.dumps(resp))


@csrf_exempt
def update_password(request):
    if request.method == 'POST':
        user_id = request.POST.get('userId')
        user_email = request.POST.get('userEmail')
        user_new_password = request.POST.get('userPassword')
        user = None
        if user_id is not None:
            user_f = Users.objects.filter(userId=user_id)
            if user_f:
                user = Users.objects.get(userId=user_f[0].userId)
        if user_email is not None:
            user_f = Users.objects.filter(userEmail=user_email)
            if user_f:
                user = Users.objects.get(userEmail=user_f[0].userEmail)
        if user:
            user.userPassword = user_new_password
            user.save()
            resp = {'message': '修改成功', 'id': '0'}
            return HttpResponse(json.dumps(resp))
        else:
            resp = {'taskId': '查询无结果', 'id': '1'}
            return HttpResponse(json.dumps(resp))


@csrf_exempt
def find_email_repeat(request):
    if request.method == 'POST':
        reg_email = request.POST.get('userEmail')
        result = Users.objects.filter(userEmail=reg_email)
        if result:
            resp = {'message': '不可注册已经重复', 'id': '1'}
            return HttpResponse(json.dumps(resp))
        else:
            resp = {'message': '可以注册', 'id': '0'}
            return HttpResponse(json.dumps(resp))


@csrf_exempt
def find_label_repeat(request):
    if request.method == 'POST':
        reg_label = request.POST.get('labelId')
        result = Labels.objects.filter(labelId=reg_label)
        if result:
            resp = {'message': '不可添加已经重复', 'id': '1'}
            return HttpResponse(json.dumps(resp))
        else:
            resp = {'message': '可以添加', 'id': '0'}
            return HttpResponse(json.dumps(resp))


@csrf_exempt
def user_task_date(request):
    if request.method == 'POST':
        user_id = request.POST.get('userId')
        start_date = request.POST.get('startDate')
        end_date = request.POST.get('endDate')
        tasks = Tasks.objects.filter(taskUserId=user_id)
        tasks_result = []
        if tasks:
            for i in tasks:
                if end_date > i.taskDueDate > start_date:
                    resp = {'taskId': i.taskId, 'taskTitles': i.taskTitles,
                            'taskComment': i.taskComment, 'taskDueDate': i.taskDueDate,
                            'taskPriority': i.taskPriority, 'taskProjectId': i.taskProjectId.projectId,
                            'taskUserId': user_id, 'taskStatus': i.taskStatus}
                    tasks_result.append(resp)
        print(tasks_result)
        return HttpResponse(json.dumps(tasks_result))
    else:
        resp = {'taskId': '查询无结果', 'id': '1'}
        return HttpResponse(json.dumps(resp))


@csrf_exempt
def user_task_status(request):
    if request.method == 'POST':
        user_id = request.POST.get('userId')
        status = request.POST.get('taskStatus')
        tasks = Tasks.objects.filter(taskUserId=user_id, taskStatus=status)
        tasks_result = []
        if tasks:
            for i in tasks:
                resp = {'taskId': i.taskId, 'taskTitles': i.taskTitles,
                        'taskComment': i.taskComment, 'taskDueDate': i.taskDueDate,
                        'taskPriority': i.taskPriority, 'taskProjectId': i.taskProjectId.projectId,
                        'taskUserId': user_id, 'taskStatus': i.taskStatus}
                tasks_result.append(resp)
        print(tasks_result)
        return HttpResponse(json.dumps(tasks_result))
    else:
        resp = {'taskId': '查询无结果', 'id': '1'}
        return HttpResponse(json.dumps(resp))


@csrf_exempt
def my_admin(request):
    if request.method == "POST":
        if not request.user.is_authenticated:
            print("已认证")
            users = Users.objects
            return render(request, "usercontrol.html", {"users": users})
        else:
            username = request.POST.get("username")
            password = request.POST.get("password")
            print("")
            user = auth.authenticate(request, username=username, password=password)
            if user:
                auth.login(request, user)
                users = Users.objects
                # tasks = Tasks.objects
                print("成功")
                return render(request, "usercontrol.html", {"users": users,"user": user})
            else:
                print("失败")
                return render(request, "myadmin.html")
    else:
        print("访问")
        return render(request, "myadmin.html")
