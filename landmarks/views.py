from django.shortcuts import get_object_or_404, render

from landmarks.models import LandmarkItem, LandmarkItemPreview


def list(request):
    ans = []

    landmarks = LandmarkItem.objects.all()
    landmarks_images = LandmarkItemPreview.objects.all()

    for i in range(len(landmarks)):
        ans.append(
            {
                'img': landmarks_images[i],
                'name': landmarks[i].name,
                'text': landmarks[i].text,
                'link': landmarks[i].link
            }
        )
    context = {
        'landmarks': ans,
    }

    return render(request, 'landmarks/list.html', context)


def detail(request, pk):
    landmark = get_object_or_404(LandmarkItem.objects.all(), pk=pk)

    context = {
        'landmark': landmark,
    }

    return render(request, 'landmarks/detail.html', context)
