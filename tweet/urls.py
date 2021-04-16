from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posttweet/', views.posttweet, name='posttweet'),
    path('<int:id>/tweetdetail/', views.tweetdetail, name='tweetdetail'),
    path('<int:id>/reply',views.reply, name="reply"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)