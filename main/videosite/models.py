from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='юзер')
    photo = models.ImageField(upload_to='profile_photo', verbose_name='Фото')

    def __str__(self):
        return self.user.username


class VideoModel(models.Model):
    name = models.CharField(max_length=25, verbose_name='Назва')
    slug = models.SlugField(max_length=25, verbose_name='Слаг')
    prev = models.ImageField(upload_to='prev_photo', verbose_name="Прев'ю")
    video = models.FileField(upload_to='videos', verbose_name='Відео')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def uni(self):
        return reverse('detail_url', kwargs={'slug_v': self.slug})
