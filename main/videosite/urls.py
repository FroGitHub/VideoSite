from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    # links of Profile
    path('', Home.as_view(), name='home'),
    path('login', LoginPage.as_view(), name='login_url'),
    path('register', RegisterPage.as_view(), name='register_url'),
    path('logout', logout_user, name='logout_url'),
    path('update/<int:pk>', UpdatePage.as_view(), name='update_url'),

    # links of video
    path('video-create', CreateVideoPage.as_view(), name='create_video_url'),
    path('video/<slug:slug_v>', DetailsPage.as_view(), name='detail_url'),
    path('delete/<int:pk>', VideoDeletePage.as_view(), name='delete_url'),
    path('my-videos', MyVideo.as_view(), name='my_video_url')

]
