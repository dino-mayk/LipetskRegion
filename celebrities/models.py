from django.db import models
from django.utils.safestring import mark_safe
from django_cleanup.signals import cleanup_pre_delete
from sorl.thumbnail import delete, get_thumbnail
from tinymce.models import HTMLField

from landmarks.models import LandmarkItem


class CelebrityItem(models.Model):
    is_published = models.BooleanField(
        default=True,
        verbose_name="опубликовано"
    )
    name = models.CharField(
        max_length=150,
        verbose_name="имя",
        help_text="максимально 150 символов"
    )
    surname = models.CharField(
        max_length=150,
        verbose_name="фамилия",
        help_text="максимально 150 символов"
    )
    patronymic = models.CharField(
        max_length=150,
        verbose_name="отчество",
        help_text="максимально 150 символов"
    )
    text = HTMLField(
        verbose_name="описание",
        help_text="введите ваш текст"
    )
    landmark = models.ManyToManyField(
        LandmarkItem(),
        verbose_name="достопримечательности"
    )

    class Meta:
        verbose_name = "знаменитость"
        verbose_name_plural = "знаменитости"

    def __str__(self):
        return self.surname


class CelebrityItemPreview(models.Model):
    upload = models.ImageField(
        upload_to='uploads/celebrities/preview/%Y/%m',
        verbose_name="картинка",
        help_text='загрузите картинку'
    )
    celebrity = models.OneToOneField(
        CelebrityItem,
        on_delete=models.CASCADE,
        primary_key=True,
        verbose_name="знаменитость",
        help_text='выберете знаменитость'
    )

    @property
    def get_img(self):
        return get_thumbnail(self.upload, '300x300', crop='center', quality=51)

    def img_tmb(self):
        if self.upload:
            return mark_safe(
                f'<img src="{self.get_img.url}">'
            )
        return 'нет изображений'

    img_tmb.short_description = 'превьюшка'
    img_tmb.allow_tags = True

    def sorl_delete(**kwargs):
        delete(kwargs['file'])

    cleanup_pre_delete.connect(sorl_delete)

    def __str__(self):
        return self.upload.url

    class Meta:
        verbose_name = "фотографию знаменитости"
        verbose_name_plural = "превьюшки знаменитостей"


class CelebrityItemGallery(models.Model):
    upload = models.ImageField(
        upload_to='uploads/celebrities/gallery/%Y/%m',
        verbose_name="картинка",
        help_text='загрузите картинку'
    )
    celebrity = models.ForeignKey(
        CelebrityItem,
        on_delete=models.CASCADE,
        verbose_name="знаменитость",
        help_text='выберете знаменитость'
    )

    @property
    def get_img(self):
        return get_thumbnail(self.upload, '300x300', crop='center', quality=51)

    def img_tmb(self):
        if self.upload:
            return mark_safe(
                f'<img src="{self.get_img.url}">'
            )
        return 'нет изображений'

    img_tmb.short_description = 'фотогалерея'
    img_tmb.allow_tags = True

    def sorl_delete(**kwargs):
        delete(kwargs['file'])

    cleanup_pre_delete.connect(sorl_delete)

    def __str__(self):
        return self.upload.url

    class Meta:
        verbose_name = "фотографию знаменитости"
        verbose_name_plural = "фотогалерея знаменитостей"
