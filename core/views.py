from django.shortcuts import render

from .forms import Contact

def index(request):
    is_valid = False
    if request.method == 'POST':
        form = Contact(request.POST)
        if form.is_valid():
            form.send_mail()
            form = Contact()
            is_valid = True
    else:
        form = Contact()
    context = {
        'form': form,
        'is_valid': is_valid,
    }
    return render(request, 'index.html', context)