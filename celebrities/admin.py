from django.contrib import admin

from celebrities.models import CelebrityItem, CelebrityItemGallery, \
    CelebrityItemPreview


class CelebrityItemAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "surname",
        "patronymic",
        "is_published",
    )
    list_editable = ("is_published", )
    list_display_links = ("name", "surname", "patronymic", )


class CelebrityItemImageAdmin(admin.ModelAdmin):
    list_display = (
        "celebrity",
        "img_tmb",
    )


admin.site.register(CelebrityItem, CelebrityItemAdmin)
admin.site.register(CelebrityItemPreview, CelebrityItemImageAdmin)
admin.site.register(CelebrityItemGallery, CelebrityItemImageAdmin)
