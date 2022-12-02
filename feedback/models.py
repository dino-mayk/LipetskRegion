from django.db import models


class Feedback(models.Model):
    text = models.TextField()
    created_on = models.DateTimeField(
        auto_now_add=True,
        verbose_name="дата создания",
        help_text="дата создания",
    )

    class Meta:
        verbose_name = "вопрос"
        verbose_name_plural = "вопросы"
