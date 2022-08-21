from django.shortcuts import render, redirect
from .models import Hello
from .forms import HelloForm


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def hellos(request):
    hello = Hello.objects.order_by('-id')
    return render(request, 'main/hellos.html', {'title': "Приветы", 'hellos': hello})


def create_hello(request):
    error = ''
    if request.method == 'POST':
        form = HelloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hellos')
        else:
            error = 'Что-то с вашим приветом не так('


    form = HelloForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create-hello.html', context)
