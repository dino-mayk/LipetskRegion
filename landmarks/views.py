from django.shortcuts import get_object_or_404, render

from landmarks.models import LandmarkItem


def list(request):
    landmarks = LandmarkItem.objects.all()

    context = {
        'landmarks': landmarks,
    }

    return render(request, 'landmarks/list.html', context)


def detail(request, pk):
    landmark = get_object_or_404(LandmarkItem.objects.all(), pk=pk)

    context = {
        'landmark': landmark,
    }

    return render(request, 'landmarks/detail.html', context)
