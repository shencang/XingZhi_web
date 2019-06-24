from django.db import models

# Create your models here.


'''
用户表
'''


class Users(models.Model):
    userId = models.AutoField(primary_key=True)  # 用户ID
    userEmail = models.EmailField(max_length=100)  # 电子邮件
    username = models.CharField(max_length=100, null=False)  # 用户名
    userPassword = models.CharField(max_length=100)  # 密码
    userPhone = models.CharField(max_length=12)  # 手机号
    userIdentity = models.CharField(max_length=2)  # 用户身份
    userAvatar = models.FileField(upload_to='media', null=False)  # 用户头像
    userSignature = models.CharField(max_length=100)  # 用户个性签名

    def __str__(self):
        return self.userEmail


'''
项目表
'''


class Projects(models.Model):
    projectId = models.AutoField(primary_key=True)  # 项目ID
    projectName = models.TextField()  # 项目名字
    projectColorName = models.TextField()  # 项目标题颜色
    projectColorCode = models.IntegerField()  # 项目颜色代码

    def __self__(self):
        return self.projectId


'''
标签表
'''


class Labels(models.Model):
    labelId = models.AutoField(primary_key=True)  # 标签ID
    labelName = models.TextField()  # 标签名字
    labelColorName = models.TextField()  # 标签标题颜色
    labelColorCode = models.IntegerField()  # 标签颜色代码

    def __self__(self):
        return self.labelId


'''
任务表
'''


class Tasks(models.Model):
    taskId = models.AutoField(primary_key=True)  # 任务ID
    taskTitles = models.TextField()  # 任务标题
    taskComment = models.TextField()  # 任务评论
    taskDueDate = models.IntegerField()  # 任务截止时间
    taskPriority = models.IntegerField()  # 任务优先级
    taskProjectId = models.IntegerField()  # 任务所属项目ID,外键
    taskUserId = models.IntegerField()  # 任务所属用户ID,外键
    taskStatus = models.IntegerField()  # 任务状态

    def __self__(self):
        return self.taskId


'''
任务和标签关系表
'''


class TaskLabels(models.Model):
    taskLabelId = models.AutoField(primary_key=True)  # 任务标签关系表ID
    taskId = models.IntegerField()  # 任务ID，外键
    labelId = models.IntegerField()  # 标签ID，外键

    def __self__(self):
        return self.taskLabelId


'''
用户项目关系表
'''


class UserProject(models.Model):
    userProjectId = models.AutoField(primary_key=True)  # 用户项目关系表ID
    userId = models.IntegerField()  # 用户ID，外键
    projectId = models.IntegerField()  # 项目ID，外键

    def __self(self):
        return self.userProjectId


'''
用户标签关系表
'''


class UserLabels(models.Model):
    userLabel = models.IntegerField(primary_key=True)  # 用户标签关系表ID
    userId = models.IntegerField()  # 用户id外键
    labelId = models.IntegerField()  # 标签id外键

    def __self__(self):
        return self.userLabel
