from django.contrib import admin

# Register your models here.
from .models import Users, Projects, Labels, Tasks, TaskLabels


class UserAdmin(admin.ModelAdmin):
    list_display = ['userId','userEmail', 'username']
    fields = ['userEmail', 'username',
              'userPassword', 'userPhone', 'userIdentity',
              'userSex', 'userAvatar', 'userSignature']


admin.site.register(Users, UserAdmin)


class ProjectAdmin(admin.ModelAdmin):

    list_display = ['projectId','projectName','projectUser']
    fields = ['projectName', 'projectColorName',
              'projectColorCode', 'projectUser']


admin.site.register(Projects, ProjectAdmin)


class LabelAdmin(admin.ModelAdmin):
    list_display = ['labelId','labelName', 'labelUser']
    fields = ['labelName', 'labelColorName',
              'labelColorCode', 'labelUser']


admin.site.register(Labels, LabelAdmin)


class TaskAdmin(admin.ModelAdmin):
    list_display = ['taskId','taskTitles','taskUserId']
    fields = ['taskTitles', 'taskComment',
              'taskDueDate', 'taskPriority', 'taskProjectId',
              'taskUserId', 'taskStatus']


admin.site.register(Tasks, TaskAdmin)


class TaskLabelAdmin(admin.ModelAdmin):
    list_display = ['taskLabelId','taskId', 'labelId']
    fields = ['taskId', 'labelId']


admin.site.register(TaskLabels, TaskLabelAdmin)
