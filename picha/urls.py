from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

from rest_framework import routers
from photos.views import PhotoViewSet

router = routers.DefaultRouter()
router.register(r'photos', PhotoViewSet)

# ** Templates do projeto antigo
#from photos.views import PhotoView
#from feedback.views import FeedbackView

urlpatterns = [
    #url(r'^$', PhotoView.as_view(), name="home"),
    #url(r'^feedback/$', FeedbackView.as_view(), name="feedback"),
    url(r'^admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
]
