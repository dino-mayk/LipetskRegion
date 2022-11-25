from django.shortcuts import get_object_or_404, render

from celebrities.models import CelebrityItem


def list(request):
    celebrities = CelebrityItem.objects.all()

    context = {
        'celebrities': celebrities,
    }

    return render(request, 'celebrities/list.html', context)


def detail(request, pk):
    celebrity = get_object_or_404(CelebrityItem.objects.all(), pk=pk)

    context = {
        'celebrity': celebrity,
    }

    return render(request, 'celebrities/detail.html', context)
