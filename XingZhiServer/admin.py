from django.contrib import admin

# Register your models here.
from .models import Users, Projects, Labels, Tasks, TaskLabels


class UserAdmin(admin.ModelAdmin):
    fields = ['userEmail', 'username',
              'userPassword', 'userPhone', 'userIdentity',
              'userSex', 'userAvatar', 'userSignature']


admin.site.register(Users, UserAdmin)


class ProjectAdmin(admin.ModelAdmin):
    fields = ['projectName', 'projectColorName',
              'projectColorCode', 'projectUser']


admin.site.register(Projects, ProjectAdmin)


class LabelAdmin(admin.ModelAdmin):
    fields = ['labelName', 'labelColorName',
              'labelColorCode', 'labelUser']


admin.site.register(Labels, LabelAdmin)


class TaskAdmin(admin.ModelAdmin):
    fields = ['taskTitles', 'taskComment',
              'taskDueDate', 'taskPriority', 'taskProjectId',
              'taskUserId', 'taskStatus']


admin.site.register(Tasks, TaskAdmin)


class TaskLabelAdmin(admin.ModelAdmin):
    fields = ['taskId', 'labelId']


admin.site.register(TaskLabels, TaskLabelAdmin)
