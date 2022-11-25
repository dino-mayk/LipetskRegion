from django.core.mail import send_mail
from django.shortcuts import redirect, render

from feedback import forms


def feedback(request):
    template = 'feedback/question.html'

    form = forms.FormFeedback(request.POST or None)
    context = {
        'form': form
    }

    if form.is_valid():
        form.save()

        send_mail(
            'Theme of letter',
            form.cleaned_data.get('text'),
            'from@example.com',
            ['to_1@example.com', 'to_2@example.com'],
            fail_silently=False
        )

        return redirect('feedback:feedback')

    return render(request, template, context)
