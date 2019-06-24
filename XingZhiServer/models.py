from django.db import models

# Create your models here.


'''
用户表
'''


class Users(models.Model):
    UserEmail = models.EmailField(max_length=100, primary_key=True)  # 电子邮件
    Username = models.CharField(max_length=100, null=False)  # 用户名
    UserPassword = models.CharField(max_length=100)  # 密码
    UserPhone = models.CharField(max_length=12)  # 手机号
    UserIdentity = models.CharField(max_length=2)  # 用户身份
    UserAvatar = models.FileField(upload_to='media', null=False)  # 用户头像
    UserSignature = models.CharField(max_length=100)  # 用户个性签名

    def __str__(self):
        return self.UserEmail


'''
项目表
'''


class Projects(models.Model):
    projectId = models.AutoField(primary_key=True),  # 项目ID
    projectName = models.TextField(),  # 项目名字
    projectColorName = models.TextField(),  # 项目标题颜色
    projectColorCode = models.IntegerField(),  # 项目颜色代码

    def __self__(self):
        return self.projectId


'''
标签表
'''


class Labels(models.Model):
    labelId = models.AutoField(primary_key=True)  # 标签ID
    labelName = models.TextField(),  # 标签名字
    labelColorName = models.TextField(),  # 标签标题颜色
    labelColorCode = models.IntegerField(),  # 标签颜色代码


'''
任务和标签关系表
'''


class TaskLabels(models.Model):
    taskLabelId = models.AutoField(primary_key=True),  # 任务标签关系表
    taskId = models.IntegerField()  # 任务ID，外键
    labelId = models.IntegerField()  # 标签ID，外键


'''
任务表
'''


class Tasks(models.Model):
    taskId = models.AutoField(primary_key=True),  # 任务ID
    taskTitles = models.TextField(),  # 任务标题
    taskComment = models.TextField(),  # 任务评论
    taskDueDate = models.IntegerField(),  # 任务截止时间
    taskPriority = models.IntegerField(),  # 任务优先级
    taskProjectID = models.IntegerField(),  # 任务所属项目ID，外键
    taskStatus = models.IntegerField(),  # 任务状态
