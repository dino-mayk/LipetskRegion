from django.contrib import admin

from landmarks.models import (LandmarkItem, LandmarkItemGallery,
                              LandmarkItemPreview)


class LandmarkItemAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "is_published",
    )
    list_editable = ("is_published", )
    list_display_links = ("name", )


class LandmarkItemImageAdmin(admin.ModelAdmin):
    list_display = (
        "landmark",
        "img_tmb",
    )


admin.site.register(LandmarkItem, LandmarkItemAdmin)
admin.site.register(LandmarkItemPreview, LandmarkItemImageAdmin)
admin.site.register(LandmarkItemGallery, LandmarkItemImageAdmin)
