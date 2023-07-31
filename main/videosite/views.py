from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from .models import *
from .forms import *


# ====================================================(All classes of the Videos are below)
class Home(ListView):  # Default list
    template_name = 'videosite/home.html'
    model = VideoModel
    context_object_name = 'videos'
    paginate_by = 3


class MyVideo(ListView):  # My videos
    template_name = 'videosite/home.html'
    model = VideoModel
    context_object_name = 'videos'
    paginate_by = 3

    def get_queryset(self):
        author = self.request.user
        return VideoModel.objects.filter(author=author)  # Filter for my video


class CreateVideoPage(CreateView):
    template_name = 'videosite/formpage.html'
    form_class = CreateVideoForm
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Додати відео'
        context['button_text'] = 'Додати'
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DetailsPage(DetailView):  # Page after click on prev
    template_name = 'videosite/detail.html'
    model = VideoModel
    context_object_name = 'video'
    slug_url_kwarg = "slug_v"


class VideoDeletePage(DeleteView):  # Delete page
    template_name = 'videosite/deleteform.html'
    model = VideoModel
    success_url = reverse_lazy('home')


# ====================================================(All classes of Profile are below)


class RegisterPage(CreateView):
    template_name = 'videosite/formpage.html'
    form_class = RegisterForm
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Реєстрація'
        context['button_text'] = 'Зареєструватися'
        return context

    def form_valid(self, form):
        user = form.save()
        ProfileModel.objects.create(user=user, photo='profile_photo/default.jpg')
        login(self.request, user)
        return redirect('home')


class LoginPage(LoginView):
    template_name = 'videosite/formpage.html'
    form_class = LoginForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизація'
        context['button_text'] = 'Авторизуватися'
        return context

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')


class UpdatePage(UpdateView):  # Change profile`s foto
    template_name = 'videosite/formpage.html'
    model = ProfileModel
    fields = ['photo']
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактор'
        context['button_text'] = 'Змінити'
        return context
