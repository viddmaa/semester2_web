from django.shortcuts import render, get_object_or_404
from .models import Breed
from django.shortcuts import redirect
from .forms import FeedbackForm, BreedForm

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

def catalog(request):
    breeds = Breed.objects.all()
    context = {
        'title': 'Каталог пород',
        'breeds': breeds
    }
    return render(request, 'catlibrary/catalog.html', context)

def breed_detail(request, pk):
    breed = get_object_or_404(Breed, pk=pk)
    context = {
        'title': 'Каталог пород',
        'breed': breed
    }
    return render(request, 'catlibrary/breed_detail.html', context)

def contact(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)

            return redirect('catlibrary:home')

    else:
        form = FeedbackForm()

    return render(request, 'catlibrary/contact.html', {'form': form})

def breed_create(request):
    if request.method == 'POST':
        form = BreedForm(request.POST, request.FILES)
        if form.is_valid():
            breed = form.save()
            return redirect('catlibrary:breed_detail', pk=breed.pk)
    else:
        form = BreedForm()

    return render(request, 'catlibrary/form.html', {
        'form': form,
        'title': 'Добавление породы'
    })

def breed_update(request, pk):
    breed = get_object_or_404(Breed, pk=pk)

    if request.method == 'POST':
        form = BreedForm(request.POST, request.FILES, instance=breed)
        if form.is_valid():
            form.save()
            return redirect('catlibrary:breed_detail', pk=breed.pk)
    else:
        form = BreedForm(instance=breed)

    return render(request, 'catlibrary/form.html', {
        'form': form,
        'title': 'Редактирование породы'
    })