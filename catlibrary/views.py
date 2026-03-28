from django.shortcuts import render


def index(request):
    context = {
        'title': 'Библиотека пород кошек',
        'welcome_text': 'Добро пожаловать на наш лучший сайт о кошках!'
    }
    return render(request, 'catlibrary/index.html', context)

def care(request):
    context = {
        'title': 'Уход за кошками'
    }
    return render(request, 'catlibrary/care.html', context)

def about(request):
    context = {
        'title': 'О нас'
    }
    return render(request, 'catlibrary/about.html', context)

def faq(request):
    context = {
        'title': 'Часто задаваемые вопросы'
    }
    return render(request, 'catlibrary/faq.html', context)