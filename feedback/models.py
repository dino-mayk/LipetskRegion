from django.db import models


class Feedback(models.Model):
    text = models.TextField(
        verbose_name="текст",
        help_text="введите ваш текст",
    )
    created_on = models.DateTimeField(
        auto_now_add=True,
        verbose_name="дата создания",
        help_text="дата создания",
    )

    class Meta:
        verbose_name = "вопрос"
        verbose_name_plural = "вопросы"
