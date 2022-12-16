from django.db import models


class News(models.Model):
    text = models.TextField()
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
