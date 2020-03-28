from django.shortcuts import render
from .models import *
from django.views.generic import CreateView, UpdateView, DeleteView, View
from django.contrib.auth import authenticate, login, views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden
from django.urls import reverse_lazy
from .forms import AuthUserForm, RegisterUserForm
from django.core.paginator import Paginator
from .mixins import GameMixin
from random import  randint
import json
# Create your views here.
class MainPage(View):
    def get(self, request):
        return render(request, 'wordsgame/index.html')


class MyLogin(views.LoginView):
    template_name = 'registration/login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('index_page_url')

    def get_success_url(self):
        return self.success_url


class RegisterUser(CreateView):
    model = GameUser
    template_name = 'registration/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('index_page_url')

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        auth_user = authenticate(username=username, password=password)
        login(self.request, auth_user)
        return form_valid


class MyLogout(views.LogoutView):
    next_page = reverse_lazy('index_page_url')


class GamePage(View):
    model = EmphWord
    template = 'wordsgame/games/emphgame.html'
    def get(self, request):
        words = self.model.objects.all()
        return render(request, self.template, context={'words': words})
    
    def post(self, request):
        word = EmphWord.objects.order_by('?').first()
        return HttpResponse(word.body)


class MyProfile(View):

    def get(self, request, current_user_page_name):
        if request.user.is_authenticated:
            if request.user.username == current_user_page_name:
                mist = request.user.mistake_set.all()
                return render(request, 'wordsgame/Myprofile.html', context={'mistakes': mist, 'profile':request.user})
            else:
                return HttpResponseNotFound('Пользователя с таким именем не существует')
        else:
            return HttpResponseForbidden('Для просмотра профиля необходимо быть авторизированным пользователем')

    def post(self, request, current_user_page_name):
        u = GameUser.objects.get(username=request.user.username)
        data = request.POST
        answer = data.get('answer')
        if answer == 'correct':
            u.static_correct += 1
            u.save()
        elif answer == 'incorrect':
            u.static_wrong += 1
            u.save()
            try:
                m = Mistake.objects.get(your_answer=data.get('youranswer'))
                m.count += 1
                m.save()
                return HttpResponse('ok')
            except:
                pass
            
            m = Mistake(your_answer=data.get('youranswer'), correct_answer=data.get('correct'), count=1)
            m.save()
            m.user_didit.add(u)
        return HttpResponse('ok')

class OvaGame(GameMixin, View):
    model = OvaWord
    template = 'wordsgame/games/ovagame.html'
class PreGame(GameMixin, View):
    model = PreWord
    template = 'wordsgame/games/pregame.html'
class IiGame(GameMixin, View):
    model = IiWord
    template = 'wordsgame/games/iigame.html'
class ZnakGame(GameMixin, View):
    model = ZnakWord
    template = 'wordsgame/games/znakgame.html'
class ChiGame(GameMixin, View):
    model = ChikWord
    template = 'wordsgame/games/chigame.html'
class OyoGame(GameMixin, View):
    model = OyoWord
    template = 'wordsgame/games/oyogame.html'


class RandomGame(View):
    def get(self, request):
        template = 'wordsgame/games/randomgame.html'
        return render(request, template)
    def post(self, request):
        models = (OvaWord, PreWord, IiWord, ZnakWord, ChikWord, OyoWord)
        i = randint(0, len(models)-1)
        model = models[i]
        word = model.objects.order_by('?').first()
        return HttpResponse(json.dumps({'word':word.body,'c': word.correct}))


def WordsList(request):
    search = request.GET.get('search', '')
    if search:
        words = EmphWord.objects.filter(body__icontains=search)
        context = {
            'words': words,
            'srch': search
        }
        return render(request, 'wordsgame/words_list.html', context=context)
    else:
        words = EmphWord.objects.all()
        paginator = Paginator(words, 50)
        page_number = request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        is_paginated = page.has_other_pages()
        if page.has_previous():
            prev_url = f'?page={page.previous_page_number()}'
        else:
            prev_url = ''
        if page.has_next():
            next_url = f'?page={page.next_page_number()}'
        else:
            next_url = ''
        context = {
            'words': words,
            'page_object': page,
            'is_paginated': is_paginated,
            'prev_url': prev_url,
            'next_url': next_url,
        }
    return render(request, 'wordsgame/words_list.html', context=context)
