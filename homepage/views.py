from django.shortcuts import render
from celebrities.models import CelebrityItem, CelebrityItemPreview


def home(request):
    ans = []

    celebrities = CelebrityItem.objects.all()[0:3]
    celebrities_images = CelebrityItemPreview.objects.all()[0:3]



    for i in range(len(celebrities)):
        ans.append(
            {
                'img': celebrities_images[i],
                'name': celebrities[i].name,
                'patronymic': celebrities[i].patronymic,
                'surname': celebrities[i].surname,
            }
        )
    context = {
        'celebrities': ans,
    }

    return render(request, 'homepage/index.html', context)
