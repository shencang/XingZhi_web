from rest_framework import serializers

from XingZhiServer.models import Users, Projects, Labels, Tasks, TaskLabels

'''
json格式化model对象
'''


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('userId', 'userEmail', 'username',
                  'userPassword', 'userPhone', 'userIdentity',
                  'userSex', 'userAvatar', 'userSignature')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('projectId', 'projectName', 'projectColorName',
                  'projectColorCode', 'projectUser')


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Labels
        fields = ('labelId', 'labelName', 'labelColorName',
                  'labelColorCode', 'labelUser')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ('taskId', 'taskTitles', 'taskComment',
                  'taskDueDate', 'taskPriority', 'taskProjectId',
                  'taskUserId', 'taskStatus')


class TaskLabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskLabels
        fields = ('taskLabelId', 'taskId', 'labelId')
