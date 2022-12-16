from django.db import models
from tinymce.models import HTMLField


class News(models.Model):
    text = HTMLField(
        verbose_name="описание",
        help_text="введите ваш текст"
    )
    created_on = models.DateTimeField(
        auto_now_add=True,
        verbose_name="дата создания",
        help_text="дата создания",
    )

    def __str__(self):
        return f'новость номер {self.id}'
    

    class Meta:
        verbose_name = "новость"
        verbose_name_plural = "новости"
