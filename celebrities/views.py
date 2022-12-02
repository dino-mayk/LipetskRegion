from django.shortcuts import get_object_or_404, render

from celebrities.models import CelebrityItem, CelebrityItemPreview


def list(request):
    ans = []

    celebrities = CelebrityItem.objects.all()
    celebrities_images = CelebrityItemPreview.objects.all()

    for i in range(len(celebrities)):
        ans.append(
            {
                'img': celebrities_images[i],
                'name': celebrities[i].name,
                'surname': celebrities[i].surname,
                'patronymic': celebrities[i].patronymic,
                'text': celebrities[i].text
            }
        )
    context = {
        'celebrities': ans,
    }

    return render(request, 'celebrities/list.html', context)


def detail(request, pk):
    celebrity = get_object_or_404(CelebrityItem.objects.all(), pk=pk)

    context = {
        'celebrity': celebrity,
    }

    return render(request, 'celebrities/detail.html', context)
