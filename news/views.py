from django.core.mail import send_mail
from django.shortcuts import redirect, render

from news.models import News

def news(request):
    news = News.objects.all()
    context = {
        'news': news
    }

    template = 'news/list.html'

    return render(request, template, context=context)