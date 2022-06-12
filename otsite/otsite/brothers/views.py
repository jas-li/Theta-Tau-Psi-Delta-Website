from django.shortcuts import render
from .forms import BrotherCreateForm

def brother_create_view(request):
    form = BrotherCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = BrotherCreateForm()

    context = {
        'form': form
    }

    return render(request, "brothers/brother_create.html", context)


