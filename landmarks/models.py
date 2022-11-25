from django.db import models
from django.utils.safestring import mark_safe
from django_cleanup.signals import cleanup_pre_delete
from sorl.thumbnail import delete, get_thumbnail
from tinymce.models import HTMLField


class LandmarkItem(models.Model):
    is_published = models.BooleanField(
        default=True,
        verbose_name="опубликовано"
    )
    name = models.CharField(
        max_length=150,
        verbose_name="имя",
        help_text="максимально 150 символов"
    )
    text = HTMLField(
        verbose_name="описание",
        help_text="введите ваш текст"
    )
    link = models.CharField(
        max_length=150,
        verbose_name="ссылка",
        help_text="максимально 150 символов"
    )

    class Meta:
        verbose_name = "достопримечательность"
        verbose_name_plural = "достопримечательности"

    def __str__(self):
        return self.name


class LandmarkItemPreview(models.Model):
    upload = models.ImageField(
        upload_to='uploads/landmarks/preview/%Y/%m',
        verbose_name="картинка",
        help_text='загрузите картинку'
    )
    landmark = models.OneToOneField(
        LandmarkItem,
        on_delete=models.CASCADE,
        primary_key=True,
        verbose_name="достопримечательность",
        help_text='выберете достопримечательность'
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
        verbose_name = "фотографию достопримечательности"
        verbose_name_plural = "превьюшки достопримечательностей"


class LandmarkItemGallery(models.Model):
    upload = models.ImageField(
        upload_to='uploads/landmarks/gallery/%Y/%m',
        verbose_name="картинка",
        help_text='загрузите картинку'
    )
    landmark = models.ForeignKey(
        LandmarkItem,
        on_delete=models.CASCADE,
        verbose_name="достопримечательность",
        help_text='выберете достопримечательность'
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
        verbose_name = "фотографию достопримечательности"
        verbose_name_plural = "фотогалерея достопримечательностей"
