from cProfile import Profile
from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView, TemplateView
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages
from  django.contrib.auth import login, logout
from django.urls import reverse_lazy
from .models import *

import random


class IndexPage(TemplateView):
    # Главная страница
    template_name = "lisovenkovaads_app/index.html"


def register_page(request):
    # Страница регистрации
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация прошла успешно.')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка регистрации.')
    else:
        form = UserRegisterForm()

    context = {
        'form': form,
    }
    return render(request=request, template_name='lisovenkovaads_app/register.html', context=context)


def login_page(request):
    # Страница авторизации
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = UserLoginForm()

    context = {
        'form': form,
    }

    return render(request=request, template_name='lisovenkovaads_app/login.html', context=context)


def logout_page(request):
    # Функция выхода из аккаунта
    logout(request)
    return redirect('login')


@login_required(login_url='/login/')
def profile_page(request):
    # Личный кабинет пользователя
    user_id = request.user.id
    ads = Ads.objects.filter(ads_author_id=user_id)
    categories = Category.objects.all()

    context = {'ads': ads, 'categories': categories, 'user_id': user_id}

    return render(request=request, template_name='lisovenkovaads_app/profile.html', context=context)


@login_required(login_url='/login/')
def ads_form_page(request):
    # Страница для размещения рекламного объявления
    error = ''
    if request.method == 'POST':
        form = AdsForm(request.POST, request.FILES)
        if form.is_valid():
            new_homework = form.save(commit=False)
            new_homework.ads_author = request.user
            new_homework.save()
        else:
            error = 'Форма была неверной.'
    form = AdsForm()

    data = {
        'form': form,
        'error': error,    
    }
    return render(request=request, template_name='lisovenkovaads_app/form.html', context=data)


class GetAds(DetailView):
    # Страница рекламного объявления
    model = Ads
    template_name = 'lisovenkovaads_app/ads.html'
    context_object_name = 'ads'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    

class ScriptFormPage(CreateView):
    # Страница с формой для получения скрипта
    template_name = 'lisovenkovaads_app/get_script.html'
    form_class = ScriptForm
    success_url = reverse_lazy('script')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


@login_required(login_url='/login/')
def script_page(request):
    # Страница со скриптом
    ads = Ads.objects.all()
    
    ads_list = []

    for item in ads:
        ads_list.append(item)

    script_ads = random.choice(ads_list)

    context = {'script_ads': script_ads,}

    return render(request=request, template_name='lisovenkovaads_app/script.html', context=context)

