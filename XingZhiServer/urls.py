from django.conf.urls import url
from django.conf.urls import include
from rest_framework import routers

from XingZhiServer import views

app_name = '[XingZhiServer]'

router = routers.DefaultRouter()
router.register(r'user', views.UserSet)
router.register(r'project', views.ProjectSet)
router.register(r'label', views.LabelSet)
router.register(r'task', views.TaskSet)
router.register(r'tasklabel', views.TaskLabelsSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
